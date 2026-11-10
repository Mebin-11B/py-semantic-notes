---
title: "Stacked pull requests are now in public preview - GitHub Changelog"
url: https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/
clipped: 2026-08-31 12:26:39
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Stacked pull requests are now in public preview - GitHub Changelog](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/)

## Full Article

[Back to changelog](https://github.blog/changelog/)
		
	

	
		
			
					
	
			
	
		
			
	
		
		
			
			
			
				

Stacked pull requests break large changes into small, reviewable pull requests. They’re an ordered series of pull requests that each represent focused layers of your change. With stacks, you can independently review and check each pull request, then merge everything together in one click. No more opening a single large pull request that takes forever to review, or splitting work across multiple branches you have to keep manually rebasing.

  “We’ve been using GitHub stacked PRs for Next.js for the past few months. It has helped us introduce smaller individual changes while shipping larger features, making it easier to review PRs. – Tim Neutkens, Next.js lead, Vercel”

With stacked pull requests, teams can:

- Keep large changes moving by reviewing short, narrowly scoped pull requests in parallel.

- Maintain quality across every layer by using focused pull request reviews alongside existing branch protections to protect  `main` .

- Merge one, some, or all by landing an entire stack altogether or individual layers one at a time.

And because stacked pull requests are built into GitHub, your existing reviews, checks, and merge requirements all work out of the box.

  “The new Github Stacked PRs preview is incredible. Landing 5 stacked PRs directly to a merge queue all at once! A+++! This removes so much friction (and the gh cli tools + agent skill help a ton)” – John Resig, creator, jQuery

## [Get started with the CLI extension](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/#get-started-with-the-cli-extension)

Install the CLI extension and create your first stack in under a minute:
 ` `gh extension install github/gh-stack
` ` 

## [Create stacks from your terminal or github.com](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/#create-stacks-from-your-terminal-or-github-com)

Work with stacks on github.com, the GitHub CLI, the GitHub mobile app, or with a coding agent such as GitHub Copilot using the gh-stack skill. Start with a branch and pull request for your first change. Then add branches and pull requests on top of it; each pull request targets the layer below it.

## [Review each layer independently](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/#review-each-layer-independently)

Open any pull request in the stack to review only the diff for that specific layer. Use the stack map at the top of the pull request to see how the change you’re reviewing fits into the larger work. You and your teammates can each review different layers in parallel without blocking further work.

  “AI has made TED’s developers dramatically more productive, but that created a new bottleneck: PRs were growing large enough that reviewers were struggling. Stacked PRs help to solve that. By breaking large changes into small, dependency-ordered pieces, review happens in smaller logical chunks – not just faster PR reviews, but more accurate ones. Stacked PRs tighten our feedback loop and help get stable code to ted.com faster.” – Andy Merryman, CTO, TED

## [Merge everything in a single click](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/#merge-everything-in-a-single-click)

Merge the latest ready pull request to land it and every unmerged layer below it in one single operation. To land part of a stack, merge one or more lower layers—the pull requests above it stay open and automatically rebase and retarget. Your existing branch protections and required checks still govern what reaches  `main` .

  “A big change used to mean one giant PR nobody wanted to review. Now it’s a stack of small ones reviewers can actually follow, and the whole stack merges in one shot. It stopped feeling like a tool on top of GitHub and started feeling like GitHub.” – Mayank Saini, connectivity engineer, WHOOP

## [Find out more and share your feedback](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/#find-out-more-and-share-your-feedback)

Stacked pull requests are rolling out in public preview to all repositories over the coming days. [Merge queue](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue?utm_source=changelog-merge-queue-docs&utm_medium=changelog&utm_campaign=stacked-prs-gtm-public-preview-2026) support for stacked pull requests is rolling out progressively over the coming weeks.

For more information, check out the [stacked pull requests documentation](https://gh.io/stacks?utm_source=changelog-stacked-pr-docs&utm_medium=changelog&utm_campaign=stacked-prs-gtm-public-preview-2026), and share your feedback with us in the [stacks discussion](https://gh.io/stacks-feedback?utm_source=changelog-pr-stacks-feedback&utm_medium=changelog&utm_campaign=stacked-prs-gtm-public-preview-2026).

			
			
				
			
		
			

		
	

	
		
			

## Related Posts

						
				
	
		
			

### 
				
	Aug.27				Improvement
							

			
				[Close all open contributions authored by a blocked user](https://github.blog/changelog/2026-08-27-close-all-open-contributions-authored-by-a-blocked-user)
				
	
		
									[collaboration tools](https://github.blog/changelog/2026/?label=collaboration-tools)
						

			
		
		
	

	
		
			

### 
				
	Aug.25				Improvement
							

			
				[Block users directly from security advisories](https://github.blog/changelog/2026-08-25-block-users-directly-from-security-advisories)
				
	
		
									[collaboration tools](https://github.blog/changelog/2026/?label=collaboration-tools)
						

			
		
		
	

	
		
			

### 
				
	Aug.21				Improvement
							

			
				[Better tools for managing blocked users](https://github.blog/changelog/2026-08-21-better-tools-for-managing-blocked-users)
				
	
		
									[collaboration tools](https://github.blog/changelog/2026/?label=collaboration-tools)
						

			
		
		
	

	
		
			

### 
				
	Aug.21				Release
							

			
				[The new GitHub Copilot experience in Slack](https://github.blog/changelog/2026-08-21-the-new-github-copilot-experience-in-slack)
				
	
		
								[collaboration tools](https://github.blog/changelog/2026/?label=collaboration-tools)
							[copilot](https://github.blog/changelog/2026/?label=copilot)
						
				...
				+1			
			

			
		
		
	

	
		
			

### 
				
	Aug.21				Release
							

			
				[Shared agentic work with GitHub Copilot in Microsoft Teams](https://github.blog/changelog/2026-08-21-shared-agentic-work-with-github-copilot-in-microsoft-teams)
				
	
		
								[collaboration tools](https://github.blog/changelog/2026/?label=collaboration-tools)
							[copilot](https://github.blog/changelog/2026/?label=copilot)
						
				...
				+1			
			

			
		
		
	

	
		
			

### 
				
	Aug.13				Improvement
							

			
				[Block users from comments in personal repositories](https://github.blog/changelog/2026-08-13-block-users-from-comments-in-personal-repositories)
				
	
		
									[collaboration tools](https://github.blog/changelog/2026/?label=collaboration-tools)
						

			
		
		
	

	
		
			

### 
				
	Aug.11				Release
							

			
				[GitHub Enterprise Server 3.22 release candidate](https://github.blog/changelog/2026-08-11-github-enterprise-server-3-22-release-candidate)
				
	
		
									[collaboration tools](https://github.blog/changelog/2026/?label=collaboration-tools)
						

			
		
		
	

	
		
			

### 
				
	Aug.10				Retired
							

			
				[Custom thread subscriptions are being deprecated](https://github.blog/changelog/2026-08-10-custom-thread-subscriptions-are-being-deprecated)
				
	
		
								[collaboration tools](https://github.blog/changelog/2026/?label=collaboration-tools)
							[community engagement](https://github.blog/changelog/2026/?label=community-engagement)
							[projects & issues](https://github.blog/changelog/2026/?label=projects-and-issues)
						
				...
				+2			
			

			
		
		
	

	
		
			

### 
				
	Aug.06				Improvement
							

			
				[Set pull request limits at the organization level](https://github.blog/changelog/2026-08-06-set-pull-request-limits-at-the-organization-level)
				
	
		
									[collaboration tools](https://github.blog/changelog/2026/?label=collaboration-tools)
						

			
		
		
	
			
								
	

	
		
			

## Subscribe to our developer newsletter

			

				Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.			

			

				
					
						Enter your email*
					

					
					

					
						Subscribe					
				

				

				By submitting, I agree to let GitHub and its affiliates use my information for personalized communications, targeted advertising, and campaign effectiveness. See the [GitHub Privacy Statement](https://github.com/site/privacy) for more details.				
			
		
	

	[Back to top](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/#start-of-content)
