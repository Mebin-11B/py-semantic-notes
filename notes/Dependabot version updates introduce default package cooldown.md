---
title: "Dependabot version updates introduce default package cooldown"
url: https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/
clipped: 2026-08-31 12:22:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Dependabot version updates introduce default package cooldown](https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/)

## Digest Summary
Dependabot now imposes a default three‑day “cooldown” before creating version‑update pull requests. The delay applies only to regular version updates; security updates continue to be opened immediately. This measure aims to reduce the risk of supply‑chain attacks by allowing time for any issues with a new release to become apparent before the update is merged. Users can modify the behavior in .github/dependabot.yml via the cooldown option to set a different wait period or to disable the cooldown entirely. The default setting is active for all supported ecosystems on GitHub.com and will be enforced in GitHub Enterprise Server 3.23.

---

## Full Article

[Back to changelog](https://github.blog/changelog/)
		
	

	
		
			
					
	
			
	
		
				
		
		
			
			
			
				

Dependabot now waits until a new release has been available on its registry for at least three days before opening a version update pull request. This cooldown is now the default and requires no configuration.

New releases are a common entry point for supply chain attacks where a compromised or broken version can reach your dependency updates before maintainers and the community have caught it. A short delay gives that signal time to surface, so you are less likely to merge a bad release the moment it ships.

A few things to know:

- The default applies only to version updates. Security updates still open immediately, so critical fixes are never delayed.

- You stay in control. Use the  `cooldown`  option in your  `.github/dependabot.yml`  to set a different window or opt out entirely.

This default applies to Dependabot version updates across all supported ecosystems on github.com and will take effect in GitHub Enterprise Server (GHES) 3.23.

Learn more in [our docs about Dependabot cooldowns](https://docs.github.com/code-security/dependabot/working-with-dependabot/dependabot-options-reference#cooldown-).

			
			
							
		
			

		
	

	
		
			

## Related Posts

						
				
	
		
			

### 
				
	Aug.13				Improvement
							

			
				[License data quality improvements](https://github.blog/changelog/2026-08-13-license-data-quality-improvements)
				
	
		
									[supply chain security](https://github.blog/changelog/2026/?label=supply-chain-security)
						

			
		
		
	

	
		
			

### 
				
	Aug.04				Improvement
							

			
				[Customize Dependabot pull request branch names](https://github.blog/changelog/2026-08-04-customize-dependabot-pull-request-branch-names)
				
	
		
									[supply chain security](https://github.blog/changelog/2026/?label=supply-chain-security)
						

			
		
		
	

	
		
			

### 
				
	Jul.31				Retired
							

			
				[Restricting npm bypass-2FA granular access tokens](https://github.blog/changelog/2026-07-31-restricting-npm-bypass-2fa-granular-access-tokens)
				
	
		
									[supply chain security](https://github.blog/changelog/2026/?label=supply-chain-security)
						

			
		
		
	

	
		
			

### 
				
	Jul.28				Release
							

			
				[npm publish-time malware scanning and dual-use metadata](https://github.blog/changelog/2026-07-28-npm-publish-time-malware-scanning-and-dual-use-metadata)
				
	
		
									[supply chain security](https://github.blog/changelog/2026/?label=supply-chain-security)
						

			
		
		
	

	
		
			

### 
				
	Jul.28				Improvement
							

			
				[Dependabot alerts on malicious packages across more ecosystems](https://github.blog/changelog/2026-07-28-dependabot-alerts-on-malicious-packages-across-more-ecosystems)
				
	
		
									[supply chain security](https://github.blog/changelog/2026/?label=supply-chain-security)
						

			
		
		
	

	
		
			

### 
				
	Jul.28				Improvement
							

			
				[GitHub Actions holds potentially malicious workflows for approval](https://github.blog/changelog/2026-07-28-github-actions-holds-potentially-malicious-workflows-for-approval)
				
	
		
								[actions](https://github.blog/changelog/2026/?label=actions)
							[supply chain security](https://github.blog/changelog/2026/?label=supply-chain-security)
						
				...
				+1			
			

			
		
		
	

	
		
			

### 
				
	Jul.08				Release
							

			
				[Innersource security advisories are generally available](https://github.blog/changelog/2026-07-08-innersource-security-advisories-are-generally-available)
				
	
		
									[supply chain security](https://github.blog/changelog/2026/?label=supply-chain-security)
						

			
		
		
	

	
		
			

### 
				
	Jul.08				Retired
							

			
				[npm install-time security and GAT bypass2fa deprecation](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation)
				
	
		
									[supply chain security](https://github.blog/changelog/2026/?label=supply-chain-security)
						

			
		
		
	

	
		
			

### 
				
	Jun.30				Release
							

			
				[Open source license compliance is in public preview](https://github.blog/changelog/2026-06-30-open-source-license-compliance-is-in-public-preview)
				
	
		
									[supply chain security](https://github.blog/changelog/2026/?label=supply-chain-security)
						

			
		
		
	
			
								
	

	
		
			

## Subscribe to our developer newsletter

			

				Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.			

			

				
					
						Enter your email*
					

					
					

					
						Subscribe					
				

				

				By submitting, I agree to let GitHub and its affiliates use my information for personalized communications, targeted advertising, and campaign effectiveness. See the [GitHub Privacy Statement](https://github.com/site/privacy) for more details.				
			
		
	

	[Back to top](https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/#start-of-content)
