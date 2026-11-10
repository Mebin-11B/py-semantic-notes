---
title: "What to learn to be a graphics programmer"
url: https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/
clipped: 2026-08-31 12:22:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [What to learn to be a graphics programmer](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/)

## Digest Summary
- Real‑time graphics programming splits into CPU‑side engine work (DirectX 12, Vulkan, Metal, asset loading) and GPU‑side rendering (lighting, shading, shadows, AO, post‑process).  
- For GPU fundamentals start with a basic path tracer (e.g., *Ray Tracing in One Weekend*) and study Physically Based Rendering (PBR); resources include LearnOpenGL PBR tutorial, Google Filament docs, and the free PBRT book.  
- Demonstrate competence with a small engine‑like project in C++ that loads models/textures, renders them using PBR via DX12/Vulkan/Metal, includes a controllable camera and effects (shadows, tone mapping, etc.). Add a separate C++ path‑tracer, optionally integrated to validate real‑time results.  
- Required mathematics: linear algebra (matrices, dot/cross products), basic trigonometry, modest calculus. Core CS knowledge: arrays, linked lists, hash tables, sorting/searching; simple algorithms often outperform complex ones.  
- Primary language: C++; shader languages: HLSL (most common) or GLSL, often transpiled for cross‑platform builds. WebGPU exists but has limited job demand.  
- Machine‑learning knowledge is optional; useful for fitting/optimization but not essential for graphics programming.

---

## Full Article

I get asked fairly often what people need to know to be hireable as a graphics programmer. I figured it was time to make a page to link instead of re-typing it each time.

