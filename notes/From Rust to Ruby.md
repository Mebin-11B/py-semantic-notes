---
title: "From Rust to Ruby"
url: https://xlii.space/eng/from-rust-to-ruby/
clipped: 2026-06-17 00:57:05
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [From Rust to Ruby](https://xlii.space/eng/from-rust-to-ruby/)

## Digest Summary
None

## Discussion Summary
The comments reveal a mixed reaction to the AI‑driven code conversion and the language comparison it presents. While several contributors acknowledge that large language models can speed up development and appreciate Ruby’s concise syntax and developer‑friendly ergonomics, many criticize the reliance on AI without verification, question the claimed stability loss without static types, and dispute the portrayed superiority of Ruby over Rust or Go. Skepticism about exaggerated metrics, concerns over maintainability, and divergent preferences for language verbosity also emerge as recurring themes.

---

## Full Article

2026-05-26

From Rust to Ruby
=================

Who does things like that?!?

Apparently: me.

I have my own project, written in Rust. Not a big one, mind you, maybe approx. 30k lines of code in total. Rust is verbose so it’s not really that impressive. I’ve put it aside for some time and was toying with local inference, LLMs, writing agents and my attention was brought to Ruby.

It’s been a while. So I had to take a look around to remind myself what Ruby and Ruby on Rails are doing nowadays. They’re doing quite well. There are some typing initiatives (Sorbet), and the language itself is terse as ever.

And then I had this thought… But an introduction is in order first: In my Rust app I have an isolated crate that’s pretty much a webapp written with Tera and Axum. 14,943 lines of Rust code in total, around 10s of compilation time (maybe the code isn’t big, but it pulls the whole universe behind itself) and then quite heavy E2E tests involving setting up Playwright and (because of the near-impossibility of mocking) an isolated database namespace and mocking services (along with a very special internal-api crate that allows Playwright to interact with the app in headless mode…).

So I thought “hmm, I wonder if I can get my Local Qwen3.6 to do a oneshot conversion”. But before I did so I researched first. I asked a few instances to analyse the project in terms of gains of complexity, stability, testability, etc., and while (obviously) stability would drop (no types in Ruby) it’s not that awful (Sorbet has types in Ruby!).

```
 ┌─────────────────────────────────┬──────────────────┬───────┬────────────────┐
 │ Area                            │ Rust/Axum/Diesel │ Rails │ Rails + Sorbet │
 ├─────────────────────────────────┼──────────────────┼───────┼────────────────┤
 │ Suitability for solo dev        │ 60               │ 90    │ 85             │
 ├─────────────────────────────────┼──────────────────┼───────┼────────────────┤
 │ Development speed               │ 40               │ 90    │ 75             │
 ├─────────────────────────────────┼──────────────────┼───────┼────────────────┤
 │ Safety                          │ 95               │ 55    │ 80             │
 ├─────────────────────────────────┼──────────────────┼───────┼────────────────┤
 │ Development complexity          │ 70               │ 90    │ 75             │
 ├─────────────────────────────────┼──────────────────┼───────┼────────────────┤
 │ Performance                     │ 95               │ 50    │ 50             │
 ├─────────────────────────────────┼──────────────────┼───────┼────────────────┤
 │ Boilerplate                     │ 30               │ 85    │ 80             │
 ├─────────────────────────────────┼──────────────────┼───────┼────────────────┤
 │ E2E testing testability         │ 40               │ 75    │ 75             │
 ├─────────────────────────────────┼──────────────────┼───────┼────────────────┤
 │ Unit testability                │ 20               │ 90    │ 90             │
 ├─────────────────────────────────┼──────────────────┼───────┼────────────────┤
 │ Integration testing testability │ 30               │ 85    │ 85             │
 ├─────────────────────────────────┼──────────────────┼───────┼────────────────┤
 │ Sum                             │ 480              │ 710   │ 695            │
 └─────────────────────────────────┴──────────────────┴───────┴────────────────┘
```

So in the end it seems I have *(licks finger and turns to the wind)* 1.47x better outcomes if the app were a Ruby on Rails app instead.

![interesting](https://xlii.space/Users/xlii/Downloads/interesting.png)
![ai-generated image of Bugs Bunny saying i-i-i-i-i-i-nteresting](https://xlii.space/images/interesting_hu_34b1b1d720ec0f69.png)

I have a local LLM running on my (bought it for gaming pre-AI craze) 4090 Ti - I’m a free man with unlimited tokens. So I thought: BRING IT ON!

Since it is a relatively small project the conversion took ~30 minutes. I have no idea if it works or not because I haven’t yet tried running it. But there is one thing I checked, and stared at in horror:

```
$ fd . -e rs -uu | xargs cat | wc -l
   14943
$ fd . -e rb -uu | xargs cat | wc -l
    3322
```

![ai-generated image of Bugs Bunny winning formula-1-like race with a huge 77% balloon](https://xlii.space/images/77percent_hu_5d42af2b93af7702.png)

That’s right folks! 77% decrease in line count; 4.49 lines of Rust code for each line of Ruby.

I browsed the Ruby code and it looks… fine. There are probably some bugs (no bunnies) but I must say it’s looking clean and idiomatic for my dated eye. I’m going to examine it further with some things in mind:

* I can add types using Agents, so probably type safety can be alleviated
* Ruby/Rails is pretty much batteries+kitchen sink included, which beats 3GiB of compiled deps.
* Testing will be *SO MUCH EASIER*

  ```
     VCR.use_cassette("llm_call") do
       result = LlmClient.match(entry, data_list)
       expect(result.results.size).to eq(data_list.size)
     end
  ```

  vs

  ```
  #[derive(Debug)]
  pub struct MockProvider {
    responses: Arc<RwLock<Vec<Response>>>,
    call_count: Arc<AtomicUsize>,
  }

  impl Default for MockProvider {
    fn default() -> Self {
      Self {
        responses: Arc::new(RwLock::new(vec![Response::default()])),
        call_count: Arc::new(AtomicUsize::new(0)),
      }
    }
  }

  impl MockProvider {
    pub fn new(responses: Vec<Response>) -> Self {
      Self {
        responses: Arc::new(RwLock::new(responses)),
        call_count: Arc::new(AtomicUsize::new(0)),
      }
    }
  }

  #[async_trait]
  impl Provider for MockProvider {
    async fn match(&self, entry: &Entry, data_list: &[Data]) -> Result<MatchResult> {
      self.call_count.fetch_add(1, Ordering::SeqCst);
      let responses = self.responses.read().await;
      Ok(MatchResult { results: responses.clone() })
    }
  }

  #[cfg(test)]
  mod tests {
    use super::*;

    #[tokio::test]
    async fn test_mock_provider_returns_expected_results() {
      let expected = vec![Response::default()];
      let provider = MockProvider::new(expected.clone());
      let result = provider.match(&Entry::default(), &[]).await.unwrap();
      assert_eq!(result.results, expected);
      assert_eq!(provider.call_count.load(Ordering::SeqCst), 1);
    }
  }
  ```

  …you get the *vibe*, right?

The benefits of working on your own project are, well, you can make crazy decisions, and I’ll be looking at this one *very closely*.