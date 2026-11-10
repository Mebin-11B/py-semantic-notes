---
title: "HTML Can Do That · Chris Burnell"
url: https://chrisburnell.com/html-can-do-that/
clipped: 2026-08-31 12:26:31
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [HTML Can Do That · Chris Burnell](https://chrisburnell.com/html-can-do-that/)

## Full Article

# HTML Can Do That

	

HTML has been gobbling up swathes of what used to be JavaScript’s remit. This page lists a bunch of dynamic functionality that we can now achieve with just HTML.

	

	

		

Update 2026-08-20: I originally built this page in one hour during [HTML Day 2026](https://2026.html.energy) to write and celebrate HTML, but I’ve since made some edits to better express and highlight where the browser implementation of some of this stuff is severely lacking and/or completely fails to meet accessibility needs. So, by all means, try it out, but make it as accessible as you can!

		

		
			

##  `popover` 

			

Browser Support: [popover →](https://caniuse.com/mdn-html_global_attributes_popover)
			

Light dismiss, Esc to close, no managing  `z-index`  to wrangle it onto a top layer. All managed with  `popover`  and  `popovertarget`  (and  `popovertargetaction` ) attributes in HTML. ([MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover))
			Toggle popover
			
				

No JavaScript, just modern browser magic, thanks to the wonderful folks speccing for the web and building our browsers!
				Close
			
			 ` `<button popovertarget="example-popover">Toggle popover</button>
<div id="example-popover" popover>
	<p>No JavaScript, just modern browser magic, thanks to the wonderful folks speccing for the web and building our browsers!</p>
	<button popovertarget="example-popover" popovertargetaction="hide">Close</button>
</div>` ` 

		

		

		
			

##  `<dialog>` 

			

Browser Support: [dialog →](https://caniuse.com/dialog)
			

Similar thing going on as  `popover`  here, except this time with a dedicated element for modal dialog boxes. ([MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog))
			

See  ``  `` [command / commandFor](https://chrisburnell.com/html-can-do-that/#command-commandfor) below for another, more recently-landing feature that allows us to open and close dialog elements (and will be useful for lots of other non-JS functionality, one day!).
			Toggle <dialog> popover
			
				

Once again the  `popover`  attribute is doing some heavy-lifting here!
				Close
			
			 ` `<button popovertarget="example-dialog">Toggle &lt;dialog&gt; popover</button>
<dialog id="example-dialog" popover>
	<p>Closed with just HTML via <code>&lt;form method="dialog"&gt;</code>, opened with the <code>popover</code> attribute.</p>
	<button popovertarget="example-dialog" popovertargetaction="hide">Close</button>
</dialog>` ` 

			

Even though it’s sort of against the spirit of this page, I want to include this short snippet of how to interact with dialog elements in JavaScript:
			Open dialog
			
				

This one is opened with  `.showModal()`  and closed with  `.close()` , both called from JavaScript.
				Close
			
			
			
				Show JS-powered dialog code
				 ` `<button id="example-dialog-js-open">Open dialog</button>
<dialog id="example-dialog-js">
	<p>This one is opened with <code>.showModal()</code> and closed with <code>.close()</code>, both called from JavaScript.</p>
	<button id="example-dialog-js-close">Close</button>
</dialog>` ` 
 ` `document.getElementById("example-dialog-js-open").addEventListener("click", () => {
	document.getElementById("example-dialog-js").showModal()
})
document.getElementById("example-dialog-js-close").addEventListener("click", () => {
	document.getElementById("example-dialog-js").close()
})` ` 

			
		

		

		
			

## Grouped  `<details>` 

			

Browser Support: [details name →](https://caniuse.com/mdn-html_elements_details_name)
			

A shared  `name`  attribute turns a group of  `<details>`  into an exclusive accordion. Open one and the others close automatically. Magic! ([MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDetailsElement/name))
			
				First
				

Open the second one and watch this close on its own.
			
			
				Second
				

First one’s hidden now.
			
			 ` `<details name="example-group">
	<summary>First</summary>
	<p>Open the second one and watch this close on its own.</p>
</details>
<details name="example-group">
	<summary>Second</summary>
	<p>First one’s hidden now.</p>
</details>` ` 

		

		

		
			

##  `command`  &  `commandfor` 

			

Browser Support: [invoker commands →](https://caniuse.com/wf-invoker-commands)
			

Separate HTML buttons controlling one popover. No scripting. ([MDN](https://developer.mozilla.org/en-US/docs/Web/API/Invoker_Commands_API))
			

Note: So far only  `show-modal` ,  `close` ,  `request-close` ,  `toggle-popover` ,  `show-popover` , and  `hide-popover`  have landed stable in browsers. We can look forward to invokers supported in the future to increment/decrement values, interact with media elements, copy text, etc.
			Open
			Close
			
				

 `show-popover`  opens this and  `hide-popover`  closes it!
				Close
			

			 ` `<button command="show-popover" commandfor="example-command-popover">Open</button>
<button command="hide-popover" commandfor="example-command-popover">Close</button>
<dialog id="example-command-popover" popover>
	<p><code>show-popover</code> opens this and <code>hide-popover</code> closes it!</p>
	<button command="hide-popover" commandfor="example-command-popover">Close</button>
</dialog>` ` 

		

		

		
			

##  `loading="lazy"` 

			

Browser Support: [loading-lazy-attr →](https://caniuse.com/loading-lazy-attr)
			

This image defers loading until it’s near the viewport. Not an  `` [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) in sight. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading))
			
			 ` `<img src="/images/avatar@2x.jpeg" loading="lazy" width="200" height="200" alt="a photo portait of Chris Burnell’s face">` ` 

		

		

		
			

## hidden until-found

			

Browser Support: [hidden until-found →](https://caniuse.com/mdn-html_global_attributes_hidden_until-found)
			

Navigating to the fragment link below reveals the hidden section. The browser automatically removes  `hidden="until-found"` . ([MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#using_the_until-found_value))
			

Note: This one’s still pretty new and only really plays nicely with browser default search, and not so well with screen reader search implementations, for example. Still, one to keep in the back pocket for another day down the road!
			[Jump to hidden content](https://chrisburnell.com/html-can-do-that/#example-until-found)
			
				

Yahaha! You found me!
			
			 ` `<a href="#example-until-found">Jump to hidden content</a>
<div id="example-until-found" hidden="until-found">
	<p>Yahaha! You found me!</p>
</div>` ` 

		

		

		
			

## More Native Elements

			

Browser Support: [input-color →](https://caniuse.com/input-color), [input-range →](https://caniuse.com/input-range), [input-datetime →](https://caniuse.com/input-datetime), [meter →](https://caniuse.com/meter), [progress →](https://caniuse.com/progress)
			

Colour, date, and range pickers, meters, and progress bars built right into the browser. ([MDN: Color Input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color), [MDN: Date Input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date), [MDN: Range Input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range), [MDN: Meter](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter), [MDN: Progress](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress))
			

Warning! Some of these elements feel a little unfinished. I’m hoping that we can expect form elements to receive some more love over the coming years, but at this point in time, the implementations shipping in browsers are, unfortunately, lacking. I would tread very carefully with using some of these. You can expect things like the default browser styles of these elements to vary pretty wildly between browsers and for the accessibility experienecs to be very poor. Be wary of the many pitfalls!
			

Colour 
			

Date 
			

Range 
			

Progress: 42%
			

Meter: Low  Between  High 
			 ` `<label>Colour <input type="color" value="#663399" autocomplete="off"></label>
<label>Date <input type="date" autocomplete="off"></label>
<label>Range <input type="range" min="0" max="100" value="50" autocomplete="off"></label>
<progress value="42" max="100">42%</progress>
<meter min="0" value="50" max="100" low="20" high="80" optimum="90"></meter>` ` 

		

		

		
			

##  `<datalist>` 

			

Browser Support: [datalist →](https://caniuse.com/datalist)
			

Native autocomplete suggestions, no dropdown library required. ([MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist))
			

Warning! Support for this across input types is still pretty spotty, and there are also a number of issues in its implementation in browsers. See Adrian Roselli’s [Under-Engineered Comboboxen](https://adrianroselli.com/2023/06/under-engineered-comboboxen.html) for more info. You might even want to skip using this for now, and keep an eye on it to see if it improves over the new few years.
			Favourite HTML element 
			
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
			
			 ` `<label>Favourite HTML element <input type="text" id="example-datalist-input" list="example-datalist" autocomplete="off"></label>
<datalist id="example-datalist">
	<option value="a">
	<option value="abbr">
	<option value="address">
	<!-- ... -->
</datalist>` ` 

		

		

	

	

	[IndieNews](https://news.indieweb.org/en)
