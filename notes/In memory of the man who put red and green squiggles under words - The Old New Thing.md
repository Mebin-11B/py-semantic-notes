---
title: "In memory of the man who put red and green squiggles under words - The Old New Thing"
url: https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451
clipped: 2026-08-31 12:26:35
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [In memory of the man who put red and green squiggles under words - The Old New Thing](https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451)

## Full Article

[Skip to main content](https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451#mainContent)
    

    
            [Dev Blogs](https://devblogs.microsoft.com)

    [AI](https://devblogs.microsoft.com/ai)

    

            [All .NET posts](https://devblogs.microsoft.com/dotnet/)

                [.NET MAUI](https://devblogs.microsoft.com/dotnet/category/maui/)
                [ASP.NET Core](https://devblogs.microsoft.com/dotnet/category/dotnet-aspire/)
                [Blazor](https://devblogs.microsoft.com/dotnet/category/blazor/)
                [Entity Framework](https://devblogs.microsoft.com/dotnet/category/entity-framework/)

                [C++](https://devblogs.microsoft.com/cppblog/)
                [C#](https://devblogs.microsoft.com/dotnet/category/csharp/)
                [F#](https://devblogs.microsoft.com/dotnet/category/fsharp/)
                [TypeScript](https://devblogs.microsoft.com/typescript/)

                [NuGet](https://devblogs.microsoft.com/dotnet/category/nuget/)
                [Servicing](https://devblogs.microsoft.com/dotnet/category/maintenance-and-updates/)
            [.NET Blog in Chinese](https://devblogs.microsoft.com/dotnet-ch/)

    

            [Microsoft for Developers](https://developer.microsoft.com/blog)
            [Agent Framework](https://devblogs.microsoft.com/agent-framework/)
            [Develop from the cloud](https://devblogs.microsoft.com/develop-from-the-cloud/)
            [Xcode](https://devblogs.microsoft.com/xcode/)
            [ISE Developer](https://devblogs.microsoft.com/ise/)
            [TypeScript](https://devblogs.microsoft.com/typescript/)
            [PowerShell](https://devblogs.microsoft.com/powershell/)
            [Python](https://devblogs.microsoft.com/python/)
            [Java](https://devblogs.microsoft.com/java/)
            [Java Blog in Chinese](https://devblogs.microsoft.com/java-ch/)
            [Go](https://devblogs.microsoft.com/go/)
            [Microsoft Edge Dev](https://blogs.windows.com/msedgedev/)
            [Microsoft 365 Developer](https://devblogs.microsoft.com/microsoft365dev/)
            [Microsoft Entra Identity Developer](https://devblogs.microsoft.com/identity/)
            [Microsoft Entra PowerShell](https://devblogs.microsoft.com/entrapowershell/)

    

            [Visual Studio](https://devblogs.microsoft.com/visualstudio/)
            [Visual Studio Code](https://devblogs.microsoft.com/vscode-blog)
            [Aspire](https://devblogs.microsoft.com/aspire/)

                [All things Azure](https://devblogs.microsoft.com/all-things-azure/)
                [Azure SDK](https://devblogs.microsoft.com/azure-sdk/)
                [Azure VM Runtime Team](https://devblogs.microsoft.com/azure-vm-runtime/)
                [Microsoft Azure](https://azure.microsoft.com/blog/)
                [Azure Cosmos DB](https://devblogs.microsoft.com/cosmosdb/)
                [Azure DocumentDB](https://devblogs.microsoft.com/documentdb/)
                [Azure Data Studio](https://cloudblogs.microsoft.com/sqlserver/?product=azure-data-studio)
                [Azure SQL](https://devblogs.microsoft.com/azure-sql/)
            [DevOps](https://devblogs.microsoft.com/devops/)
            [DirectX](https://devblogs.microsoft.com/directx/)
            [Microsoft Foundry](https://devblogs.microsoft.com/foundry/)
            [Power Platform](https://devblogs.microsoft.com/powerplatform/)

    

            [OData](https://devblogs.microsoft.com/odata/)
            [Unified Data Model (IDEAs)](https://devblogs.microsoft.com/udm/)

    

            [Windows Command Line](https://devblogs.microsoft.com/commandline/)
            [#ifdef Windows](https://devblogs.microsoft.com/ifdef-windows/)
            [Inside MSIX](https://devblogs.microsoft.com/insidemsix/)
            [MIDI and music](https://devblogs.microsoft.com/windows-music-dev/)
            [React Native](https://devblogs.microsoft.com/react-native/)
            [The Old New Thing](https://devblogs.microsoft.com/oldnewthing/)
            [Windows Developer](https://blogs.windows.com/windowsdeveloper/)

    
        

            
            
    

    	
	
	
							
									

													
															
						
												
							
														
											
							
 
  
    
    
        
                
                            
                    
                        
                    
                    
                                                
                            [Raymond Chen](https://devblogs.microsoft.com/oldnewthing/author/oldnewthing)
                        

                                            
                
                    
    
    

    
    
        
            

I recently learned of the passing of someone whose work nearly everybody knows, but nobody knows his name.

Tony Krueger is [remembered in Wikipedia](https://en.wikipedia.org/wiki/Chip's_Challenge) as the person who ported the game Chip’s Challenge to Windows for the Windows Entertainment Pack.¹ But that’s probably not the code he wrote that touched the most people.

Tony worked on Word 1.0, 1.1, 2.0, then on Word for OS/2 and Word for Mac, then returned to Word 6.0 and several versions beyond that. He probably holds the record for “most versions of Word shipped.”

In early versions of Word, the Spell Check feature was something that you explicitly invoked, and then you had to sit and wait while the program looked for all your potentially-misspelled words, and then showed them to you one at a time for a decision on what to do for each one. Word did introduce an Auto Spell Check feature to run spell check when the user was idle, so that when you hit the Spell Check button, the results were ready to go. However, the Auto Spell Check was still a blocking operation. As a result, a lot of users turned it off because it always seemed to decide “Now would be a good time to spell-check the document” just as you wanted to do something, forcing you to wait for the spell check pass to complete before you could, say, save and exit.

Tony made the spell checker much more unobtrusive so that it didn’t interfere with your foreground work. And when it found a problem, instead of waiting for you to trigger a spell check, it immediately drew red squiggles under potentially-misspelled words (and later green squiggles under potential grammatical errors).

Tony was an early fan of the magic/comedy team Penn and Teller. A friend and colleague attended a show and hung out afterward to ask the duo to sign a photo for his friend Tony. “He was on the team that did the red and green squiggles in Word.”

Upon hearing this, Penn Jillette announced in his stentorian voice which filled the entire theater: “The red and green squiggles!? I love the red and green squiggles!” Teller silently concurred.

Tony received that autographed photo for his birthday, and it wasn’t clear which he was more happy about, the autographed photo or the fact that Penn and Teller loved his feature.

Many years later, “Weird Al” Yankovic recorded a parody video titled [Word Crimes](https://www.youtube.com/watch?v=8Gv0H-vPoDc), in which the Word red squiggles make a brief appearance. That same friend got “Weird Al” to autograph the screen shot.

Today, there are red (and even green and blue) squiggles in nearly every word processor, and often outside word processors. Tony did it first. The next time a red squiggle catches one of your mistakes, say thanks to Tony. I think he’d appreciate it.

¹ Probably not as widely documented is that he accomplished this without the source code: He reverse-engineered the MS-DOS version and then reimplemented it for Windows.
        

        
            
    

    

    
    
        

### Category

- [Old New Thing](https://devblogs.microsoft.com/oldnewthing/category/oldnewthing)

### Topics

- [History](https://devblogs.microsoft.com/oldnewthing/tag/history)
					

### Share

					
						
- 
							
						
						
- 
							
						
						
- 
							
						
					
				        
            

## Author

            [Raymond Chen](https://devblogs.microsoft.com/oldnewthing/author/oldnewthing)

Raymond has been involved in the evolution of Windows for more than 30 years. In 2003, he began a Web site known as The Old New Thing which has grown in popularity far beyond his wildest imagination, a development which still gives him the heebie-jeebies. The Web site spawned a book, coincidentally also titled The Old New Thing (Addison Wesley 2007). He occasionally appears on the Windows Dev Docs Twitter account to tell stories which convey no useful information.        
    
    
  
    
    
      
      
        

    
    				

## 
            26 comments		

		
			

Discussion is closed.				[Login to edit/delete existing comments.](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260622-00%2F%3Fp%3D112451%23comments)
				
	
	
		
			

			
				
					
					
					
					
				
				[Code of Conduct](https://aka.ms/msftqacodeconduct)
			
			
		
	

					
				
						
				
				
					
						Sort by :
						
							Newest
							
								Newest
								Popular
								Oldest
							
						
					
				
			
				
								
    
- 
    	
						
							
        
																		
									

@Gutleber, Richard 

> Windows has always had “high-contrast mode”, but that’s a bit extreme.

Yes, but it makes EVERYTHING contrast-y which is tiring to look at unless you are half-blind and you actually need that.

It also had high contrast but only black on white before dark mode was added (which in itself was added late and poorly).

Come to think of it, whole Windows GUI is a convoluted mess, and here's why:

1. The idea that DPI isn't an actual display property read from EDID but a user adjustable setting (scaling) is pure madness. Whoever made that decision should be thrown in jail...Read more

@Gutleber, Richard 

> Windows has always had “high-contrast mode”, but that’s a bit extreme.

Yes, but it makes EVERYTHING contrast-y which is tiring to look at unless you are half-blind and you actually need that.

It also had high contrast but only black on white before dark mode was added (which in itself was added late and poorly).

Come to think of it, whole Windows GUI is a convoluted mess, and here’s why:

1. The idea that DPI isn’t an actual display property read from EDID but a user adjustable setting (scaling) is pure madness. Whoever made that decision should be thrown in jail and left to rot because on a high-DPI monitor everything will be smaller and there’s no way to properly fix that nor to be able to say I want a 1 cm letter size and then put a ruler to display and actually measure that.
2. The “Make text bigger” option which 95% of apps don’t respect because querying font size user set is an obscure operation requiring you to query icon title font size and try to reverse-engineer which size would that be with a totally different font instead of having a function returning either scale factor or a number you can use directly.
3. Non-customizable UI colors in 2026. Not only non-customizable, but also non-queriable programmatically. You want to mimic dark theme colors? Sucks to be you. And even if you know the colors? Either custom-draw everything or use obscure undocumented WM_ messages to make your menu background dark.
4. Deluge of disjointed, half-assed, and abandoned GUI frameworks — User32 / GDI (native Win32), MFC, WTL, Windows Forms, WPF, UWP, WinUI 3…. That a cross-platform Qt framework of all things is used by many serious Windows apps and that the rest is using CEF is a testament to how sick the Windows developers are of chasing Microsoft’s latest GUI fad.

And now that I mentioned it, the reason why Windows is losing relevance as a desktop platform is exactly that lack of unified GUI framework.

If you make it easier to write a decent looking desktop app by using Chrome Electron Framework, then once the developers turn their apps into browser frames showing a copy of their website those can work on ANY operating system. And people are no longer trapped and incentivized to stay on Windows. Ouch, self-inflicted gunshot wound to the liver.
Read less									

				
							
									
			        
      
    
	
    
- 
    	
						
							
        
																		
									

I so greatly appreciate you folks writing these memories and stories about Tony!  I am Tony's father and I must tell you how gutted we all were to lose him so young!

Tony spent his entire post grad working career at Microsoft.  He graduated from Stanford in 1989 and started at Microsoft right after.  (By then he had already worked two previous summer internships there).  He passed away very unexpectedly on April 14, 2026, at age 58.  By then he was about to complete year 37 as a full-time MS employee.  He was there -...Read more

I so greatly appreciate you folks writing these memories and stories about Tony!  I am Tony’s father and I must tell you how gutted we all were to lose him so young!

Tony spent his entire post grad working career at Microsoft.  He graduated from Stanford in 1989 and started at Microsoft right after.  (By then he had already worked two previous summer internships there).  He passed away very unexpectedly on April 14, 2026, at age 58.  By then he was about to complete year 37 as a full-time MS employee.  He was there – and planned to continue working because he loved what he did.

As parents, we never really knew much about what Tony was working on.  When we would ask, he would do his best to give us some description, but it was difficult for us “non-Techies” to comprehend.  If we understood correctly, he was quite involved in the development of the Click-to-Run system that MS used/(still uses?) to transmit updates, etc..

He never really wanted credit for what he had done.  He was a quiet, thoughtful fellow and very modest and unassuming.

Tony was also totally dedicated to his own family and was a wonderful husband and great father to his two boys.

Anyway, we are obviously very proud of Tony and really appreciate hearing stories about his activities!  So, thank you Raymond Chen, the originator of this Blog, and to Doug Timpe for passing along the link!!

Dick Krueger
Tony Krueger’s Father
Read less									

				
							
									
			        
      
    
	
    
- 
    	
						
							
        
																		
									

I’m sorry for your loss.  58 is far to young.
									

				
							
									
			        
      
    
	
    
- 
    	
						
							
        
																		
									

I remember when this feature came out. Felt a bit like sorcery, given the power available at the time. I love hearing about the people behind the features. It’s the seemingly little things that stick in people’s memories.
									

				
							
									
			        
      
    

	
    
- 
    	
						
							
        
																		
									

By "came up with it," that would be the implementation in the source code in Word. 

I believe a PM named Diana originally came up with the design in the Word for Windows specification (circa 1989?) and in later versions (after the initial spec), Tony's Dev Manager, Jim Walsh also had design input. 

Tony and I played Chip's Challenge on our Atari Lynx systems. (In fact, on one of those evenings when we were playing Chip's Challenge and Slime World in one of the Building 5 conference rooms, we heard about the Bay area earthquake that destroyed the 880 freeway,...Read more

By “came up with it,” that would be the implementation in the source code in Word. 

I believe a PM named Diana originally came up with the design in the Word for Windows specification (circa 1989?) and in later versions (after the initial spec), Tony’s Dev Manager, Jim Walsh also had design input. 

Tony and I played Chip’s Challenge on our Atari Lynx systems. (In fact, on one of those evenings when we were playing Chip’s Challenge and Slime World in one of the Building 5 conference rooms, we heard about the Bay area earthquake that destroyed the 880 freeway, and were pretty shocked. Word spread fast that we’d lost a Microsoft employee during their commute home.) 

And today I learned something new about it — Tony and I had worked on it to meet his ship date all through the summer of 1992. We went down to the Kirkland Best Buy together and he managed to find and purchase a copy of the DOS version of Chip’s Challenge. 

Tony used that to reverse engineer the database for the 149 levels. The Entertainment Pack PM, Charles Fitzgerald, then got the license from Epyx Games (before they went bankrupt) and the rest is history.

Today’s Chip’s Challenge trivia came from the fact that the original author at Epyx, Chuck Sommerville, couldn’t get a license from the Epyx post-bankruptcy company in order to be able to ship his own Chip’s Challenge 2 update (I found it on Steam today – not sure if it’s the “same” Chip’s Challenge 2 or not). 

But back then, in order for Chuck to be able to run the program, he had to have people use Tony’s version of Chip’s Challenge for the chips.dat file, or Chips Challenge 2 wouldn’t run!

I’m not even sure Tony knew about that!
Read less									

				
							
									
			        
      
    
	
    
- 
    	
						
							
        
																		
									

It is the same Chip’s Challenge 2 – IIRC the buyback of the rights was crowdfunded.

Various tools have been written over the years to create custom levels for Chip’s Challenge (and, indeed, the game runtime has also been cloned). The CHIPS.DAT parser in the Win16 Chip’s Challenge doesn’t check for buffer overflow, so it’s possible to craft a CHIPS.DAT file that crashes the game; it may be possible for a better Win16 hacker than me to create one that executes arbitrary code.
									

				
							
									
			        
      
    

	
    
- 
    	
						
							
        
																		
									

I remember when I first saw that feature, I was really impressed at the idea of the software unobtrusively flagging things for your attention.  I’ve rarely used Word, so it’s possible I first saw it in other software, but it was a significant improvement in usability for spell checking. 

Also, Chip’s Challenge was a great game.  The Windows Entertainment Packs were unreasonably entertaining in an era when Windows games were almost non-existent, aside from the few that shipped with Windows 3.
									

				
							
									
			        
      
    
					
			
Load more comments
								      
      
        
          
    

## Read next

    
        
  
      June 30, 2026
      

### [A compatibility note on the abuse of Windows window class extra bytes](https://devblogs.microsoft.com/oldnewthing/20260630-00/?p=112488)

      
            
                        
        
        Raymond Chen
    

  
      July 7, 2026
      

### [How did Windows 95 decide that a setup program ran?](https://devblogs.microsoft.com/oldnewthing/20260707-00/?p=112508)

      
            
                        
        
        Raymond Chen
    

    
            
      
      
      

    
        

## Stay informed

        Get notified when new posts are published.
            
                
                
                    Email *
                     
                    Country/Region *
                        Select...United StatesAfghanistanÅland IslandsAlbaniaAlgeriaAmerican SamoaAndorraAngolaAnguillaAntarcticaAntigua and BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBonaireBosnia and HerzegovinaBotswanaBouvet IslandBrazilBritish Indian Ocean TerritoryBritish Virgin IslandsBruneiBulgariaBurkina FasoBurundiCabo VerdeCambodiaCameroonCanadaCayman IslandsCentral African RepublicChadChileChinaChristmas IslandCocos (Keeling) IslandsColombiaComorosCongoCongo (DRC)Cook IslandsCosta RicaCôte dIvoireCroatiaCuraçaoCyprusCzechiaDenmarkDjiboutiDominicaDominican RepublicEcuadorEgyptEl SalvadorEquatorial GuineaEritreaEstoniaEswatiniEthiopiaFalkland IslandsFaroe IslandsFijiFinlandFranceFrench GuianaFrench PolynesiaFrench Southern TerritoriesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuadeloupeGuamGuatemalaGuernseyGuineaGuinea-BissauGuyanaHaitiHeard Island and McDonald IslandsHondurasHong Kong SARHungaryIcelandIndiaIndonesiaIraqIrelandIsle of ManIsraelItalyJamaicaJan MayenJapanJerseyJordanKazakhstanKenyaKiribatiKoreaKosovoKuwaitKyrgyzstanLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacau SARMadagascarMalawiMalaysiaMaldivesMaliMaltaMarshall IslandsMartiniqueMauritaniaMauritiusMayotteMexicoMicronesiaMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueMyanmarNamibiaNauruNepalNetherlandsNew CaledoniaNew ZealandNicaraguaNigerNigeriaNiueNorfolk IslandNorth MacedoniaNorthern Mariana IslandsNorwayOmanPakistanPalauPalestinian AuthorityPanamaPapua New GuineaParaguayPeruPhilippinesPitcairn IslandsPolandPortugalPuerto RicoQatarRéunionRomaniaRwandaSabaSaint BarthélemySaint Kitts and NevisSaint LuciaSaint MartinSaint Pierre and MiquelonSaint Vincent and the GrenadinesSamoaSan MarinoSão Tomé and PríncipeSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSint EustatiusSint MaartenSlovakiaSloveniaSolomon IslandsSomaliaSouth AfricaSouth Georgia and South Sandwich IslandsSouth SudanSpainSri LankaSt HelenaAscensionTristan da CunhaSurinameSvalbardSwedenSwitzerlandTaiwanTajikistanTanzaniaThailandTimor-LesteTogoTokelauTongaTrinidad and TobagoTunisiaTurkeyTurkmenistanTurks and Caicos IslandsTuvaluU.S. Outlying IslandsU.S. Virgin IslandsUgandaUkraineUnited Arab EmiratesUnited KingdomUruguayUzbekistanVanuatuVatican CityVenezuelaVietnamWallis and FutunaYemenZambiaZimbabwe
                        
                        I would like to receive the The Old New Thing Newsletter. [Privacy Statement.](https://go.microsoft.com/fwlink/?LinkId=521839)
                    
                    
                    
                        Subscribe
                    
                
            
                
        Follow this blog
        
            
- 
- 
- 
-         
    

    
  

  
    
      
      
    
  

  
    
      
        Are you sure you wish to delete this
          comment?
        
      
      
        OK
        Cancel
      
    
  

        
        [Sign in](https://devblogs.microsoft.com/oldnewthing/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Foldnewthing%2F20260622-00%2F%3Fp%3D112451)
    
    
    
        Theme
    

    
    

		
				
				
		
		
				

## Insert/edit link

		
			Close		
		
			
				

Enter the destination URL
				
					URL
					
				
				
					Link Text
					
				
				
					
					 Open link in a new tab
				
			
			

Or link to existing content
			
				
					
						Search
						
						
					
				
				
					
					
						
					
				
				
					
						No search term specified. Showing recent items.
						
							Search or use up and down arrow keys to select an item.						
					
					
					
						
					
				
			
		
		
			
				Cancel
			
			
				
			
		
		
		
		    
            		
		
	
	
		
		
			

##### Code Block

			
			×
			
		
		
			
				
					Paste your code snippet
					
				
			
			
				Ok
				Cancel
			
		
		
	
	

  

    
    

            
                    
                                [Surface Pro](https://www.microsoft.com/surface/devices/surface-pro)                            
                                [Surface Laptop](https://www.microsoft.com/surface/devices/surface-laptop)                            
                                [Surface Laptop Ultra](https://www.microsoft.com/en-us/surface/devices/surface-laptop-ultra?icid=DSM_Footer_WhatsNew_SurfaceLaptopUltra)                            
                                [Surface RTX Spark Dev Box](https://www.microsoft.com/en-us/surface/devices/surface-rtx-spark-dev-box?icid=DSM_Footer_WhatsNew_SurfaceRTXSparkDevBox)                            
                                [Copilot for organizations](https://www.microsoft.com/en-us/microsoft-copilot/organizations?icid=DSM_Footer_CopilotOrganizations)                            
                                [Copilot for personal use](https://www.microsoft.com/en-us/microsoft-copilot/for-individuals?form=MY02PT&OCID=GE_web_Copilot_Free_868g3t5nj)                            
                                [Explore Microsoft products](https://www.microsoft.com/en-us/microsoft-products-and-apps)                            
                                [Windows 11 apps](https://www.microsoft.com/en-us/windows/apps-for-windows?icid=DSM_Footer_WhatsNew_Windows11apps)                            
                    
                    
                                [Account profile](https://account.microsoft.com/)                            
                                [Download Center](https://www.microsoft.com/en-us/download)                            
                                [Microsoft Store support](https://go.microsoft.com/fwlink/?linkid=2139749)                            
                                [Returns](https://www.microsoft.com/en-us/store/b/returns)                            
                                [Order tracking](https://www.microsoft.com/en-us/store/b/order-tracking)                            
                                [Certified Refurbished](https://www.microsoft.com/en-us/store/b/certified-refurbished-products)                            
                                [Microsoft Store Promise](https://www.microsoft.com/en-us/store/b/why-microsoft-store?icid=footer_why-msft-store_7102020)                            
                                [Flexible Payments](https://www.microsoft.com/en-us/store/b/payment-financing-options?icid=footer_financing_vcc)                            
                    
                    
                                [Microsoft in education](https://www.microsoft.com/en-us/education)                            
                                [Devices for education](https://www.microsoft.com/en-us/education/devices/overview)                            
                                [Microsoft Teams for Education](https://www.microsoft.com/en-us/education/products/teams)                            
                                [Microsoft 365 Education](https://www.microsoft.com/en-us/education/products/microsoft-365)                            
                                [How to buy for your school](https://www.microsoft.com/education/how-to-buy)                            
                                [Educator training and development](https://education.microsoft.com/)                            
                                [Deals for students and parents](https://www.microsoft.com/en-us/store/b/education)                            
                                [AI for education](https://www.microsoft.com/en-us/education/ai-in-education)                            
                    
            
            
                    
                                [Microsoft AI](https://www.microsoft.com/en-us/ai?icid=DSM_Footer_AI)                            
                                [Microsoft Security](https://www.microsoft.com/en-us/security)                            
                                [Dynamics 365](https://www.microsoft.com/en-us/dynamics-365)                            
                                [Microsoft 365](https://www.microsoft.com/en-us/microsoft-365/business)                            
                                [Microsoft Power Platform](https://www.microsoft.com/en-us/power-platform)                            
                                [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)                            
                                [Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365-copilot?icid=DSM_Footer_Microsoft365Copilot)                            
                                [Small Business](https://www.microsoft.com/en-us/store/b/business?icid=CNavBusinessStore)                            
                    
                    
                                [Azure](https://azure.microsoft.com/en-us/)                            
                                [Microsoft Developer](https://developer.microsoft.com/en-us/)                            
                                [Microsoft Learn](https://learn.microsoft.com/)                            
                                [Support for AI marketplace apps](https://www.microsoft.com/software-development-companies/offers-benefits/isv-success?icid=DSM_Footer_SupportAIMarketplace&ocid=cmm3atxvn98)                            
                                [Microsoft Tech Community](https://techcommunity.microsoft.com/)                            
                                [Microsoft Marketplace](https://marketplace.microsoft.com?icid=DSM_Footer_Marketplace&ocid=cmm3atxvn98)                            
                                [Software companies](https://www.microsoft.com/software-development-companies?icid=DSM_Footer_SoftwareCompanies&ocid=cmm3atxvn98)                            
                                [Visual Studio](https://visualstudio.microsoft.com/)                            
                    
                    
                                [Careers](https://careers.microsoft.com/)                            
                                [About Microsoft](https://www.microsoft.com/about)                            
                                [Company news](https://news.microsoft.com/source/?icid=DSM_Footer_Company_CompanyNews)                            
                                [Privacy at Microsoft](https://www.microsoft.com/en-us/privacy?icid=DSM_Footer_Company_Privacy)                            
                                [Investors](https://www.microsoft.com/investor/default.aspx)                            
                                [Diversity and inclusion](https://www.microsoft.com/en-us/diversity/default?icid=DSM_Footer_Company_Diversity)                            
                                [Accessibility](https://www.microsoft.com/en-us/accessibility)                            
                                [Sustainability](https://www.microsoft.com/en-us/corporate-responsibility/sustainability?icid=DSM_Footer_Sustainability)                            
                    
            

    
        
[Your Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)
        
    
    [Consumer Health Privacy](https://go.microsoft.com/fwlink/?linkid=2259814)
    

            [Sitemap](https://www.microsoft.com/en-us/sitemap1.aspx)
            [Contact Microsoft](https://support.microsoft.com/contactus)
            [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
            [Manage cookies](https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451#)
            [Terms of use](https://go.microsoft.com/fwlink/?LinkID=206977)
            [Trademarks](https://go.microsoft.com/fwlink/?linkid=2196228)
            [Safety & eco](https://go.microsoft.com/fwlink/?linkid=2196227)
            [Recycling](https://www.microsoft.com/en-us/legal/compliance/recycling)
            [About our ads](https://choice.microsoft.com)
