---
title: "GitHub - runetes/maiao: Seamless GitHub PR management from the command-line · GitHub"
url: https://github.com/runetes/maiao
clipped: 2026-08-31 12:26:35
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [GitHub - runetes/maiao: Seamless GitHub PR management from the command-line · GitHub](https://github.com/runetes/maiao)

## Full Article

[Skip to content](https://github.com/runetes/maiao#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      
    

      
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

  

  

      

        
            
  
      
    
    
      [runetes](https://github.com/runetes)    
    /
    
      [maiao](https://github.com/runetes/maiao)
    

    Public
  
    
      forked from [adevinta/maiao](https://github.com/adevinta/maiao)
    

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Frunetes%2Fmaiao)    You must be signed in to change notification settings

  

  
- 
          [Fork
    2](https://github.com/login?return_to=%2Frunetes%2Fmaiao)
  

  
- 
        
        [Star
          167](https://github.com/login?return_to=%2Frunetes%2Fmaiao)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/runetes/maiao/branches)[Tags](https://github.com/runetes/maiao/tags)Go to fileCodeOpen more actions menu  

## Latest commit

 

## History

[107 Commits](https://github.com/runetes/maiao/commits/main/)107 Commits

## Folders and files

NameNameLast commit messageLast commit date[.github](https://github.com/runetes/maiao/tree/main/.github)[.github](https://github.com/runetes/maiao/tree/main/.github)  [HomebrewFormula](https://github.com/runetes/maiao/tree/main/HomebrewFormula)[HomebrewFormula](https://github.com/runetes/maiao/tree/main/HomebrewFormula)  [cmd/maiao](https://github.com/runetes/maiao/tree/main/cmd/maiao)[cmd/maiao](https://github.com/runetes/maiao/tree/main/cmd/maiao)  [docs](https://github.com/runetes/maiao/tree/main/docs)[docs](https://github.com/runetes/maiao/tree/main/docs)  [pkg](https://github.com/runetes/maiao/tree/main/pkg)[pkg](https://github.com/runetes/maiao/tree/main/pkg)  [scripts](https://github.com/runetes/maiao/tree/main/scripts)[scripts](https://github.com/runetes/maiao/tree/main/scripts)  [.dockerignore](https://github.com/runetes/maiao/blob/main/.dockerignore)[.dockerignore](https://github.com/runetes/maiao/blob/main/.dockerignore)  [.gitignore](https://github.com/runetes/maiao/blob/main/.gitignore)[.gitignore](https://github.com/runetes/maiao/blob/main/.gitignore)  [.release-please-manifest.json](https://github.com/runetes/maiao/blob/main/.release-please-manifest.json)[.release-please-manifest.json](https://github.com/runetes/maiao/blob/main/.release-please-manifest.json)  [CHANGELOG.md](https://github.com/runetes/maiao/blob/main/CHANGELOG.md)[CHANGELOG.md](https://github.com/runetes/maiao/blob/main/CHANGELOG.md)  [CONTRIBUTING.md](https://github.com/runetes/maiao/blob/main/CONTRIBUTING.md)[CONTRIBUTING.md](https://github.com/runetes/maiao/blob/main/CONTRIBUTING.md)  [DISCLAIMER.md](https://github.com/runetes/maiao/blob/main/DISCLAIMER.md)[DISCLAIMER.md](https://github.com/runetes/maiao/blob/main/DISCLAIMER.md)  [LICENSE](https://github.com/runetes/maiao/blob/main/LICENSE)[LICENSE](https://github.com/runetes/maiao/blob/main/LICENSE)  [go.mod](https://github.com/runetes/maiao/blob/main/go.mod)[go.mod](https://github.com/runetes/maiao/blob/main/go.mod)  [go.sum](https://github.com/runetes/maiao/blob/main/go.sum)[go.sum](https://github.com/runetes/maiao/blob/main/go.sum)  [license_test.go](https://github.com/runetes/maiao/blob/main/license_test.go)[license_test.go](https://github.com/runetes/maiao/blob/main/license_test.go)  [mise.toml](https://github.com/runetes/maiao/blob/main/mise.toml)[mise.toml](https://github.com/runetes/maiao/blob/main/mise.toml)  [release-please-config.json](https://github.com/runetes/maiao/blob/main/release-please-config.json)[release-please-config.json](https://github.com/runetes/maiao/blob/main/release-please-config.json)  View all files

## Repository files navigation

# Maiao

Note: This is a community fork of [adevinta/maiao](https://github.com/adevinta/maiao). The original maintainers are no longer at Adevinta and the upstream repository is no longer actively maintained. This fork continues development under [runetes/maiao](https://github.com/runetes/maiao).

Gerrit-style code review workflow for GitHub, GitLab, Gitea, Forgejo, Bitbucket Cloud, and Cursor Origin

Maiao brings the power of stacked pull requests (or merge requests) to your git hosting provider, enabling you to break large features into small, reviewable commits where each commit becomes its own PR/MR.

## What is Maiao?

Maiao provides the  `git review`  command that:

- Creates one PR/MR per commit in your branch

- Stacks PRs/MRs automatically with proper parent-child dependencies

- Registers native stacks when available (GitHub Stacks, GitLab auto-detected stacks)

- Manages fixups elegantly using  `git commit --fixup` 

- Tracks commits via Change-IDs (using the Gerrit commit-msg hook)

- Auto-rebases your stack when PRs/MRs get merged

- Auto-detects your provider from the remote URL

## Supported Providers

Provider
PR/MR type
WIP/Draft
Native stacks

GitHub
Pull Request
API field
Yes (explicit registration)

GitLab
Merge Request
 `Draft:`  title prefix
Yes (auto-detected from target branch, up to 20 MRs)

Gitea
Pull Request
 `WIP:`  title prefix
No

Forgejo/Codeberg
Pull Request
 `WIP:`  title prefix
No

Bitbucket Cloud
Pull Request
Not supported
No

Cursor Origin (beta)
Pull Request
API field
Yes ( `parentPullNumber` )

Maiao auto-detects the provider from your remote URL for known hosts ( `github.com` ,  `gitlab.com` ,  `codeberg.org` ,  `bitbucket.org` ,  `origin.cursor.com` ). For self-hosted instances, it prompts on first use and saves the choice to  `git config maiao.provider` .

## Quick Example

 `# Make multiple commits
git commit -m "Add user authentication"
git commit -m "Add authorization middleware"
git commit -m "Add admin endpoints"

# Create stacked PRs/MRs for all commits
git review` 

Result: Three PRs/MRs created and stacked:

- PR #1:  `Add user authentication`  →  `main` 

- PR #2:  `Add authorization middleware`  → PR #1

- PR #3:  `Add admin endpoints`  → PR #2

## Key Benefits

- Granular Reviews: Each commit reviewed independently for faster, focused feedback

- Clear History: One logical change per PR/MR maintains clean git history

- Easy Fixups: Address review feedback with  `git commit --fixup <sha>` 

- Automatic Stacking: Tool manages PR/MR dependencies automatically

- Native Stacks: Integrates with GitHub Stacks and GitLab's auto-detected stacks

- Merge Detection: Stack updates automatically when PRs/MRs merge

- Rebase Integration: Handles upstream changes gracefully

- Multi-Provider: Works across GitHub, GitLab, Gitea, Forgejo, Bitbucket Cloud, and Cursor Origin

## Native GitHub Stacks

Maiao treats [GitHub native stacks](https://github.blog/changelog/2024-10-25-github-stacked-pull-requests/) as a progressive enhancement. When two or more PRs are pushed, Maiao probes the Stacks API (cached for 24 hours) and registers the PRs as a stack if supported. On older GitHub Enterprise instances the feature is silently skipped — branch-based stacking still works as before.
 `# Control via git config (default: auto)
git config maiao.useNativeStack auto   # use when available, skip otherwise
git config maiao.useNativeStack true   # always register; warn if unavailable
git config maiao.useNativeStack false  # disable entirely` 

## Documentation

- [Getting Started](https://github.com/runetes/maiao/blob/main/docs/getting-started.md) - Installation and workflow guide

- [How Does It Work](https://github.com/runetes/maiao/blob/main/docs/how-does-it-work.md) - Technical details and architecture

- [Pricing](https://github.com/runetes/maiao/blob/main/docs/pricing.md) - Free and open source

## Learn About Stacked Diffs

Maiao implements the stacked diffs methodology. Learn more:

- [Stacked Diffs Versus Pull Requests](https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/) - Jackson Gabbard's foundational article on the philosophy

- [Graphite's Guide to Stacked Diffs](https://graphite.dev/guides/stacked-diffs) - Comprehensive guide to the workflow and best practices

- [The Pragmatic Engineer: Stacked Diffs](https://newsletter.pragmaticengineer.com/p/stacked-diffs) - Industry analysis and adoption patterns (paywalled)

## Why "Maiao"?

As Maiao encourages users to create smaller and nicer commits in their pull requests, it has been given the name of a tiny island:

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](https://github.com/runetes/maiao/blob/main/CONTRIBUTING.md) for details.

## License

MIT License - see [DISCLAIMER.md](https://github.com/runetes/maiao/blob/main/DISCLAIMER.md) for details.

## About

Seamless GitHub PR management from the command-line

### Resources

[Readme](https://github.com/runetes/maiao#readme-ov-file)[License](https://github.com/runetes/maiao#License-1-ov-file)

### Contributing

[Contributing](https://github.com/runetes/maiao#contributing-ov-file)[Activity](https://github.com/runetes/maiao/activity)[Custom properties](https://github.com/runetes/maiao/custom-properties)

### Stars

167 stars

### Watchers

1 watching

### Forks

[2 forks](https://github.com/runetes/maiao/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Frunetes%2Fmaiao&report=runetes+%28user%29)

## Releases

## Packages

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
