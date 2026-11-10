---
title: "8389219: Implement JEP 401: Value Objects (Preview) by MrSimms · Pull Request #31120 · openjdk/jdk · GitHub"
url: https://github.com/openjdk/jdk/pull/31120
clipped: 2026-08-31 12:26:43
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [8389219: Implement JEP 401: Value Objects (Preview) by MrSimms · Pull Request #31120 · openjdk/jdk · GitHub](https://github.com/openjdk/jdk/pull/31120)

## Full Article

[Skip to content](https://github.com/openjdk/jdk/pull/31120#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      
    

      
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

  

  

      

        
            
  
      
    
    
      [openjdk](https://github.com/openjdk)    
    /
    
      [jdk](https://github.com/openjdk/jdk)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fopenjdk%2Fjdk)    You must be signed in to change notification settings

  

  
- 
          [Fork
    6.4k](https://github.com/login?return_to=%2Fopenjdk%2Fjdk)
  

  
- 
        
        [Star
          23.3k](https://github.com/login?return_to=%2Fopenjdk%2Fjdk)
  

        
      

        

          

  
  

    
    

    
      

    

  
  
  

## Conversation

  
          
  

### 
    
      
          
      

      
            [MrSimms](https://github.com/MrSimms)
    

      

      

      commented

        [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#issue-4421432912)

      
  •

  
    
      
        
          edited by openjdk
          Bot
        
        
      
    
    
      
  
        
      Loading

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  
    
  

    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

  
  Member

        

    
  

          
        
  
  
    
      

This pull request implements the first [preview](https://openjdk.org/jeps/12) of [JEP 401: Value Objects (Preview)](https://openjdk.org/jeps/401). This pull request also includes the implementation of [JEP 539: Strict Field Initialization in the JVM (Preview)](https://openjdk.org/jeps/539). That work was implemented in the same code base because JEP 401 depends on strict field initialization.

Sub-reviews, for spreading review debates are here:

- [JDK-8317277](https://bugs.openjdk.org/browse/JDK-8317277): Java language implementation of value objects

- [8317277: Java language implementation of value objects #31121](https://github.com/openjdk/jdk/pull/31121)

- [JDK-8317278](https://bugs.openjdk.org/browse/JDK-8317278): JVM implementation of value objects

- [8317278: JVM implementation of value objects #31122](https://github.com/openjdk/jdk/pull/31122)

- [JDK-8317279](https://bugs.openjdk.org/browse/JDK-8317279): Standard library implementation of value objects

- [8317279: Standard library implementation of value objects #31123](https://github.com/openjdk/jdk/pull/31123)

This is the "master pull request" for the initial preview of [JEP 401](https://openjdk.org/jeps/401). Comments and review for a change this large will not scale well in a single pull request. This pull request serves as the vehicle for sign-off and integration into  `` [jdk/master](https://github.com/openjdk/jdk). Review comments should be directed to the appropriate "sub-review pull request" listed above.

Note

The "sub-review pull requests" contain the same full set of code changes as this "master pull request" to preserve the full implementation context; the language compiler, JVM, and standard library changes are intertwined. The separate pull requests exist only to subdivide the review and related discussion by area.

Any resulting code changes should be made in  `` [valhalla/lworld](https://github.com/openjdk/valhalla/).

 `valhalla/lworld`  is currently updated from  `jdk/master`  whenever a weekly  `` [jdk tag](https://github.com/openjdk/jdk/tags) is created. At that time, code changes from  `valhalla/lworld`  will be propagated to this pull request and to all sub-review pull requests.

Ultimately, review sign-off will be recorded on this "master pull request", and the "sub-review pull requests" will be closed without integration.

This pull request has a large surface area and frequently conflicts with  `jdk/master` . Refer to  `` [valhalla/lworld](https://github.com/openjdk/valhalla/) for the latest state of the project code, keeping in mind that it may lag several days behind  `jdk/master` . Both repositories may be needed as references during review.

-  I confirm that I make this contribution in accordance with the [OpenJDK Interim AI Policy](https://openjdk.org/legal/ai).

### Progress

-  Change must not contain extraneous whitespace

-  Commit message must refer to an issue

-  Change must be properly reviewed (2 reviews required, with at least 1 [Reviewer](https://openjdk.org/bylaws#reviewer), 1 [Author](https://openjdk.org/bylaws#author))

### Issues

- [JDK-8389219](https://bugs.openjdk.org/browse/JDK-8389219): Implement JEP 401: Value Objects (Preview) (Enhancement - P4)

- [JDK-8389220](https://bugs.openjdk.org/browse/JDK-8389220): Implement JEP 539: Strict Field Initialization in the JVM (Preview) (Enhancement - P4)

### Reviewers

- [Coleen Phillimore](https://openjdk.org/census#coleenp) ([@coleenp](https://github.com/coleenp) - Reviewer) Review applies to [620ec3d6](https://git.openjdk.org/jdk/pull/31120/files/620ec3d6ce3c89369b467bd1759b316c291c655a)

- [Ioi Lam](https://openjdk.org/census#iklam) ([@iklam](https://github.com/iklam) - Reviewer) Review applies to [620ec3d6](https://git.openjdk.org/jdk/pull/31120/files/620ec3d6ce3c89369b467bd1759b316c291c655a)

- [Maurizio Cimadamore](https://openjdk.org/census#mcimadamore) ([@mcimadamore](https://github.com/mcimadamore) - Reviewer)

- [Jan Lahoda](https://openjdk.org/census#jlahoda) ([@lahodaj](https://github.com/lahodaj) - Reviewer) Review applies to [620ec3d6](https://git.openjdk.org/jdk/pull/31120/files/620ec3d6ce3c89369b467bd1759b316c291c655a)

- [Dean Long](https://openjdk.org/census#dlong) ([@dean-long](https://github.com/dean-long) - Reviewer) Review applies to [620ec3d6](https://git.openjdk.org/jdk/pull/31120/files/620ec3d6ce3c89369b467bd1759b316c291c655a)

- [Jaikiran Pai](https://openjdk.org/census#jpai) ([@jaikiran](https://github.com/jaikiran) - Reviewer) Review applies to [620ec3d6](https://git.openjdk.org/jdk/pull/31120/files/620ec3d6ce3c89369b467bd1759b316c291c655a)

- [Viktor Klang](https://openjdk.org/census#vklang) ([@viktorklang-ora](https://github.com/viktorklang-ora) - Reviewer) Review applies to [620ec3d6](https://git.openjdk.org/jdk/pull/31120/files/620ec3d6ce3c89369b467bd1759b316c291c655a)

- [Dan Heidinga](https://openjdk.org/census#heidinga) ([@DanHeidinga](https://github.com/DanHeidinga) - no project role) Review applies to [620ec3d6](https://git.openjdk.org/jdk/pull/31120/files/620ec3d6ce3c89369b467bd1759b316c291c655a)

- [Serguei Spitsyn](https://openjdk.org/census#sspitsyn) ([@sspitsyn](https://github.com/sspitsyn) - Reviewer) Review applies to [620ec3d6](https://git.openjdk.org/jdk/pull/31120/files/620ec3d6ce3c89369b467bd1759b316c291c655a)

- [Chris Plummer](https://openjdk.org/census#cjplummer) ([@plummercj](https://github.com/plummercj) - Reviewer) Review applies to [620ec3d6](https://git.openjdk.org/jdk/pull/31120/files/620ec3d6ce3c89369b467bd1759b316c291c655a)

- [Chen Liang](https://openjdk.org/census#liach) ([@liach](https://github.com/liach) - Reviewer)

- [Joe Darcy](https://openjdk.org/census#darcy) ([@jddarcy](https://github.com/jddarcy) - Reviewer)

- [Daniel D. Daugherty](https://openjdk.org/census#dcubed) ([@dcubed-ojdk](https://github.com/dcubed-ojdk) - Reviewer)

- [Axel Boldt-Christmas](https://openjdk.org/census#aboldtch) ([@xmas92](https://github.com/xmas92) - Reviewer)

### Contributors

- David Simms  `<dsimms@openjdk.org>` 

- Dan Smith  `<dlsmith@openjdk.org>` 

- Frederic Parain  `<fparain@openjdk.org>` 

- Tobias Hartmann  `<thartmann@openjdk.org>` 

- Roger Riggs  `<rriggs@openjdk.org>` 

- Vicente Romero  `<vromero@openjdk.org>` 

- Axel Boldt-Christmas  `<aboldtch@openjdk.org>` 

- Karen Kinnear  `<acorn@openjdk.org>` 

- Alex Menkov  `<amenkov@openjdk.org>` 

- Bill Huang  `<bhuang@openjdk.org>` 

- Benoît Maillard  `<bmaillard@openjdk.org>` 

- Christian Hagedorn  `<chagedorn@openjdk.org>` 

- Chris Plummer  `<cjplummer@openjdk.org>` 

- Casper Norrbin  `<cnorrbin@openjdk.org>` 

- Coleen Phillimore  `<coleenp@openjdk.org>` 

- David Beaumont  `<dbeaumont@openjdk.org>` 

- Daniel D. Daugherty  `<dcubed@openjdk.org>` 

- Damon Fenacci  `<dfenacci@openjdk.org>` 

- David Holmes  `<dholmes@openjdk.org>` 

- Dmitry Samersoff  `<dsamersoff@openjdk.org>` 

- Eric Caspole  `<ecaspole@openjdk.org>` 

- Evgeny Nikitin  `<enikitin@openjdk.org>` 

- Ekaterina Pavlova  `<epavlova@openjdk.org>` 

- Fei Yang  `<fyang@openjdk.org>` 

- Dan Heidinga  `<heidinga@openjdk.org>` 

- Harold Seigel  `<hseigel@openjdk.org>` 

- Ioi Lam  `<iklam@openjdk.org>` 

- Ivan Walulya  `<iwalulya@openjdk.org>` 

- Jatin Bhateja  `<jbhateja@openjdk.org>` 

- Jan Lahoda  `<jlahoda@openjdk.org>` 

- Jim Laskey  `<jlaskey@openjdk.org>` 

- John R Rose  `<jrose@openjdk.org>` 

- Joel Sikström  `<jsikstro@openjdk.org>` 

- Lois Foltan  `<lfoltan@openjdk.org>` 

- Chen Liang  `<liach@openjdk.org>` 

- Leonid Mesnik  `<lmesnik@openjdk.org>` 

- Matias Saavedra Silva  `<matsaave@openjdk.org>` 

- Marc Chevalier  `<mchevalier@openjdk.org>` 

- Mandy Chung  `<mchung@openjdk.org>` 

- Maurizio Cimadamore  `<mcimadamore@openjdk.org>` 

- Markus Grönlund  `<mgronlun@openjdk.org>` 

- Manuel Hässig  `<mhaessig@openjdk.org>` 

- Nick Gasson  `<ngasson@openjdk.org>` 

- Patricio Chilano Mateo  `<pchilanomate@openjdk.org>` 

- Paul Hübner  `<phubner@openjdk.org>` 

- Paul Sandoz  `<psandoz@openjdk.org>` 

- Quan Anh Mai  `<qamai@openjdk.org>` 

- Roberto Castañeda Lozano  `<rcastanedalo@openjdk.org>` 

- Roland Westrelin  `<roland@openjdk.org>` 

- Srikanth Adayapalam  `<sadayapalam@openjdk.org>` 

- Aleksey Shipilev  `<shade@openjdk.org>` 

- Stefan Johansson  `<sjohanss@openjdk.org>` 

- Sergey Kuksenko  `<skuksenko@openjdk.org>` 

- Serguei Spitsyn  `<sspitsyn@openjdk.org>` 

- Stefan Karlsson  `<stefank@openjdk.org>` 

- Thomas Stuefe  `<stuefe@openjdk.org>` 

- Thomas Schatzl  `<tschatzl@openjdk.org>` 

- Zoltan Majo  `<zmajo@openjdk.org>` 

- Alan Bateman  `<alanb@openjdk.org>` 

- Jaikiran Pai  `<jpai@openjdk.org>` 

- Martin Doerr  `<mdoerr@openjdk.org>` 

- Richard Reingruber  `<rrich@openjdk.org>` 

- Feilong Jiang  `<fjiang@openjdk.org>` 

- Daisuke Yamazaki  `<dyama@openjdk.org>` 

### Reviewing

Using  `git` 

Checkout this PR locally: 
 `$ git fetch https://git.openjdk.org/jdk.git pull/31120/head:pull/31120`  
 `$ git checkout pull/31120` 

Update a local copy of the PR: 
 `$ git checkout pull/31120`  
 `$ git pull https://git.openjdk.org/jdk.git pull/31120/head` 

Using Skara CLI tools

Checkout this PR locally: 
 `$ git pr checkout 31120` 

View PR using the GUI difftool: 
 `$ git pr show -t 31120` 

Using diff file

Download this PR as a diff file: 
[https://git.openjdk.org/jdk/pull/31120.diff](https://git.openjdk.org/jdk/pull/31120.diff)

Using Webrev

[Link to Webrev Comment](https://git.openjdk.org/jdk/pull/31120#issuecomment-4501491943)

    
  
  

      

          
          
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

                    
          
  
    
    
              👍
            21
  ExE-Boss, DenuxPlays, hatahet, Ducius6, TomBeckett, lyubomyr-shaydariv, sureshg, TheBrokenRail, 7mochi, ashm-dev, and 11 more reacted with thumbs up emoji
              🎉
            112
  sideeffffect, Arraying, bluebear94, sureshg, literallyfiro, ShadelessFox, xGab0, jonmv, toinouH, masmc05, and 102 more reacted with hooray emoji
              ❤️
            31
  dzikoysk, jjank, Col-E, sidosera, ExE-Boss, bmscomp, DenuxPlays, Alathreon, wendigo, TomBeckett, and 21 more reacted with heart emoji
              🚀
            36
  sureshg, xGab0, jonmv, masmc05, Spasi, lbkulinski, dzikoysk, BruceCavill, AnemoFlower, Col-E, and 26 more reacted with rocket emoji
              👀
            31
  quat1024, TheDrOfDoctoring, masmc05, Kobzol, lbkulinski, dzikoysk, CallMeEchoCodes, Kilip1000, dongwq, sidosera, and 21 more reacted with eyes emoji
      
        
            
    All reactions
  

          
              
- 
                👍
                  21 reactions
              
              
- 
                🎉
                  112 reactions
              
              
- 
                ❤️
                  31 reactions
              
              
- 
                🚀
                  36 reactions
              
              
- 
                👀
                  31 reactions
              
          
        
      
    

        

  

    

      
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [MrSimms](https://github.com/MrSimms)
    

      

      

      commented

        [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-4421399519)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

  
  Member

        

  Author

    
  

      

        

  
    
      
          

/issue add 8317277, 8317278, 8317279

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

      
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [bridgekeeper](https://github.com/apps/bridgekeeper)
    Bot

      

      

      commented

        [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-4421406667)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

👋 Welcome back dsimms! A progress list of the required criteria for merging this PR into  `master`  will be added to the body of your pull request. There are additional [pull request commands](https://wiki.openjdk.java.net/display/SKARA/Pull+Request+Commands) available for use with this pull request.

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

      
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-4421422445)

      
  •

  
    
      
        
          edited
          
        
        
      
    
    
      
  
        
      Loading

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  
    
  

    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

[@MrSimms](https://github.com/MrSimms) This change now passes all automated pre-integration checks.

ℹ️ This project also has non-automated pre-integration requirements. Please see the file [CONTRIBUTING.md](https://github.com/openjdk/jdk/blob/master/CONTRIBUTING.md) for details.

After integration, the commit message for the final commit will be:
 ` `8389219: Implement JEP 401: Value Objects (Preview)
8389220: Implement JEP 539: Strict Field Initialization in the JVM (Preview)

Co-authored-by: David Simms <dsimms@openjdk.org>
Co-authored-by: Dan Smith <dlsmith@openjdk.org>
Co-authored-by: Frederic Parain <fparain@openjdk.org>
Co-authored-by: Tobias Hartmann <thartmann@openjdk.org>
Co-authored-by: Roger Riggs <rriggs@openjdk.org>
Co-authored-by: Vicente Romero <vromero@openjdk.org>
Co-authored-by: Axel Boldt-Christmas <aboldtch@openjdk.org>
Co-authored-by: Karen Kinnear <acorn@openjdk.org>
Co-authored-by: Alex Menkov <amenkov@openjdk.org>
Co-authored-by: Bill Huang <bhuang@openjdk.org>
Co-authored-by: Benoît Maillard <bmaillard@openjdk.org>
Co-authored-by: Christian Hagedorn <chagedorn@openjdk.org>
Co-authored-by: Chris Plummer <cjplummer@openjdk.org>
Co-authored-by: Casper Norrbin <cnorrbin@openjdk.org>
Co-authored-by: Coleen Phillimore <coleenp@openjdk.org>
Co-authored-by: David Beaumont <dbeaumont@openjdk.org>
Co-authored-by: Daniel D. Daugherty <dcubed@openjdk.org>
Co-authored-by: Damon Fenacci <dfenacci@openjdk.org>
Co-authored-by: David Holmes <dholmes@openjdk.org>
Co-authored-by: Dmitry Samersoff <dsamersoff@openjdk.org>
Co-authored-by: Eric Caspole <ecaspole@openjdk.org>
Co-authored-by: Evgeny Nikitin <enikitin@openjdk.org>
Co-authored-by: Ekaterina Pavlova <epavlova@openjdk.org>
Co-authored-by: Fei Yang <fyang@openjdk.org>
Co-authored-by: Dan Heidinga <heidinga@openjdk.org>
Co-authored-by: Harold Seigel <hseigel@openjdk.org>
Co-authored-by: Ioi Lam <iklam@openjdk.org>
Co-authored-by: Ivan Walulya <iwalulya@openjdk.org>
Co-authored-by: Jatin Bhateja <jbhateja@openjdk.org>
Co-authored-by: Jan Lahoda <jlahoda@openjdk.org>
Co-authored-by: Jim Laskey <jlaskey@openjdk.org>
Co-authored-by: John R Rose <jrose@openjdk.org>
Co-authored-by: Joel Sikström <jsikstro@openjdk.org>
Co-authored-by: Lois Foltan <lfoltan@openjdk.org>
Co-authored-by: Chen Liang <liach@openjdk.org>
Co-authored-by: Leonid Mesnik <lmesnik@openjdk.org>
Co-authored-by: Matias Saavedra Silva <matsaave@openjdk.org>
Co-authored-by: Marc Chevalier <mchevalier@openjdk.org>
Co-authored-by: Mandy Chung <mchung@openjdk.org>
Co-authored-by: Maurizio Cimadamore <mcimadamore@openjdk.org>
Co-authored-by: Markus Grönlund <mgronlun@openjdk.org>
Co-authored-by: Manuel Hässig <mhaessig@openjdk.org>
Co-authored-by: Nick Gasson <ngasson@openjdk.org>
Co-authored-by: Patricio Chilano Mateo <pchilanomate@openjdk.org>
Co-authored-by: Paul Hübner <phubner@openjdk.org>
Co-authored-by: Paul Sandoz <psandoz@openjdk.org>
Co-authored-by: Quan Anh Mai <qamai@openjdk.org>
Co-authored-by: Roberto Castañeda Lozano <rcastanedalo@openjdk.org>
Co-authored-by: Roland Westrelin <roland@openjdk.org>
Co-authored-by: Srikanth Adayapalam <sadayapalam@openjdk.org>
Co-authored-by: Aleksey Shipilev <shade@openjdk.org>
Co-authored-by: Stefan Johansson <sjohanss@openjdk.org>
Co-authored-by: Sergey Kuksenko <skuksenko@openjdk.org>
Co-authored-by: Serguei Spitsyn <sspitsyn@openjdk.org>
Co-authored-by: Stefan Karlsson <stefank@openjdk.org>
Co-authored-by: Thomas Stuefe <stuefe@openjdk.org>
Co-authored-by: Thomas Schatzl <tschatzl@openjdk.org>
Co-authored-by: Zoltan Majo <zmajo@openjdk.org>
Co-authored-by: Alan Bateman <alanb@openjdk.org>
Co-authored-by: Jaikiran Pai <jpai@openjdk.org>
Co-authored-by: Martin Doerr <mdoerr@openjdk.org>
Co-authored-by: Richard Reingruber <rrich@openjdk.org>
Co-authored-by: Feilong Jiang <fjiang@openjdk.org>
Co-authored-by: Daisuke Yamazaki <dyama@openjdk.org>
Reviewed-by: mcimadamore, liach, darcy, dcubed, aboldtch, coleenp, iklam, jlahoda, dlong, jpai, vklang, heidinga, sspitsyn, cjplummer
` ` 

You can use [pull request commands](https://wiki.openjdk.org/display/SKARA/Pull+Request+Commands) such as [/summary](https://wiki.openjdk.org/display/SKARA/Pull+Request+Commands#PullRequestCommands-/summary), [/contributor](https://wiki.openjdk.org/display/SKARA/Pull+Request+Commands#PullRequestCommands-/contributor) and [/issue](https://wiki.openjdk.org/display/SKARA/Pull+Request+Commands#PullRequestCommands-/issue) to adjust it as needed.

At the time when this comment was updated there had been no new commits pushed to the  `master`  branch. If another commit should be pushed before you perform the  `/integrate`  command, your PR will be automatically rebased. If you prefer to avoid any potential automatic rebasing, please check the documentation for the [/integrate](https://wiki.openjdk.org/display/SKARA/Pull+Request+Commands#PullRequestCommands-/integrate) command for further details.

As you do not have [Committer](https://openjdk.org/bylaws#committer) status in [this project](https://openjdk.org/census#jdk) an existing Committer must agree to [sponsor](https://openjdk.org/sponsor/) your change. Possible candidates are the reviewers of this PR ([@coleenp](https://github.com/coleenp), [@iklam](https://github.com/iklam), [@mcimadamore](https://github.com/mcimadamore), [@lahodaj](https://github.com/lahodaj), [@dean-long](https://github.com/dean-long), [@jaikiran](https://github.com/jaikiran), [@viktorklang-ora](https://github.com/viktorklang-ora), [@sspitsyn](https://github.com/sspitsyn), [@plummercj](https://github.com/plummercj), [@liach](https://github.com/liach), [@jddarcy](https://github.com/jddarcy), [@dcubed-ojdk](https://github.com/dcubed-ojdk), [@xmas92](https://github.com/xmas92)) but any other Committer may sponsor as well.

➡️ To flag this PR as ready for integration with the above commit message, type  `/integrate`  in a new comment. (Afterwards, your sponsor types  `/sponsor`  in a new comment to perform the integration).

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

      
  
          
  
    
  

  
      

    
[MrSimms](https://github.com/MrSimms)

    mentioned this pull request
    [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#ref-pullrequest-4421526823)

  
    [8317277: Java language implementation of value objects
      #31121](https://github.com/openjdk/jdk/pull/31121)  

  
      
   Closed

  

  
  
      
        
      
      

  

    5 tasks
  

  

      
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-4421543945)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

[@MrSimms](https://github.com/MrSimms) this pull request can not be integrated into  `master`  due to one or more merge conflicts. To resolve these merge conflicts and update this pull request you can run the following commands in the local repository for your personal fork:
 `git checkout 8317277
git fetch https://git.openjdk.org/jdk.git master
git merge FETCH_HEAD
# resolve conflicts and follow the instructions given by git merge
git commit -m "Merge master"
git push` 

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

      
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-4421546179)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

⚠️  [@MrSimms](https://github.com/MrSimms) This pull request contains merges that bring in commits not present in the target repository. Since this is not a "merge style" pull request, these changes will be squashed when this pull request in integrated. If this is your intention, then please ignore this message. If you want to preserve the commit structure, you must change the title of this pull request to  `Merge <project>:<branch>`  where  `<project>`  is the name of another project in the [OpenJDK organization](https://github.com/openjdk) (for example  `Merge jdk:master` ).

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

      
  
            
    
      
    
    

      

          
[openjdk](https://github.com/apps/openjdk)
Bot

            added
      [csr](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Acsr)
  Pull request needs approved CSR before integration

      [merge-conflict](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Amerge-conflict)
  Pull request has merge conflict with target branch

  labels

      [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#event-25386043494)

    
  

      
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-4421550250)

      
  •

  
    
      
        
          edited
          
        
        
      
    
    
      
  
        
      Loading

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  
    
  

    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

[@MrSimms](https://github.com/MrSimms) This issue is referenced in the PR title - it will now be updated.

Adding additional issue to issue list:  `8317278: JVM implementation of value classes and objects` .

Adding additional issue to issue list:  `8317279: Standard library implementation of value classes and objects` .

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

      
  
          
  
    
  

  
      

  This was referenced May 11, 2026

  
    [8317278: JVM implementation of value objects
      #31122](https://github.com/openjdk/jdk/pull/31122)  

  
      
   Closed

  

      

  
    [8317279: Standard library implementation of value objects
      #31123](https://github.com/openjdk/jdk/pull/31123)  

  
      
   Closed

  

  

    
    
      
    
    

      

          
[openjdk](https://github.com/apps/openjdk)
Bot

            added
      [serviceability](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Aserviceability)
  serviceability-dev@openjdk.org

      [hotspot](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Ahotspot)
  hotspot-dev@openjdk.org

      [i18n](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Ai18n)
  i18n-dev@openjdk.org

      [shenandoah](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Ashenandoah)
  shenandoah-dev@openjdk.org

      [javadoc](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Ajavadoc)
  javadoc-dev@openjdk.org

      [security](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Asecurity)
  security-dev@openjdk.org

      [build](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Abuild)
  build-dev@openjdk.org

      [nio](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Anio)
  nio-dev@openjdk.org

      [core-libs](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Acore-libs)
  core-libs-dev@openjdk.org

      [compiler](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Acompiler)
  compiler-dev@openjdk.org

      [net](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Anet)
  net-dev@openjdk.org

  labels

      [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#event-25386520020)

    
  

      
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-4421643216)

      
  •

  
    
      
        
          edited
          
        
        
      
    
    
      
  
        
      Loading

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  
    
  

    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

[@MrSimms](https://github.com/MrSimms) The following labels will be automatically applied to this pull request:

-  `build` 

-  `compiler` 

-  `core-libs` 

-  `hotspot` 

-  `i18n` 

-  `javadoc` 

-  `net` 

-  `nio` 

-  `security` 

-  `serviceability` 

-  `shenandoah` 

When this pull request is ready to be reviewed, an "RFR" email will be sent to the corresponding mailing lists. If you would like to change these labels, use the [/label](https://wiki.openjdk.org/display/SKARA/Pull+Request+Commands#PullRequestCommands-/label) pull request command.

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

      
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [May 11, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-4421644276)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

The total number of required reviews for this PR has been set to 2 based on the presence of this label:  `hotspot` . This can be overridden with the  `/reviewers`  command.

      
    
  

        
            

            
              
  
    
      
    
              👀
            1
  bredouane-tmsw reacted with eyes emoji
      
        
            
    All reactions
  

          
              
- 
                👀
                  1 reaction
              
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

      
  
        
    
  
  
            Dan Smith
and others
        added 6 commits
        [May 12, 2026 14:56](https://github.com/openjdk/jdk/pull/31120#commits-pushed-873f02d)
  
      
  
  
            
  
    
      

  
        
  

      
         `
          [8383755: [lworld] Clean up Class.isValue and Class.isIdentity](https://github.com/openjdk/jdk/pull/31120/commits/873f02d2d521108f8883341350315991b592e733)
        ` 

          
                  …
          
      

      
        

    
    
    

  

      

      
        
          

    
    
    

  

  
    
  

        
      

      
         `
          [873f02d](https://github.com/openjdk/jdk/pull/31120/commits/873f02d2d521108f8883341350315991b592e733)
        ` 
      
    
  
    
       `Reviewed-by: liach` 
    

      
  
  
            
  
    
      

  
          

      
         `
          [8384050: [lworld] Update JDWP and JDI specs for JEP 401](https://github.com/openjdk/jdk/pull/31120/commits/f39fa97e6905c6cad790b97aad663b6a4e2040a2)
        ` 

          
                  …
          
      

      
        

    
    
    

  

      

      
        
          

    
    
    

  

  
    
  

        
      

      
         `
          [f39fa97](https://github.com/openjdk/jdk/pull/31120/commits/f39fa97e6905c6cad790b97aad663b6a4e2040a2)
        ` 
      
    
  
    
       `Reviewed-by: dholmes, sspitsyn` 
    

      
  
  
            
  
    
      

  
          

      
         `
          [8384431: [lworld] Adjust tests affected by JDK-8370769](https://github.com/openjdk/jdk/pull/31120/commits/e51da80a65a3efa7ad890fda1847a924248efe0a)
        ` 

          
                  …
          
      

      
        

    
    
    

  

      

      
        
          

    
    
    

  

  
    
  

        
      

      
         `
          [e51da80](https://github.com/openjdk/jdk/pull/31120/commits/e51da80a65a3efa7ad890fda1847a924248efe0a)
        ` 
      
    
  
    
       `Reviewed-by: mchevalier` 
    

      
  
  
            
  
    
      

  
        
  

      
         `
          [8384489: [lworld] ProblemList serviceability/jvmti/valhalla/SampledOb…](https://github.com/openjdk/jdk/pull/31120/commits/2585704c4f92a2aefcad7d4496c439cd1577bff3)
        ` 

          
                  …
          
      

      
        

    
    
    

  

      

      
        
          

    
    
    

  

  
    
  

        
      

      
         `
          [2585704](https://github.com/openjdk/jdk/pull/31120/commits/2585704c4f92a2aefcad7d4496c439cd1577bff3)
        ` 
      
    
  
    
       `…jectAllocValue/SampledObjectAllocValue.java

Reviewed-by: fparain, cjplummer` 
    

      
  
  
            
  
    
      

  
          

      
         `
          [8384487: [lworld] Fix minor typos in JDWP and JDI specs for JEP 401](https://github.com/openjdk/jdk/pull/31120/commits/96a8b4b55e7db45b9f15ab7e489fad53a665d7a2)
        ` 

          
                  …
          
      

      
        

    
    
    

  

      

      
        
          

    
    
    

  

  
    
  

        
      

      
         `
          [96a8b4b](https://github.com/openjdk/jdk/pull/31120/commits/96a8b4b55e7db45b9f15ab7e489fad53a665d7a2)
        ` 
      
    
  
    
       `Reviewed-by: sspitsyn` 
    

      
  
  
            
  
    
      

  
          

      
         `
          [8382504](https://github.com/MrSimms/jdk/commit/838250410ff378df568d090f7f2561ed25713c69)[: [lworld] TestIntrinsics.java triggers assert "must not cast …](https://github.com/openjdk/jdk/pull/31120/commits/4990f91ac2a698bded2313caf792b64202cd35ed)
        ` 

          
                  …
          
      

      
        

    
    
    

  

      

      
        
          

    
    
    

  

  
    
  

        
      

      
         `
          [4990f91](https://github.com/openjdk/jdk/pull/31120/commits/4990f91ac2a698bded2313caf792b64202cd35ed)
        ` 
      
    
  
    
       `…to a different type"

Reviewed-by: mchevalier, qamai` 
    

  

  
    
      
        
          
            405 hidden items
          
          
            Load more…
          
        
      
   

        
  
        
  
        
  
  
              
              
                    [jddarcy](https://github.com/jddarcy)
    

              

              approved these changes

              
                  [Jul 30, 2026](https://github.com/openjdk/jdk/pull/31120#pullrequestreview-4824164171)
              
              
            

            

                [View reviewed changes](https://github.com/openjdk/jdk/pull/31120/files/58712b78775b7d9b0182af519c16e78af1065878)

            

      
  
  
  

  

        
  
        
  
        
  
  
              
              
                    [dcubed-ojdk](https://github.com/dcubed-ojdk)
    

              

              approved these changes

              
                  [Jul 30, 2026](https://github.com/openjdk/jdk/pull/31120#pullrequestreview-4824171684)
              
              
            

            

                [View reviewed changes](https://github.com/openjdk/jdk/pull/31120/files/58712b78775b7d9b0182af519c16e78af1065878)

            

          
  
  
                
                      
  

### 
    
      
          
      

      
            [dcubed-ojdk](https://github.com/dcubed-ojdk)
    

      

      

      left a comment

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

  
  Member

        

    
  

                  

                      
  
  
  
    
      
    

    

There was a problem hiding this comment.

  

 
  
    
      
    

    

### Choose a reason for hiding this comment

    

      The reason will be displayed to describe this comment to others. [Learn more](https://docs.github.com/articles/managing-disruptive-comments/#hiding-a-comment).
    

    
      
        
        Choose a reason
        
        Spam
Abuse
Off Topic
Outdated
Duplicate
Resolved
Low Quality
      
        
    Hide comment
  

  

  
    
      

Thumbs up.
      
    
  
  

                    
                  
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

                      
                    
  
    
    
              👍
            1
  liach reacted with thumbs up emoji
      
        
            
    All reactions
  

          
              
- 
                👍
                  1 reaction
              
          
        
      
    

                  

      
  
  
  

  

        
  
        
  
        
  
  
              
              
                    [xmas92](https://github.com/xmas92)
    

              

              approved these changes

              
                  [Jul 30, 2026](https://github.com/openjdk/jdk/pull/31120#pullrequestreview-4824175555)
              
              
            

            

                [View reviewed changes](https://github.com/openjdk/jdk/pull/31120/files/58712b78775b7d9b0182af519c16e78af1065878)

            

      
  
  
  

  

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [dcubed-ojdk](https://github.com/dcubed-ojdk)
    

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137537105)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

  
  Member

        

    
  

      

        

  
    
      
          

Waiting for "ready" to appear, the "/integrate auto" should process, then the "sponsor" flag will be added, then I can "/sponsor"...

      
    
  

        
            

            
              
  
    
      
    
              👍
            1
  liach reacted with thumbs up emoji
      
        
            
    All reactions
  

          
              
- 
                👍
                  1 reaction
              
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
            
    
      
    
    

      

          
[openjdk](https://github.com/apps/openjdk)
Bot

          added
  the [ready](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Aready)
  Pull request is ready to be integrated
 label

      [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#event-28751059463)

    
  

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137571349)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

/integrate

      
    
  

        
            

            
              
  
    
      
    
              ❤️
            2
  sureshg and woess reacted with heart emoji
              🚀
            3
  liach, sureshg, and woess reacted with rocket emoji
      
        
            
    All reactions
  

          
              
- 
                ❤️
                  2 reactions
              
              
- 
                🚀
                  3 reactions
              
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [dcubed-ojdk](https://github.com/dcubed-ojdk)
    

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137620575)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

  
  Member

        

    
  

      

        

  
    
      
          

What happens if I do this early:

/sponsor

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
            
    
      
    
    

      

          
[openjdk](https://github.com/apps/openjdk)
Bot

          added
  the [sponsor](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Asponsor)
  Pull request is ready to be sponsored
 label

      [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#event-28751287741)

    
  

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137621096)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

[@openjdk](https://github.com/openjdk)[bot] 
Your change (at version [58712b7](https://github.com/openjdk/jdk/commit/58712b78775b7d9b0182af519c16e78af1065878)) is now ready to be sponsored by a Committer.

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [dcubed-ojdk](https://github.com/dcubed-ojdk)
    

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137623738)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

  
  Member

        

    
  

      

        

  
    
      
          

/sponsor

      
    
  

        
            

            
              
  
    
      
    
              🚀
            4
  liach, vidmik, lfoltan, and pengxiaolong reacted with rocket emoji
      
        
            
    All reactions
  

          
              
- 
                🚀
                  4 reactions
              
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [dcubed-ojdk](https://github.com/dcubed-ojdk)
    

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137626061)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

  
  Member

        

    
  

      

        

  
    
      
          

Just to get it in the right order... if that makes a difference...

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [dcubed-ojdk](https://github.com/dcubed-ojdk)
    

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137748100)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

  
  Member

        

    
  

      

        

  
    
      
          

tap, tap, tap... is this thing working?

      
    
  

        
            

            
              
  
    
      
    
              👍
            2
  liach and pengxiaolong reacted with thumbs up emoji
      
        
            
    All reactions
  

          
              
- 
                👍
                  2 reactions
              
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [dcubed-ojdk](https://github.com/dcubed-ojdk)
    

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137763729)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

  
  Member

        

    
  

      

        

  
    
      
          

Anyone? Anyone? Bueller? Bueller? Bueller?

      
    
  

        
            

            
              
  
    
      
    
              👍
            1
  liach reacted with thumbs up emoji
      
        
            
    All reactions
  

          
              
- 
                👍
                  1 reaction
              
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137845497)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

Going to push as commit [cc278db](https://github.com/openjdk/jdk/commit/cc278dbb8a1ca0754d5842708b9029441055d361).

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
            
    
      
    
    

      

          
[openjdk](https://github.com/apps/openjdk)
Bot

          added
  the [integrated](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Aintegrated)
  Pull request has been integrated
 label

      [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#event-28752098402)

    
  

    
    
      
    
    

      

          
[openjdk](https://github.com/apps/openjdk)
Bot

          closed this

      [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#event-28752099312)

    
  

    

    
    
      
    
    

      

          
[openjdk](https://github.com/apps/openjdk)
Bot

            removed
      [ready](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Aready)
  Pull request is ready to be integrated

      [rfr](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Arfr)
  Pull request is ready for review

      [sponsor](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Asponsor)
  Pull request is ready to be sponsored

  labels

      [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#event-28752099993)

    
  

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137847090)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

[@dcubed-ojdk](https://github.com/dcubed-ojdk) [@MrSimms](https://github.com/MrSimms) Pushed as commit [cc278db](https://github.com/openjdk/jdk/commit/cc278dbb8a1ca0754d5842708b9029441055d361).

💡 You may see a message that your pull request was closed with unmerged commits. This can be safely ignored.

      
    
  

        
            

            
              
  
    
      
    
              🎉
            27
  h-vetinari, liach, RogerRiggs, sureshg, shakuzen, TheShermanTanker, IMS212, mfiguiere, bahaa, gavlyukovskiy, and 17 more reacted with hooray emoji
              ❤️
            1
  ExE-Boss reacted with heart emoji
              🚀
            1
  ExE-Boss reacted with rocket emoji
      
        
            
    All reactions
  

          
              
- 
                🎉
                  27 reactions
              
              
- 
                ❤️
                  1 reaction
              
              
- 
                🚀
                  1 reaction
              
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
      

  
  

  

    
      
  

### 
    
      
          
      

      
            [openjdk](https://github.com/apps/openjdk)
    Bot

      

      

      commented

        [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#issuecomment-5137849390)

      
    

  

  
    
      
          
    
  

        
            
  
      
              Copy link

  
            
  
      
              Copy Markdown

  
        
      
    

    
        

        

    
  

      

        

  
    
      
          

[@dcubed-ojdk](https://github.com/dcubed-ojdk) The command  `sponsor`  can only be used in open pull requests.

      
    
  

        
            

            
              
  
    
      
    
      
        
            
    All reactions
  

          
          
        
      
    

            
        
      

      
            
  
  

    
  
  
  

    
    Sorry, something went wrong.
  

  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

        
  
          
  
    
  

  
      

    
[claude-yolo](https://github.com/apps/claude-yolo)
Bot

    mentioned this pull request
    [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#ref-issue-5028096482)

  
    [DeepSeek Pennies, Java Values, and Privacy Apps
      thevibeworks/claude-reads-hn#1450](https://github.com/thevibeworks/claude-reads-hn/issues/1450)  

  
      

  
  Closed

  

  

  
  
    
  

  
      

    
[Foxhunt](https://github.com/Foxhunt)

    mentioned this pull request
    [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#ref-issue-5028372767)

  
    [Daily Hacker News 31-07-2026
      Foxhunt/daily-hackernews#752](https://github.com/Foxhunt/daily-hackernews/issues/752)  

  
      

  
  Open

  

  

  
  
    
  

  
      

  This was referenced Jul 31, 2026

  
    [🌐 Global Tech Briefing - 2026-07-31
      AtomChen0425/Global_Trends#164](https://github.com/AtomChen0425/Global_Trends/issues/164)  

  
      

  
  Closed

  

      

  
    [每日速递 Daily Digest — 2026-07-31
      Aurora-yang-git/workflow#63](https://github.com/Aurora-yang-git/workflow/issues/63)  

  
      

  
  Open

  

  

  
  
    
  

  
      

    
[blka](https://github.com/blka)

    mentioned this pull request
    [Jul 31, 2026](https://github.com/openjdk/jdk/pull/31120#ref-issue-5029157662)

  
    [Daily Hacker News 31/07/2026
      blka/daily-hackernews#495](https://github.com/blka/daily-hackernews/issues/495)  

  
      

  
  Open

  

  

  
  
    
  

  
      

    
[headllines](https://github.com/apps/headllines)
Bot

    mentioned this pull request
    [Aug 1, 2026](https://github.com/openjdk/jdk/pull/31120#ref-issue-5034679515)

  
    [Hacker News Daily Top 10 @2026-08-01
      headllines/hackernews-daily#2214](https://github.com/headllines/hackernews-daily/issues/2214)  

  
      

  
  Open

  

  

  
  
    
  

  
      

    
[hacknews-bot](https://github.com/apps/hacknews-bot)
Bot

    mentioned this pull request
    [Aug 1, 2026](https://github.com/openjdk/jdk/pull/31120#ref-issue-5034783701)

  
    [Hacker News Daily Top 10 2026-08-01
      luoyunchong/actions#783](https://github.com/luoyunchong/actions/issues/783)  

  
      

  
  Open

  

  

  
  
    
  

  
      

    
[github-actions](https://github.com/apps/github-actions)
Bot

    mentioned this pull request
    [Aug 1, 2026](https://github.com/openjdk/jdk/pull/31120#ref-issue-5034930596)

  
    [[2026-07-31] UEFA and its national associations will not participate in FIFA competitions
      jiacai2050/mofish#1527](https://github.com/jiacai2050/mofish/issues/1527)  

  
      

  
  Open

  

  

  
  
    
  

  
      

    
[lgxbslgx](https://github.com/lgxbslgx)

    mentioned this pull request
    [Aug 18, 2026](https://github.com/openjdk/jdk/pull/31120#ref-pullrequest-5179162860)

  
    [8390501: Several JMH benchmarks fail with java.lang.UnsupportedClassVersionError
      #32413](https://github.com/openjdk/jdk/pull/32413)  

  
      
   Open

  

  
  
      
        
      
      

  

    4 tasks
  

  

  
  
    
      
  

  

  
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)
    

          [Show hidden characters](https://github.com/openjdk/jdk/pull/{{ revealButtonHref }})

  
    

  
      
  
    [Sign up for free](https://github.com/join?source=comment-repo)
    to join this conversation on GitHub.
    Already have an account?
    [Sign in to comment](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fopenjdk%2Fjdk%2Fpull%2F31120)

  

    
        
  
    
    
    

  

### 
    Reviewers
  

    

      
        
          17 more reviewers
          
          
        
          
            

  
    

    [borodulinartm](https://github.com/borodulinartm)

    
    borodulinartm left review comments

          
          
            

  
    

    [dfuch](https://github.com/dfuch)

    
    dfuch left review comments

          
          
            

  
    

    [mgronlun](https://github.com/mgronlun)

    
    mgronlun left review comments

          
          
            

  
    

    [lahodaj](https://github.com/lahodaj)

    
    lahodaj approved these changes

          
          
            

  
    

    [plummercj](https://github.com/plummercj)

    
    plummercj approved these changes

          
          
            

  
    

    [dean-long](https://github.com/dean-long)

    
    dean-long approved these changes

          
          
            

  
    

    [jddarcy](https://github.com/jddarcy)

    
    jddarcy approved these changes

          
          
            

  
    

    [iklam](https://github.com/iklam)

    
    iklam approved these changes

          
          
            

  
    

    [jaikiran](https://github.com/jaikiran)

    
    jaikiran approved these changes

          
          
            

  
    

    [liach](https://github.com/liach)

    
    liach approved these changes

          
          
            

  
    

    [DanHeidinga](https://github.com/DanHeidinga)

    
    DanHeidinga approved these changes

          
          
            

  
    

    [sspitsyn](https://github.com/sspitsyn)

    
    sspitsyn approved these changes

          
          
            

  
    

    [mcimadamore](https://github.com/mcimadamore)

    
    mcimadamore approved these changes

          
          
            

  
    

    [coleenp](https://github.com/coleenp)

    
    coleenp approved these changes

          
          
            

  
    

    [dcubed-ojdk](https://github.com/dcubed-ojdk)

    
    dcubed-ojdk approved these changes

          
          
            

  
    

    [xmas92](https://github.com/xmas92)

    
    xmas92 approved these changes

          
          
            

  
    

    [viktorklang-ora](https://github.com/viktorklang-ora)

    
    viktorklang-ora approved these changes

          
      
      Reviewers whose approvals may not affect merge requirements

      

  
      
  

      
  

### 
    Assignees
  

        

    No one assigned

  
        

  

  

### 
    Labels
  

    
      [auto](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Aauto)
  Expect automatic integration when ready; no further action required
  [build](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Abuild)
  build-dev@openjdk.org
  [compiler](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Acompiler)
  compiler-dev@openjdk.org
  [core-libs](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Acore-libs)
  core-libs-dev@openjdk.org
  [hotspot](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Ahotspot)
  hotspot-dev@openjdk.org
  [hotspot-jfr](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Ahotspot-jfr)
  hotspot-jfr-dev@openjdk.org
  [i18n](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Ai18n)
  i18n-dev@openjdk.org
  [integrated](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Aintegrated)
  Pull request has been integrated
  [javadoc](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Ajavadoc)
  javadoc-dev@openjdk.org
  [net](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Anet)
  net-dev@openjdk.org
  [nio](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Anio)
  nio-dev@openjdk.org
  [security](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Asecurity)
  security-dev@openjdk.org
  [serviceability](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Aserviceability)
  serviceability-dev@openjdk.org
  [shenandoah](https://github.com/openjdk/jdk/issues?q=state%3Aopen%20label%3Ashenandoah)
  shenandoah-dev@openjdk.org

  
  
        

  
    
  

### 
    Milestone
  

      No milestone

    
      
          

  
    
      
        
          
  

### 
    Development
  

            

Successfully merging this pull request may close these issues.

  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

      
    
  

      

  
  
        
  
    

### 
      20 participants
    

    
                                                                                                                                                                    
  

  
  
  
  
  
  

Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
