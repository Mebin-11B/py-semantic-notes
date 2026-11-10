---
title: "GUIs should be fully keyboard-driven | Charalampos Kardaris"
url: https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html
clipped: 2026-08-31 12:26:37
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [GUIs should be fully keyboard-driven | Charalampos Kardaris](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html)

## Full Article

2026-08-28

on
[Charalampos Kardaris' blog](https://ckardaris.com/blog), view [comments](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html#comments)

      

  
    

This post has made it to the Hacker News front page.
See the [discussion](https://news.ycombinator.com/item?id=49479837).

Last week I came across a [post on Hacker
News](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/) that encouraged application
developers to stop making terminal user interfaces[1](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html#fn:1)
(a.k.a. TUIs) and instead focus on graphical user interfaces (a.k.a. GUIs).
The post reached the HN front page and sparked a lively debate in the
[comments](https://news.ycombinator.com/item?id=49384210) section.

I think there is merit in both sides of the debate.
On one hand, I understand the GUI-positive arguments of the post author.
In theory, the capabilities of GUI application frameworks are a superset of the capabilities of
their TUI counterparts, so they should be preferred.
On the other hand, as a heavy terminal user, I also greatly appreciate all TUIs that allow me to
“stay” in the terminal and fulfill all my needs.

But I want to oppose a recurring argument in favor of TUIs that in my opinion does not have a solid
foundation[2](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html#fn:2).
To paraphrase various commenters:

  

TUIs should be preferred because they are keyboard-driven.

While it’s true that if you randomly pick a GUI and a TUI application, the latter is more probable
to be fully keyboard-driven, this does not tip the scale in favor of developing TUIs over GUIs[3](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html#fn:3).
What it does is highlight the inadequacies of keyboard navigation in many GUI applications.

There is nothing preventing a GUI from being fully keyboard-driven[4](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html#fn:4) just like — or even better
than — a TUI.
In fact, many GUI framework application guidelines explicitly encourage GUI application developers
to provide support for keyboard-driven navigation that covers the whole functionality of the
application.

For example, the GNOME Human Interface Guidelines state that [just as it should be possible to perform every
action with a pointing device, every action should also be possible with the
keyboard](https://developer.gnome.org/hig/guidelines/keyboard.html#:~:text=Just%20as%20it%20should%20be%20possible%20to%20perform%20every%20action%20with%20a%20pointing%20device%2C%20every%20action%20should%20also%20be%20possible%20with%20the%20keyboard)
and that [it should be possible to move around and interact with every part of your user interface
using the
keyboard](https://developer.gnome.org/hig/guidelines/keyboard.html#:~:text=It%20should%20be%20possible%20to%20move%20around%20and%20interact%20with%20every%20part%20of%20your%20user%20interface%20using%20the%20keyboard).

This resonates with me as a user.
Being able to intuitively — and predictably — navigate around a GUI application with only my
keyboard gives me more incentive to choose it compared to its alternatives.

Knowing that, and when wearing my developer hat, I have to make sure that my
applications are keyboard-friendly.
For my first ever GUI application, [Klisi](https://gitlab.com/ckardaris/klisi), I invested some time
to implement keyboard shortcuts targeting the whole range of available actions.

Keyboard navigation is not that hard to achieve in most cases and results in an overall better user
experience.
It is not a matter of feasibility, but a matter of will on the application developer’s part.

The takeaway is simple.
Do not compromise on the user experience you provide with your application.
Strive to make it as intuitive as possible.
To that end, enabling full keyboard navigation should not be ignored.

  
    
- 
      

Or alternatively [text-based user
interfaces](https://en.wikipedia.org/wiki/Text-based_user_interface). [↩](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html#fnref:1)
    
    
- 
      

The original post author mentions this as well. [↩](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html#fnref:2)
    
    
- 
      

There are other more compelling arguments towards tipping that scale, for example ease of
portability. [↩](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html#fnref:3)
    
    
- 
      

Of course, the dexterity achieved via mouse is still preferred — or even required — for some
tasks. [↩](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html#fnref:4)
    
  

  
    Tags:
    
      [programming](https://ckardaris.com/blog/tags/programming)
    
  
  
  
    
     Comments:
     [feed](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis/comments.xml)
     
     

add comment

  
    Name or nickname
    
      The name will be linked to your email address.
      If you change your name, your old name will be replaced in all comments.
      All comment data will be automatically encrypted with the [public key](https://ckardaris.com/pgp-public-key.txt).
    
  
  
  

  
    Password
    
      The password is used to authenticate against your email address.
      The password is linked to your email address after your first comment.
      After the first comment, you have to keep using the same password.
      All comment data will be automatically encrypted with the [public key](https://ckardaris.com/pgp-public-key.txt).
      You may change or reset your password at the [account](https://ckardaris.com/blog/account) page.
    
  
  
  
  
    
    
  
  

  
    Comment
    
      The comment can be markdown text.
      All comment data will be automatically encrypted with the [public key](https://ckardaris.com/pgp-public-key.txt).
    
  
  
  

  send comment via email

  cancel

  
  

    
  
  
    
      No comments to show.
