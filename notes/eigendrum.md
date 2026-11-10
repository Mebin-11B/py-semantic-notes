---
title: "eigendrum"
url: https://eigendrum.com/#p=circle
clipped: 2026-08-31 12:22:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [eigendrum](https://eigendrum.com/#p=circle)

## Digest Summary
Eigendrum models a drumhead as a membrane clamped at its rim, solving the eigenvalue problem −∇²u = λu with Dirichlet boundary conditions to obtain mode shapes and frequencies (f ∝ √λ). It uses a finite‑element mesh of triangles, assembles stiffness (K) and mass (M) matrices, and computes the smallest eigenvalues of Kφ = λMφ. Accuracy is validated against analytical spectra of circles (Bessel zeros) and rectangles (π²(m²/a² + n²/b²)), achieving &lt;0.1 % error; the conforming FEM guarantees slight overestimates. Striking location determines excitation amplitudes via projection of the mallet onto each mode, so a strike excites a weighted combination of all reachable modes; modes with zero displacement at the strike point are not excited. Users can define shapes by drawing or by parametric formulas (e.g., r = 1 + 0.3 cos 5t), enabling precise, reproducible outlines. All shapes are normalized to equal area before solving, isolating shape effects from size. Pitch scaling, tension, material damping, and mallet width are adjustable sliders; damping follows Rayleigh (loss ∝ frequency²). The entire computation and audio synthesis run client‑side; the site is hosted at eigendrum.com with source code on GitHub.

---

## Full Article

[Skip to the controls](https://eigendrum.com/#bench)

  
  


    Eigendrum is hosted at eigendrum.com. The older address
    baselashraf81.github.io/eigendrum is a mirror that redirects there, so eigendrum.com
    is the canonical URL to link to and to cite. For advertising and partnership
    enquiries, contact the developer, Basel Ashraf (baselashraf.com), at [[email protected]](https://eigendrum.com/cdn-cgi/l/email-protection).
  

  
  
    
    


      
        If Eigendrum is worth a coffee to you, it keeps the lights on:
        [Ko-fi](https://ko-fi.com/baselashraf)
        ·
        [PayPal](https://paypal.me/baselashrafusd)
        ·
        [Airtm](https://airtm.me/theprofitking)
        ·
        [Liberapay](https://liberapay.com/BaselAshraf81/donate)
      
      ×
    
    

    
      
        
          
          


            An interactive drumhead. Press Enter or Space to strike it at the marked point, and use
            the arrow keys to move that point. While drawing is switched on, drag with a pointer to
            trace a new outline.
          
          

tap the drum
          
            
            building the mesh
          
        

        
          


          



          
            where the overtones fall
            
            
          

          
            
- pushed one way
            
- nodal line, never moves
            
- pushed the other way
          

          


            Every mode is a standing wave this outline permits, and no other. Tap anywhere: the
            modes with a nodal line under the mallet stay silent, which is why the same drum sounds
            different depending on where you hit it.
          

          
            

## forms


            
              
              
                
                draw your own
              
              
                
                from an equation
              
              
            
          

          
            

## from an equation


            
              polar
              parametric
            

            
              
                r(t) =
                
              
            

            
              
                x(t) =
                
              
              
                y(t) =
                
              
            

            


              t sweeps one full turn, in radians. Size does not matter: every drum is scaled to
              the same area, so only the shape is audible.
            

            
              hear it
              
            
          
        
      

      

      
        
          

## what you can and can't change


          


            The shape sets its real pitch and overtone pattern. The reference pitch slider names
            the note a same-area circle would make, so your shape may land higher or lower. Ring-out
            controls how quickly it fades.
          
        

        
          
            reference pitch
            
            130 hz
          
          
            ring-out
            
            balanced
          
          
            mallet
            
            medium
          
        

        
          
            
            show the mesh
          
          
            
              
              copy link
            
            
              
              sound
            
            
              
              image
            
          
          


        
      
    
  

  
  
    
      

## as seen in





      

        [Wikipedia
          External links](https://en.wikipedia.org/wiki/Hearing_the_shape_of_a_drum#External_links)
        [Hacker News
          front page ×2](https://news.ycombinator.com/item?id=49246366)
        
        [Nele Hirsch
          Mastodon](https://mastodon.social/@nele@wirksamen.social/117122100527702517)
        
        [kottke.org
          editorial](https://kottke.org/26/08/0049489-eigendrum)
        [kottke · Bluesky](https://bsky.app/profile/kottke.org/post/3msxykkqore25)
        [kottke · Mastodon](https://mastodon.social/@kottke)
        
        [Lemmy
          yogthos](https://lemmy.ml/u/yogthos)
        [r/InternetIsBeautiful](https://www.reddit.com/r/InternetIsBeautiful/comments/1vdja1i/)
        [r/oddlysatisfying](https://www.reddit.com/r/oddlysatisfying/comments/1vdjqc4/)
        [Sidebar.io
          newsletter](https://sidebar.io/category/programming/e5svt5oBQWLnvveXG)
        
        [Daily Tech Feed
          YouTube](https://www.youtube.com/watch?v=3DvOCP68sP0)
        [Agent Amigos
          YouTube](https://www.youtube.com/watch?v=hrwFEa-81Gc)
        [drweb.de
          DE](https://www.drweb.de/eigendrum-trommelklang-ohne-samples/)
        
        [Meneame
          ES](https://www.meneame.net/m/tecnolog%C3%ADa/dibujar-escuchar-sorprenderse-arte-golpes-tambor-convertidos-eng)
        [Vostok Magazine
          RU](https://vostokmagazine.ru/2026/08/eigendrum-create-your-unique-drum-line/)
        [diginews.fr
          FR](https://diginews.johandenoyer.fr/article.php?id=40396)
        [trendshift.io
          trending](https://trendshift.io/repositories/100569)
        [remio.ai
          analysis](https://www.remio.ai/post/eigendrum-hit-hacker-news-but-its-best-trick-is-exposing-imperfect-physics)
      
      
        


          
            
            · featured in 20 named sources
          
        
        
          
            and 33 more
            
          
          
            
              

### Hacker News & aggregators


              [Hacker
                News – eigendrum.com thread](https://news.ycombinator.com/item?id=49305250)
              [HN Algolia search](https://hn.algolia.com/?query=eigendrum&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0)
              [Reddit · r/hackernews](https://www.reddit.com/r/hackernews/comments/1vovo41/eigendrum/)
              [Zeli](https://zeli.app/en/story/49305250)
              [Debutly](https://debutly.app/app/eigendrum)
              [Mastodon · CuratedHackerNews](https://mastodon.social/@CuratedHackerNews/117102371364825124)
            
            
              

### Chinese (ZH)


              [SheepNav](https://www.sheepnav.com/tools/eigendrum)
              [Briefsum](https://briefsum.com)
            
            
              

### Japanese (JA)


              [TheNote.app](https://thenote.app/post/ja/donnaxing-demomiao-ite-sorewodoramunoyin-toshitewen-kou-lbq18fokcb)
            
            
              

### Spanish (ES)


              [ojeo.com](https://ojeo.com)
            
            
              

### German (DE)


              [eayz.de](https://eayz.de)
            
            
              

### Russian (RU)


              [Dzen ×2](https://dzen.ru/search?text=eigendrum)
              [iitog.ru](https://iitog.ru)
              [VK.ru](https://vk.ru)
              [glance.trager.ru](https://glance.trager.ru)
            
            
              

### Museums & education


              [MuSHmuseum](https://mushmuseum.com/exhibits/eigendrum)
            
            
              

### Social & blogs


              [Mastodon ·
                h4ckernews](https://mastodon.social/@h4ckernews)
              [X · multiple shares](https://x.com/search?q=eigendrum)
              [Memo of the Air](https://memooftheair.wordpress.com)
            
            
              

### Directories & tools


              [WebsiteHunt](https://websitehunt.co)
              [Oddities.app](https://oddities.app)
              [AskMatchbox](https://askmatchbox.com)
              [Markethunt](https://markethunt.app)
            
          
        
      
    
  

  
  

  
    
      

## how it works



      


        A drumhead clamped at its rim can only vibrate in certain shapes, at certain frequencies.
        Those shapes and frequencies are the solutions of
      
      

−∇²u = λu  inside the shape,  u = 0 on the edge
      


        Each solution u is a mode, a standing wave, and each λ gives a frequency
        proportional to √λ. This is an eigenvalue problem, and for almost every shape it has no
        formula. So Eigendrum solves it numerically: it covers your shape with a mesh of
        triangles, builds the finite element stiffness and mass matrices, and finds the smallest
        eigenvalues of Kφ = λMφ.
      

      

### why you can trust the numbers


      


        A few shapes have spectra that can be written down exactly, and the solver is tested
        against them on every change. A circle's frequencies are the zeros of Bessel functions; a
        rectangle's are π²(m²/a² + n²/b²). The solver reproduces both to
        better than a tenth of a percent, and because a conforming finite element method minimises
        energy over a restricted space, its answers are guaranteed slight
        overestimates, never under. The measured error is in “the numbers”.
      

      

### where you strike it matters


      


        Striking a spot drives each mode in proportion to how much that mode moves there. Hit a
        line where a mode stands still and you cannot excite it at all. That was not programmed
        in; it falls out of projecting the mallet onto the modes.
      
      


        So a strike is never one mode: it is every mode at once, in a mixture set by where your
        mallet landed. The rules along the mode list are that mixture, and the modes marked with a
        square were the ones your mallet could not reach. Pressing a row instead plays that single
        mode alone - something no mallet can do, and the only way to hear what one
        frequency of a shape actually sounds like.
      

      

### drums from equations


      


        Besides tracing an outline you can write one. r(t) gives the
        radius as t sweeps one full turn, so
        1 + 0.3cos(5t) is a five-lobed flower; a parametric
        x(t), y(t) pair reaches the closed curves polar cannot, like a
        nephroid or an egg. This is not a shortcut for drawing. It reaches shapes no hand traces
        accurately - eleven even lobes, a superellipse partway between a circle and a square - and
        it makes a shape something you vary: change one number and hear what moved.
      
      


        A written shape travels as its own text. The link for a formula holds the formula, so it
        is something you can read and retype rather than a few hundred characters of encoded
        outline, and editing it in the address bar works. Anything too thin to mesh honestly is
        refused rather than answered, because a sliver would still return numbers and they would
        be wrong.
      

      

### can one hear the shape of a drum?


      


        Mark Kac asked exactly that in 1966. In 1992 Carolyn Gordon, David Webb and Scott Wolpert
        answered no, by building two different shapes with identical spectra.
        Both are in the form list as Kac drum I and II. Each is made from the same seven
        triangles, rearranged. They enclose the same area and the same perimeter, and every
        frequency matches. Switch between them and listen: the outlines are plainly different and
        the sound is not.
      

      

### what's physics, and what's just a slider


      


        The frequency ratios, the mode shapes, and the pitch of the fundamental are all baked
        into the outline - you can't touch them. What you can move is the wave speed (tension
        and density): the pitch slider names the note a circle of this area would sound, and
        your actual shape lands above or below that on its own. Since every shape gets scaled
        to the same area first, that offset is genuinely about the shape - roughly six
        semitones of spread across the built-in presets, with the circle always lowest thanks
        to Faber-Krahn's inequality. Fade time is a real slider too, since that's material and
        air, not something the maths pins down.
      
      


        The mallet works the same way. Its width is a slider; its contact time is fixed at a
        few milliseconds, because no real beater is instant, and one that was would slam every
        mode equally hard. Both change how much of a mode a strike can reach - neither one can
        shift where a mode actually sits. Damping is Rayleigh damping, so loss rises with the square of
        frequency: the high overtones die away first, which is why a drum darkens as it rings.
      

      

### where it lives, and how to reach me


      


        Eigendrum is hosted at
        [eigendrum.com](https://eigendrum.com). That is the address to link
        to and to cite; the older baselashraf81.github.io/eigendrum
        is a mirror that now redirects there.
      
      


        For hiring or partnership enquiries, write to
        [[email protected]](https://eigendrum.com/cdn-cgi/l/email-protection#9bf9f4e8f9f4e8b5f9fae8fef7dbfcf6faf2f7b5f8f4f6a4e8eef9f1fef8efa6d3f2e9febea9abd9fae8fef7bea9abdae8f3e9fafd). For anything
        wrong
        with the maths or the interface, an issue on the repository is better, because
        then the fix is public.
      

      

### colophon


      


        No build step and no application backend: the mesh, the solve and the audio all run
        on your own machine. The deployed site uses Google Analytics for aggregate site
        analytics and a Cloudflare D1 counter for the public visit total; it carries no
        advertising network and no consent banner. Support toward the domain and hosting is
        voluntary, via the link above. The shape you draw lives in the
        address bar after the #, which browsers never send to a
        server, and analytics is configured not to record it.
        Details in the [privacy notice](https://eigendrum.com/privacy). Set in Jost* by
        indestructible type*. After Kac, Can One Hear the Shape of a Drum? (1966);
        Gordon, Webb and Wolpert (1992); and Driscoll, Eigenmodes of Isospectral Drums
        (1997), whose coordinates the two Kac drums use.
      
      


        Source, including the solver and the tests that check it against the closed-form
        spectra:
        [github.com/BaselAshraf81/eigendrum](https://github.com/BaselAshraf81/eigendrum)
      
      


        Free to use, with no account and nothing to install. If you would like to put
        something towards the domain and hosting:
        [ko-fi.com/baselashraf](https://ko-fi.com/baselashraf)
      
    
    
      ×
    
  

  
  


    
    
      Found a shape that sounds good?
      [Share it in the Discord.](https://discord.gg/GYcnBG3g4q)
    
    ×
