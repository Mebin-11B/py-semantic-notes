---
title: "GitHub - mysk-research/loupe: A privacy-focused iOS app that raises awareness about what native apps can see · GitHub"
url: https://github.com/mysk-research/loupe
clipped: 2026-08-31 12:26:31
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [GitHub - mysk-research/loupe: A privacy-focused iOS app that raises awareness about what native apps can see · GitHub](https://github.com/mysk-research/loupe)

## Full Article

[Skip to content](https://github.com/mysk-research/loupe#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      
    

      
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

  

  

      

        
            
  
      
    
    
      [mysk-research](https://github.com/mysk-research)    
    /
    
      [loupe](https://github.com/mysk-research/loupe)
    

    Public
  

        

        
            
    
        
- 
          
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

        

      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fmysk-research%2Floupe)    You must be signed in to change notification settings

  

  
- 
          [Fork
    58](https://github.com/login?return_to=%2Fmysk-research%2Floupe)
  

  
- 
        
        [Star
          1.5k](https://github.com/login?return_to=%2Fmysk-research%2Floupe)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/mysk-research/loupe/branches)[Tags](https://github.com/mysk-research/loupe/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[4 Commits](https://github.com/mysk-research/loupe/commits/main/)4 Commits

## Folders and files

NameNameLast commit messageLast commit date[.github](https://github.com/mysk-research/loupe/tree/main/.github)[.github](https://github.com/mysk-research/loupe/tree/main/.github)  [app-store](https://github.com/mysk-research/loupe/tree/main/app-store)[app-store](https://github.com/mysk-research/loupe/tree/main/app-store)  [code](https://github.com/mysk-research/loupe/tree/main/code)[code](https://github.com/mysk-research/loupe/tree/main/code)  [docs/images](https://github.com/mysk-research/loupe/tree/main/docs/images)[docs/images](https://github.com/mysk-research/loupe/tree/main/docs/images)  [fastlane](https://github.com/mysk-research/loupe/tree/main/fastlane)[fastlane](https://github.com/mysk-research/loupe/tree/main/fastlane)  [.gitignore](https://github.com/mysk-research/loupe/blob/main/.gitignore)[.gitignore](https://github.com/mysk-research/loupe/blob/main/.gitignore)  [AGENTS.md](https://github.com/mysk-research/loupe/blob/main/AGENTS.md)[AGENTS.md](https://github.com/mysk-research/loupe/blob/main/AGENTS.md)  [Gemfile](https://github.com/mysk-research/loupe/blob/main/Gemfile)[Gemfile](https://github.com/mysk-research/loupe/blob/main/Gemfile)  [Gemfile.lock](https://github.com/mysk-research/loupe/blob/main/Gemfile.lock)[Gemfile.lock](https://github.com/mysk-research/loupe/blob/main/Gemfile.lock)  [LICENSE](https://github.com/mysk-research/loupe/blob/main/LICENSE)[LICENSE](https://github.com/mysk-research/loupe/blob/main/LICENSE)  [README.md](https://github.com/mysk-research/loupe/blob/main/README.md)[README.md](https://github.com/mysk-research/loupe/blob/main/README.md)  View all files

## Repository files navigation

  

# Loupe

Loupe is an iOS and iPadOS app that gives you a hands-on tour of the device fingerprinting surface. It reads real values from public iOS APIs, the same ones any third-party app can call, and shows them to you raw. The point is simple: see what your iPhone quietly exposes, and why each reading helps an app recognize you again.

Trackers don't need your name, email, or location to recognize you online. Each reading isn't necessarily unique on its own, but together they form a fingerprint that follows you across apps and websites.

  

  
  
  

## How signals are organized

Loupe groups every reading into three tiers, reflecting the cost of access:

- Passive — visible to any app with no prompt at all (locale, time zone, screen, battery, and more).

- Needs Permission — readings that trigger an iOS prompt (contacts, photos, location, calendars).

- Advanced — clever side-channel uses of public APIs, such as URL-scheme probing via  `canOpenURL`  and Keychain persistence across reinstalls.

## Privacy

Nothing Loupe reads leaves your device unless you explicitly export it. Values are shown raw, without aggregation or hashing. Nothing is uploaded, synced, or shared.

## A note on how this was built

Loupe was written almost entirely by AI coding tools.

## Building

You'll need Xcode 26 or newer.

- Open  `code/Loupe.xcodeproj` .

- Copy  `code/Config/Signing.local.xcconfig.example`  to  `code/Config/Signing.local.xcconfig`  and fill in your own  `DEVELOPMENT_TEAM`  and bundle identifiers. This file is gitignored and never published.

- Build and run on a device or simulator.

The project uses Xcode's buildable folders (folder references), so new Swift files are picked up automatically with no need to edit the project file.

### macOS

Loupe also builds for macOS. The Mac version is mostly complete, but a few things still need work before it's polished.

## Support the project

Loupe is free and open source. If it helped you see what apps can quietly learn about your device, the best way to support more work like this is to try [Psylo](https://apps.apple.com/app/psylo-private-browser-proxy/id6741358035), our privacy-first browser for iPhone and iPad. Psylo gives you proxy-backed browsing, isolated tabs, and anti-fingerprinting protections.

You can also read [why we built Psylo](https://mysk.blog/2025/06/17/introducing-psylo/).

## License

The source code is released under the [MIT License](https://github.com/mysk-research/loupe/blob/main/LICENSE).

The Loupe name and logo, the app icon, all other images and icons, and the design source files are © Mysk, all rights reserved, and are not covered by the MIT license.

## About

Loupe is made by Mysk.

- [Website](https://mysk.co)

- [Blog](https://mysk.blog)

- [X](https://x.com/mysk_co)

- [Mastodon](https://mastodon.social/@mysk)

## About

A privacy-focused iOS app that raises awareness about what native apps can see

### Resources

[Readme](https://github.com/mysk-research/loupe#readme-ov-file)[License](https://github.com/mysk-research/loupe#License-1-ov-file)[Activity](https://github.com/mysk-research/loupe/activity)[Custom properties](https://github.com/mysk-research/loupe/custom-properties)

### Stars

1.5k stars

### Watchers

4 watching

### Forks

[58 forks](https://github.com/mysk-research/loupe/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fmysk-research%2Floupe&report=mysk-research+%28user%29)

## Releases

## Sponsor this project

## Packages

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
