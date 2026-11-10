---
title: "FFmpeg 9.1's new AAC encoder"
url: https://hydrogenaudio.org/index.php/topic,129691.0.html
clipped: 2026-08-31 12:22:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [FFmpeg 9.1's new AAC encoder](https://hydrogenaudio.org/index.php/topic,129691.0.html)

## Digest Summary
FFmpeg 9.1 introduces an updated AAC encoder with selectable coding algorithms. The example commands demonstrate encoding a FLAC source (“the‑tower‑8s.flac”) to AAC at a constant bitrate of 64 kb/s using three different coder settings:  
- `-aac_coder twoloop` selects the “twoloop” algorithm.  
- `-aac_coder nmr` selects the “nmr” (Noise‑Level‑Based Rate‑Control) algorithm.  
- Adding `-cutoff 12000` to the “nmr” mode limits the audio bandwidth to 12 kHz.  

The snippet includes two placeholder images labeled “HydrogenAudio” and an unspecified second image. The commands illustrate how to specify bitrate, coder type, and optional low‑pass cutoff when using the new AAC encoder in FFmpeg 9.1.

---

## Full Article

[Skip to main content](https://hydrogenaudio.org/index.php/topic,129691.0.html#skipnav)
	[↑](https://hydrogenaudio.org/index.php/topic,129691.0.html#top)
	[↓](https://hydrogenaudio.org/index.php/topic,129691.0.html#bot)
	
	
		
			
		
	
					
						

### 
							Notice
						


						
							
		Please note that most of the software linked on this forum is likely to be safe to use. If you are unsure, feel free to ask in the relevant topics, or send a private message to an administrator or moderator. To help curb the problems of false positives, or in the event that you do find actual malware, you can contribute through the article linked [here](https://hydrogenaudio.org/index.php?topic=120969).
							
						
					
	
	
		
			
				
				
			
			
			
		
			
			
			
				0 Members and 4 Guests are viewing this topic.
				
			
			
				
					
					
						
						Hi,I recently did a full rewrite of FFmpeg's AAC encoder.  Everything from rate control, RDO, and all coding tools (PNS, TNS, I/S and M/S) was reengineered. Metrics-wise (Google's new [Zimtohrli](https://github.com/google/zimtohrli), [ViSQOL](https://github.com/google/visqol), and my own hearing) it's apparently the best AAC encoder, compared to qaac and fdk-aac:kbps8.1 fast8.1 twoloopnmrfdk-aacapplelibopus640.01315 / 2.650.00696 / 3.240.00309 / 3.830.00322 / 3.690.00612 / 3.290.00100 / 4.59960.00338 / 3.770.00268 / 3.990.00134 / 4.040.00153 / 3.980.00175 / 3.870.00039 / 4.621280.00229 / 4.100.00170 / 4.280.00072 / 4.470.00143 / 4.270.00081 / 4.440.00020 / 4.681600.00129 / 4.300.00108 / 4.440.00051 / 4.560.00065 / 4.310.00117 / 4.510.00084 / 4.682560.00105 / 4.410.00121 / 4.550.00031 / 4.610.00103 / 4.450.00067 / 4.630.00002 / 4.73Zim/ViS, lower-is-better/higher-is-better respectively.[The rewrite](https://code.ffmpeg.org/FFmpeg/FFmpeg/pulls/23430) will be merged today. You can either compile it from source or grab one of [BtbN's latest nightly builds](https://github.com/BtbN/FFmpeg-Builds/releases/tag/latest) (once merged and they update) to test it.Some specifics:
- the new encoder is strictly CBR, with very little variation in rate. Having a bit budget target helps coding a lot. I don't recommend using -q:a (real VBR mode).
- Other encoders don't use any coding tools except TNS. So first, I beat them fair, using only TNS, then reimplemented PNS, I/S and M/S on top to crush them conclusively.
- I RE'd qaac and found out it does no perceptual optimizations. It simply uses band energy with a bit allocation curve that favours high frequencies. I improved on that by having a similar curve, and using masked band energy for the RDO.
- FFmpeg's AAC DEcoder is busted with regards to stereo PNS, and the bug may be in other AAC decoders too, so we work around it in the encoder. Since no other encoder used PNS, the bug was not found until now.
- Special attention was paid to high bitrates. Coding tools like I/S and PNS get turned off by themselves if the encoder does good on its own to maintain rate.
- All coding tools, PNS, TNS, I/S and M/S are part of the RDO loop. We use no parroted heuristics or arbitrary bitrate cutoffs. If a tool can be used, it will be used.
- If you intend to downmix or expect the output to get downmixed, use -aac_is 0 -aac_pns 0 to maintain the original signal phase.
- The encoder was mainly optimized for 48Khz audio. Get over it. It's 2026, resampling is free, 48Khz is the standard. 44.1Khz will work, and so will 96Khz but use 48Khz if you want the best quality.
- If you look at spectrograms, we leave a lot of holes. This is by design. Masked bands get zero'd or PNS'd, since a neighbouring band is loud enough to avoid noticing the missing bands. It's better to only code audible bands well, than code everything badly.I look forward to A/B testing by users. I tested this on 3000 tracks (my music collection), though I had very little speech content to test on, so it may need some optimizations there.The encoder prints extra stats on uninit:Qavg: 207.975  Tr: 5.3%  TNS(L): 4.8%  TNS(S): 36.9%  M/S: 3.9%  I/S: 10.0%  PNS: 5.1%Here's how to read them.
- the average lambda value (higher values == encoder struggles more to keep rate)
- Short blocks
- TNS usage on long frames
- TNS usage on short frames
- Mid/Side coding usage
- Intensity stereo coding usage
- Perceptual Noise Substitution usageIf you find annoying artifacts, post the original input samples, and that line so I can look into it.
						
					
					
					
				
				
				
					
					
					
						
						"The encoder was mainly optimized for 48Khz audio. Get over it. It's 2026, resampling is free, 48Khz is the standard. 44.1Khz will work, and so will 96Khz but use 48Khz if you want the best quality."Yet most of the worlds audio is 44KHz...
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: spoon on 2026-06-30 10:37:12](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083531)"The encoder was mainly optimized for 48Khz audio. Get over it. It's 2026, resampling is free, 48Khz is the standard. 44.1Khz will work, and so will 96Khz but use 48Khz if you want the best quality."Yet most of the worlds audio is 44KHz...The benchmarks I posted were done mainly on 44.1Khz. I tuned by ear on 48Khz data though, so some of the windowing/transient logic is tied to 48Khz. It translated to 44.1Khz well enough that I left it as-is, since the timing difference isn't that large.And if you're encoding lossily, may as well resample to 48 and not require decoders to do so on the other end.
						
					
					
					
				
				
				
					
					
					
						
						What do you mean, you tuned it by ear? Tuned what, exactly?
						
					
					
					
				
				
				
					
					
					
						
						I have some killer FLAC samples that clearly shows how old AAC encoder is low quality.I hope the new encoder is much better.
						
					
					
					
				
				
				
					
					
					
						
						Oh, Lynne is on HA! Welcome!For those unaware: Lynne also wrote the native USAC decoder for FFmpeg, all of it AFAIR. Bit off-topic, but: Lynne, are you aware of the USAC playback glitches during seeking? Discussed a lot here, e.g. [https://hydrogenaudio.org/index.php/topic,129641.msg1083064.html#msg1083064](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&/topic,129641.msg1083064.html#msg1083064) and [https://hydrogenaudio.org/index.php/topic,129641.msg1083087.html#msg1083087](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&/topic,129641.msg1083087.html#msg1083087)I agree with Mycroft that FFmpeg's old AAC encoder performs quite "suboptimally", and I think this is also confirmed in the results of one of Kamedo2's listening tests, [https://hydrogenaudio.org/index.php/topic,119861.0.html](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&/topic,119861.0.html)Chris
						
					
					
					
				
				
				
					
					
					
						
						Too bad, I am currently testing the FFmpeg AAC encoder version N-124995-gbb6de744cc, Sat, 13 Jun 2026 19:08:10 version. Your wholly-rewritten version won't be included in the upcoming ABC/HR listening test results(now 19% done).aac_mf is AAC via MediaFoundation (Available on Windows 10 and 11)Code: [[Select]](https://hydrogenaudio.org/index.php/topic,129691.0.html#) `$ ffmpeg124995 -i in.44100Hz.stereo.wav -c:a libopus -b:a 89k out.opus$ ffmpeg124995 -i in.44100Hz.stereo.wav -c:a opus -strict experimental -b:a 96k out.opus$ ffmpeg124995 -i in.44100Hz.stereo.wav -c:a libfdk_aac -b:a 96k out.mp4$ ffmpeg124995 -i in.44100Hz.stereo.wav -c:a aac -b:a 96k out.mp4$ ffmpeg124995 -i in.44100Hz.stereo.wav -c:a aac_mf -b:a 96k out.mp4$ ffmpeg124995 -i in.44100Hz.stereo.wav -c:a libmp3lame -b:a 96k out.mp3$ ffmpeg124995 -i in.44100Hz.stereo.wav -c:a ac3 -b:a 96k out.ac3` 
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: lynne on 2026-06-30 10:31:23](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083529)[The rewrite](https://code.ffmpeg.org/FFmpeg/FFmpeg/pulls/23430) will be merged today.well, turns out it did actually merge today.just... not the today that marked June 30, 2026.yeah.
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: C.R.Helmrich on 2026-06-30 16:00:40](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083556)Oh, Lynne is on HA! Welcome!For those unaware: Lynne also wrote the native USAC decoder for FFmpeg, all of it AFAIR. Bit off-topic, but: Lynne, are you aware of the USAC playback glitches during seeking? Discussed a lot here, e.g. [https://hydrogenaudio.org/index.php/topic,129641.msg1083064.html#msg1083064](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&/topic,129641.msg1083064.html#msg1083064) and [https://hydrogenaudio.org/index.php/topic,129641.msg1083087.html#msg1083087](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&/topic,129641.msg1083087.html#msg1083087)I agree with Mycroft that FFmpeg's old AAC encoder performs quite "suboptimally", and I think this is also confirmed in the results of one of Kamedo2's listening tests, [https://hydrogenaudio.org/index.php/topic,119861.0.html](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&/topic,119861.0.html)ChrisIt shouldn't be worse than seeking on HE-AAC, right? We don't handle preroll properly at FFmpeg yet, since the preroll grows by a lot due to the delay HE-AAC has.[Quote from: Kamedo2 on 2026-06-30 16:55:06](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083557)Too bad, I am currently testing the FFmpeg AAC encoder version N-124995-gbb6de744cc, Sat, 13 Jun 2026 19:08:10 version. Your wholly-rewritten version won't be included in the upcoming ABC/HR listening test results(now 19% done).I don't think you should cancel the tests you're running, but if you could, would you be able to run quick comparisons rather than full A/B testing?By the way, about the metrics, Zim is the better metric, but saturates at high bitrates, so ViS is used as a tiebreaker. Using this rule, we win across all comparisons (except Opus, because it's the best).
						
					
					
					
				
				
				
					
					
					
						
						tested new AAC encoder.solid encoding quality indeed.i tested this with only one song (Burn the Boats from Marathon [Vol. II]: They are Waiting (Original Game Soundtrack)), but did so with -b:a mode as lynne requested.following bitrates tested are 64kbps, 134kbps, 200kbps.64k is good, albeit with a bit of artifacting. not sure if ffmpeg AAC PNS decoder bug (playing the resulting file with ffplay btw) or not.134k and 200k makes for a sublime listen.
						
					
					
					
				
				
				
					
					
					
						
						Some command line help pls for fb2k? Highly interested, just not having much time and only few love for ffmpeg cmdline. 
						
					
					
					
				
				
				
					
					
					
						
						Example 1:Code: [[Select]](https://hydrogenaudio.org/index.php/topic,129691.0.html#) `ffmpeg -i input.flac -map 0:0 -c:a aac -b:a 128000 output.m4a` Example 2:Code: [[Select]](https://hydrogenaudio.org/index.php/topic,129691.0.html#) `ffmpeg -i input.flac -map 0:0 -c:a aac -aac_is 0 -b:a 128000 output.m4a` Example 3:Code: [[Select]](https://hydrogenaudio.org/index.php/topic,129691.0.html#) `ffmpeg -i input.flac -map 0:0 -c:a aac -aac_pns 0 -b:a 128000 output.m4a` 
						
					
					
					
				
				
				
					
					
					
						
						Decided to reduce bandwidth to 16Khz for 128Kbs and 18Khz for 160kbps+. You can use -cutoff 16000 or wait for the builds to update.
						
					
					
					
				
				
				
					
					
					
						
						Hi Lynne, edit: Seems that in my jurisdiction, even short samples (~8 seconds) cannot be provided. Keeping this information available in text form, in case Lynne has this particular song available.thanks for your work on the ffmpeg AAC encoder, this is certainly very exciting work!I think I'm having a sample the new encoder (current git main) doesn't like too much.Sample: First 8 seconds of "The Tower" by Bruce Dickinson.I think this uses the old AAC encoder, which appears to use a ca. 12 kHz cutoff:Code: [[Select]](https://hydrogenaudio.org/index.php/topic,129691.0.html#) `ffmpeg -i the-tower-8s.flac -b:a 64k -aac_coder twoloop the-tower-8s-64k-twoloop.aac` The new encoder:Code: [[Select]](https://hydrogenaudio.org/index.php/topic,129691.0.html#) `ffmpeg -i the-tower-8s.flac -b:a 64k -aac_coder nmr the-tower-8s-64k-nmr.aac` The new encoder, with a 12 kHz cutoff:Code: [[Select]](https://hydrogenaudio.org/index.php/topic,129691.0.html#) `ffmpeg -i the-tower-8s.flac -b:a 64k -aac_coder nmr -cutoff 12000 the-tower-8s-64k-nmr-12khz.aac` I feel that NMR, on this sample, is more smeary and metallic than the old encoder, even with the cutoff adjusted. The twoloop encoder has other problems (some collapse at the beginning, overall more noisy and rough) and I guess it's up to the listener to decide what's preferable.
						
					
					
					
				
				
				
					
					
					
						
						I quickly tested the fatboy_30sec sample at 192 kbps and heard a ticking sound at 6.836s and 10.480s. Resampling to 48kHz doesn't fix the problem, and actually introduces an additional tick at 14.125s. The ticking only disappears when TNS is turned off. I didn't do an ABX test because the issue is clearly audible. Still, it's great to hear a noticeable improvement in overall quality, so thanks to @lynne for that.Sample: [https://hydrogenaudio.org/index.php/topic,19682.msg193708.html](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&/topic,19682.msg193708.html)Commands:Code: [[Select]](https://hydrogenaudio.org/index.php/topic,129691.0.html#) `ffmpeg -i fatboy_30sec.flac -c:a aac -b:a 192000 output.m4affmpeg -i fatboy_30sec.flac -c:a aac -ar 48000 -b:a 192000 output48k.m4affmpeg -i fatboy_30sec.flac -c:a aac -aac_tns 0 -b:a 192000 output_notns.m4a` 
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: KrajzegaX on 2026-07-01 18:55:02](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083598)I quickly tested the fatboy_30sec sample at 192 kbps and heard a ticking sound at 6.836s and 10.480s. Resampling to 48kHz doesn't fix the problem, and actually introduces an additional tick at 14.125s. The ticking only disappears when TNS is turned off. I didn't do an ABX test because the issue is clearly audible. Still, it's great to hear a noticeable improvement in overall quality, so thanks to @lynne for that.Sample: [https://hydrogenaudio.org/index.php/topic,19682.msg193708.html](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&/topic,19682.msg193708.html)Commands:Code: [[Select]](https://hydrogenaudio.org/index.php/topic,129691.0.html#) `ffmpeg -i fatboy_30sec.flac -c:a aac -b:a 192000 output.m4affmpeg -i fatboy_30sec.flac -c:a aac -ar 48000 -b:a 192000 output48k.m4affmpeg -i fatboy_30sec.flac -c:a aac -aac_tns 0 -b:a 192000 output_notns.m4a` Are you able to build from source? If so, could you check if the clicking disappears if you set TNS_PG_C1_SHORT in libavcodec/aacenc_tns.c to higher values? Try 3.2, 4.2 and 5.0. I can't hear it myself, but it does look overly aggressive.
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: maikmerten on 2026-07-01 18:42:41](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083597)Hi Lynne, edit: Seems that in my jurisdiction, even short samples (~8 seconds) cannot be provided. Keeping this information available in text form, in case Lynne has this particular song available.There really isn't a lot we can do at 64kbps stereo. We can't boost PNS without ruining the stereo image. I don't have the track to test on either.
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: lynne on 2026-07-01 19:39:20](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083602)There really isn't a lot we can do at 64kbps stereo. We can't boost PNS without ruining the stereo image.Yeah, that's certainly true, usually 64kbps is for other AAC profiles. I'm happy to report that in the ~100 kbps range, things improve a lot (which is a surprise to exactly no one) and fixing the "roughness" and "noise" of the older encoder (which is great news, IMO).
						
					
					
					
				
				
				
					
					
					
						
						1. Attached the sample [@maikmerten](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&action=profile;u=1312) cannot, since I'm not in the same jurisdiction. Bruce Dickinson: The Tower. In case anyone else wants to give it a shot at their fave setting (or codec!) 29 seconds, not just the first 8.2. I welcome attempts to fix some outright errors in ffmpeg's audio codec handlings, It's not the only one. 3. Wouldn't mind if mods fixed the thread title either.
						
					
					
					
				
				
				
					
					
					
						
						First of all, I just want to thank you for finally creating a usable native AAC encoder for FFmpeg. The previous FFmpeg AAC encoder being bad bothered me a lot considering how many online infrastructures and open source projects (like OBS, Kdenlive and Handbrake) uses it with most people having no clue on how bad it sounds (even SoundCloud using it for a while before and ruining audio quality for everyone).With a simple test, the rewrite really does well on high bitrates which is really important (>128kbps). Best part is that the encoder by default is mono compatible at any bitrate I've tested it with (cough cough Opus having phase inversion enabled by default cough cough). Testing it with worst conditions however at 64kbps with forced 16khz cutoff, the Fraunhofer AAC encoder seems to still sound better than the rewrite when it comes to low bitrates. It tended to sound more metallic at 64kbps, and the snares for one song I tested really sounded metallic for the new AAC encoder while it sounded cleaner with fdk_aac:Code: [[Select]](https://hydrogenaudio.org/index.php/topic,129691.0.html#) `ffmpeg_new.exe -i "02. Porter Robinson - Cheerleader.flac" -vn -ab 64k -cutoff 16000 "cheerleader-64k-16khz-newaac.m4a"ffmpeg.exe -i "02. Porter Robinson - Cheerleader.flac" -vn -ab 64k -cutoff 16000 -c:a libfdk_aac "cheerleader-64k-16khz-fdkaac.m4a ` I guess I'll stick to libfdk_aac if its available to be safe, but what really matters is that we finally have a widely accessible AAC encoder inside native FFmpeg that's as good enough as libfdk_aac at normal/high bitrates (plus people should be using Opus at low bitrates anyway). There's definitely room for improvement, but it's very usable. The days of OBS Studio having horrible livestream audio by default are over.(also I was gonna say that the 18khz cutoff for 128kbps is too high but it seems that you've already figured that out)
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: notcharldeon on 2026-07-02 03:55:02](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083611)With a simple test, the rewrite really does well on high bitrates which is really important (>128kbps). Best part is that the encoder by default is mono compatible at any bitrate I've tested it with (cough cough Opus having phase inversion enabled by default cough cough). Testing it with worst conditions however at 64kbps with forced 16khz cutoff, the Fraunhofer AAC encoder seems to still sound better than the rewrite when it comes to low bitrates. It tended to sound more metallic at 64kbps, and the snares for one song I tested really sounded metallic for the new AAC encoder while it sounded cleaner with fdk_aac:I think that 15Khz is still too much for 64kbps. Could you test with 12Khz cutoff again? Also, could you do a separate test with mono? PNS is used a ton more in mono since we don't have to workaround the decoder bug.
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: lynne on 2026-07-01 19:39:20](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083602)There really isn't a lot we can do at 64kbps stereo.You could, and should (if possible in one's use case) downsample and encode the input at 32 kHz sampling rate. We do the same with non-SBR USAC encoding via exhale (preset 0-1), a comparable codec architecture.Chris
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: lynne on 2026-07-01 14:52:30](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083586)[Quote from: C.R.Helmrich on 2026-06-30 16:00:40](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083556)[...] USAC playback glitches during seeking? [...]It shouldn't be worse than seeking on HE-AAC, right? We don't handle preroll properly at FFmpeg yet, since the preroll grows by a lot due to the delay HE-AAC has.Actually some tracks glitch even without seeking. Seeking just triggers issues on all tracks so that's where the problems were first noticed. Here's an example track that simply can't be decoded right: [https://hydrogenaudio.org/index.php/topic,129447.0.html](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&/topic,129447.0.html).
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: lynne on 2026-07-01 17:22:48](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083595)Decided to reduce bandwidth to 16Khz for 128Kbs and 18Khz for 160kbps+. You can use -cutoff 16000 or wait for the builds to update.Regarding your recent decision to adjust the bandwidth thresholds for AAC (16kHz for 128kbps and 18kHz for 160kbps+), I was wondering if you have already decided on the target bandwidth for higher bitrates, specifically for 256kbps and above.Will those remain at >= 20kHz, or are you planning to adjust them as well?
						
					
					
					
				
				
				
					
					
					
						
						[Quote from: Goa Trance on 2026-07-02 09:12:47](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083620)[Quote from: lynne on 2026-07-01 17:22:48](https://hydrogenaudio.org/index.php?PHPSESSID=hgqi9tnm8ud3crcf9ci32b1ie6&msg=1083595)Decided to reduce bandwidth to 16Khz for 128Kbs and 18Khz for 160kbps+. You can use -cutoff 16000 or wait for the builds to update.Regarding your recent decision to adjust the bandwidth thresholds for AAC (16kHz for 128kbps and 18kHz for 160kbps+), I was wondering if you have already decided on the target bandwidth for higher bitrates, specifically for 256kbps and above.Will those remain at >= 20kHz, or are you planning to adjust them as well?Sure, I just made it so at 192kbps *per channel* the full 20Khz+ spectrum gets coded. Better to be conservative here, since the data is very expensive to code and the coder itself is still reluctant to not zero/PNS bands until you use 200kbps per channel.