We are in a strange time with LLMs. I think ML as it is right now won’t live up to the hype, and the pendulum will swing away from ML a bit over the next couple years. I think the grifters will move onto quantum computing next or find some other thing to pump and dump. However, ML itself does have a place in the computer science tool box, so learning about the fitting and optimization techniques it offers is valuable IMO.  I made a video you can watch to learn about the bare metal bits, but it’s up to you if you think it’s worth while to learn or not.Machine Learning For Game Developers[https://www.youtube.com/watch?v=sTAqWRsEiy0](https://www.youtube.com/watch?v=sTAqWRsEiy0)

Besides that:

Modern rendering is sort of like two jobs in one.

- Learning the CPU side – Learning DirectX12, Vulkan, Metal, or similar modern “explicit” APIs and the engine programming to support loading assets and other supporting tasks.

- Learning the GPU side – the mathematics of modern lighting and shading, rendering techniques like shadows, ambient occlusion, and post processing effects. Also understanding what is fast and what is slow on the GPU, to know how to make things that run better in real time.

It’s very difficult to learn both things at once. If you want to focus on #2, then you could use a simpler thing for #1, such as opengl, webgl, DirectX11, an engine, or similar. If you want to focus on #1, you should work until you get a first triangle up on the screen, then get a mesh on screen, and so on, but don’t worry about it being very pretty.

Part of #2 is writing a path tracer.  Path tracing is how movies do rendering, and it is what we try to approximate with modern real time rendering techniques. A great place to start with a path tracer is this free book online “Ray Tracing in One Weekend”. A lot of people have used it. It’s really approachable and shows you how to make photo realistic renderings.[https://raytracing.github.io/books/RayTracingInOneWeekend.html](https://raytracing.github.io/books/RayTracingInOneWeekend.html)

Another part of #2 is learning “Physically based rendering” or PBR, which is a way of applying lighting (mainly specular, when it comes down to it). PBR is “principled,” meaning if you stick to the rules, you get good results.  Before PBR, people wrote random equations for lighting with all sorts of random tweaks and hacks. It made it so you could make an asset that looked good in one situation, but changing the lighting would make it look too dark or would look like it was glowing.  People had to make different versions of the assets for different lighting conditions, which was a lot of time and effort.PBR lets your assets look better in all lighting conditions by default, and saves the time and effort of having to make different versions.  It was a big win for our industry. Even so, asset creation time, money and effort is still a big bottleneck in game development.

The PBR section (and subsections) on this page are a great intro to PBR:[https://learnopengl.com/PBR/Theory](https://learnopengl.com/PBR/Theory)

If at some point you outgrow that and want to go deeper, reading the Filament documentation is a good next step. lots of calculus and statistics as you go deeper into PBR:[https://google.github.io/filament/Filament.md.html](https://google.github.io/filament/Filament.md.html)

Beyond that is the famous PBRT book “Physically Based Rendering: From Theory To Implementation” which is also free online:[https://pbrt.org/](https://pbrt.org/)

Ideally you’ll end up with some source code you can share with prospective employers (like on github, linked to on your resume) to show as proof that you know these things. Something like:

- Something that looks vaguely like an engine in that it loads assets (models, textures) and renders them on the screen in real time, with lighting and a couple effects (shadows, depth of field, area lights, tone mapping, ray traced shadows, whatever). Preferably lit using PBR, with a user controllable camera, and is written using DX12, vulkan or similar, and in C++.

- A path tracer that generates a photo realistic image.  Preferably in C++, but it could be a program without a window that just writes a png as output, it doesn’t have to be real time.

- Bonus points if the path tracer is just a separate mode of your “engine-like renderer” and you use it to help verify that your real time PBR rendering is correct, by showing that it matches path traced results. Extra bonus points if you point out where the two renderings don’t match, you can explain why they don’t match, and have thoughts on what you could implement in your real time renderer to make them match more closely while still staying real time.

You might wonder what math you need to know.  If you do the above items, you will encounter the math you need to know but basically linear algebra (matrix multiplication, cross product, dot product), basic trigonometry, and a little bit of calculus is really all you NEED.  The fun thing about graphics (and game development in general), is that while the amount of math you need is fairly minimal, the amount of math you can use is essentially unbounded.

The same is true algorithmically.  You should know the basic abstract data types and algorithms such as linked lists, hash tables, sorting and searching.  Often times, the fastest algorithms are the simplest.  An array is far faster than a linked list. However, knowing more advanced algorithmic concepts can help you when you really do need something novel and custom.

In game development, C++ is the language to learn. Some people use rust, and it’s hard to tell if rust use is growing or not, but it does have a slice of the pie, while not being the standard language that people expect you to know.  WebGPU has a lot of capabilities that WebGL did not have, and it’s becoming more of a serious platform, which lets you work in javascript to do the CPU side of the work.  I haven’t seen a lot of WebGPU jobs posted though, and I don’t see a lot of WebGPU content on the web. Knowing C++ seems to be the thing to learn, by far, for CPU side programming.

For shader languages, hlsl seems most common, but some people work in glsl.  The shaders are often transpiled to other shader languages in multi platform games.

You might wonder if you have to be good at art to be a graphics programmer. Luckily not. You’ll be collaborating with artists who are good at art, as well as technical artists, who sit between programmers and artists and help bridge the gap in understanding between the two disciplines.  That said, if you do know something about art, or photography, or similar, it does help.  Not required, though.

I’ll keep this page updated as things change or as people ask questions not covered here.

Extended ML Commentary Regarding Agents:I don’t believe current ML technology is “up to task” for most of the things they are selling it’s use on. I do get use out of it by talking to Claude about math, papers, or unfamiliar algorithms. It’s easy to see if it’s making things up or not in those situations, and it’s easy to check other sources for sanity checks. I do not find it very useful for programming however because even when it does what it’s supposed to do, I don’t understand the code without taking the time to understand it. At that point, I should have just written it. There are some smaller things I find useful, such as “do you see any bugs in this file?” which either returns yes and i can investigate, or returns no, and it cost me nothing to ask. These technical things aside, I do believe that at some point humanity will figure out how to make actual human level artificial intelligence and then go beyond that. I don’t know if that will happen in my lifetime, but I do believe it will happen some day, unless we destroy ourselves first. In that way, this age of LLMs is sort of like a dress rehearsal for when “the real stuff” comes later on. I hope we learn the right lessons and are more prepared when it comes.

### Share this:

- [Share on X (Opens in new window)
				X](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?share=twitter)
- [Share on Facebook (Opens in new window)
				Facebook](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?share=facebook)
- Like Loading...

	

### Related

			
	
		
		This entry was posted in [Uncategorized](https://blog.demofox.org/category/uncategorized/). Bookmark the [permalink](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/).	
	

					
	
				
	

			
		

## 
			9 comments		

		
		
				
- 
		

Pingback: [Guia Definitivo: Como se Tornar um Graphics Programmer - Big_SaaS](https://bigsaas.top/guia-definitivo-como-se-tornar-um-graphics-programmer/)
	
	
- 
		
			

			

Nice artile on the foundations of graphics. If you are wondering the relation between graphics and deeplearning, you may find these articles interesting.[https://arvinddevaraj.substack.com/p/how-the-gpu-works-the-graphics-pipeline](https://arvinddevaraj.substack.com/p/how-the-gpu-works-the-graphics-pipeline)[https://arvinddevaraj.substack.com/p/from-triangles-to-transformers-how](https://arvinddevaraj.substack.com/p/from-triangles-to-transformers-how)

[Like](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?like_comment=18948&_wpnonce=726530c06c)Like

			
				[Reply](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?replytocom=18948#respond)			
		

	
	
- 
		
			

			

+1 this is great, great intro for an intense but rewarding journey; i’ll be sending this to people who are curious!

[Like](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?like_comment=18949&_wpnonce=17cce2f2fd)Like

			
				[Reply](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?replytocom=18949#respond)			
		

	
	
- 
		
			

			

A very good article! I will show it to my friends asking the same question.

[Like](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?like_comment=18950&_wpnonce=634de3246d)Like

			
				[Reply](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?replytocom=18950#respond)			
		

	
	
- 
		
			

			

Thanks Adam!

[Like](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?like_comment=18951&_wpnonce=7ade39581b)Like

			
				[Reply](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?replytocom=18951#respond)			
		

	

	
- 
		
			

			

Hardest part for me to find roles, looks like there is almost no roles for graphics programmers in 2026, the ones I can find require a ton of professional experience (and it’s not easy to find these ones) not sure if I’m doing this wrong.

[Like](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?like_comment=18952&_wpnonce=b04eca6727)Liked by [1 person](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/#)

			
				[Reply](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?replytocom=18952#respond)			
		

	
	
- 
		
			

			

It isn’t just you, It took me 9 months of searching to find a new job. It’s really hard right now. I think in the next 12-24 months things will improve, but that’s not a short amount of time ):

[Like](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?like_comment=18954&_wpnonce=c9c4c55173)Liked by [1 person](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/#)

			
				[Reply](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?replytocom=18954#respond)			
		

	

	
- 
		
			

			

pretty sad  but thanks for the excellent article

[Like](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?like_comment=18955&_wpnonce=78545fa5e4)Like

			
				[Reply](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?replytocom=18955#respond)			
		

	
	
- 
		
			

			

Great article. I’ve always wanted to dive into graphics programming, but I’m afraid it will remian just a hobby for me. I’ll probbably never reach the level of expertise I’d like. Then LLMs came along, and everythinthe landscape has been changing so fast ever sine.

[Like](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?like_comment=18956&_wpnonce=76b1a7c87e)Liked by [1 person](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/#)

			
				[Reply](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/?replytocom=18956#respond)			
		

	
		

		
	
	

	
		
		

### Leave a comment [Cancel reply](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/#respond)

			
			

Δ
	
	

			
			
		

		
			
	
		
		
			
	
		

	

	

	

		
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
								
- 
						[Comment](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/#comments)
					
									
- 
						Reblog
					
									
- 
								Subscribe
		Subscribed
							
							
							
															
											
- 
			[The blog at the bottom of the sea](https://blog.demofox.org)
		
										
									
																						Join 185 other subscribers
																					
										
										
										
										
										
										
																				
											
												Sign me up											
										
									
									
- 
										
											Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fblog.demofox.org%252F2026%252F07%252F01%252Fwhat-to-learn-to-be-a-graphics-programmer%252F)										
									
								
															
						
					
							
- 
								
					
					
						
								
- 
			[The blog at the bottom of the sea](https://blog.demofox.org)
		
								
- 
										Subscribe
		Subscribed
								
														
- [Sign up](https://wordpress.com/start/)
							
- [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fblog.demofox.org%252F2026%252F07%252F01%252Fwhat-to-learn-to-be-a-graphics-programmer%252F)
																
- 
										[Copy shortlink](https://wp.me/p8L9R6-4M1)
									
																
- 
									[Report this content](https://wordpress.com/abuse/?report_url=https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/)
								
															
- 
									[View post in Reader](https://wordpress.com/reader/blogs/129449992/posts/18353)
								
															
- 
									[Manage subscriptions](https://subscribe.wordpress.com/)
								
																
- Collapse this bar
														
					
				
			
		
	
	

			
			
				
			
		
		

		
			
			
				
				
					
				
				
					
				
			
			
			
				
			
			
			
				
					
						
						
					
					
						
					
					
						
												
											
				
				
					
						
							
						
						
															
									Loading Comments...
								
								
								
									
									
																														
												Write a Comment...
												
												
													
																													
																Email (Required)
																
															
															
																Name (Required)
																
															
															
																Website
																
															
																											
													
												
											
																											
													
						
							
								
									
								

								
							
							
							
						
					
				
			
		

		
		
	
				
	

	
	%d
