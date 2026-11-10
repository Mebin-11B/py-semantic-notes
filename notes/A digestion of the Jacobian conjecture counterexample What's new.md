---
title: "A digestion of the Jacobian conjecture counterexample | What's new"
url: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/
clipped: 2026-08-31 12:26:31
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [A digestion of the Jacobian conjecture counterexample | What's new](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)

## Full Article

[What's new](https://terrytao.wordpress.com/)		

Updates on my research and expository papers, discussion of open problems, and other maths-related topics.  By Terence Tao	

	
		
	
- [Home](https://terrytao.wordpress.com/)
	
- [About](https://terrytao.wordpress.com/about/)

- [Career advice](https://terrytao.wordpress.com/career-advice/)

- [On writing](https://terrytao.wordpress.com/advice-on-writing-papers/)

- [Books](https://terrytao.wordpress.com/books/)

- [Mastodon+](https://terrytao.wordpress.com/mastodon-posts/)

- [Applets](https://terrytao.wordpress.com/applets/)

		
			
- [Subscribe to feed](https://terrytao.wordpress.com/feed/)
		
	

	

	
	
		

# A digestion of the Jacobian conjecture counterexample

		

21 July, 2026 in [math.AG](https://terrytao.wordpress.com/category/mathematics/mathag/) | Tags: [Jacobian conjecture](https://terrytao.wordpress.com/tag/jacobian-conjecture/), [polynomials](https://terrytao.wordpress.com/tag/polynomials/) | by [Terence Tao](https://terrytao.wordpress.com/author/teorth/)		
	
	
		

 The notorious [Jacobian conjecture](https://en.wikipedia.org/wiki/Jacobian_conjecture) can be formulated concretely over the complex numbers as follows.

Conjecture 1 (Jacobian Conjecture)  Let  be a polynomial map in  complex variables, whose Jacobian  is a non-zero constant. Then  is invertible (with polynomial inverse). 

The condition that the Jacobian  is non-zero is equivalent to  being locally invertible. (The implication of local invertibility from non-vanishing Jacobian follows from the inverse function theorem; the converse implication can be derived from the [Weierstrass preparation theorem](https://en.wikipedia.org/wiki/Weierstrass_preparation_theorem), but is omitted here; see also Lemma 5 of [this previous blog post](https://terrytao.wordpress.com/2009/03/07/infinite-fields-finite-fields-and-the-ax-grothendieck-theorem/).) Also, from the fundamental theorem of algebra, once the Jacobian polynomial  is non-zero, it must be constant. So the hypothesis “Jacobian  is a non-zero constant” can be replaced with “ is locally invertible”. So the Jacobian conjecture can be viewed as an assertion that local invertibility implies global invertibility. The complex numbers can be easily replaced with other fields of characteristic zero by the [Lefschetz principle](https://en.wikipedia.org/wiki/Algebraic_geometry_and_analytic_geometry#The_Lefschetz_principle), but I prefer to work in the concrete setting of the complex numbers.

It was [recently shown](https://www.newscientist.com/article/2580374-ais-solution-to-87-year-old-riddle-takes-mathematicians-by-surprise/) (using the Fable AI) that the conjecture is false in three dimensions (and thus in higher dimensions as well):

Theorem 2 (Counterexample to conjecture)  There exists a polynomial  which has non-zero constant Jacobian, but is not invertible. 

The conjecture remains open in two dimensions, and is easy to establish in one dimension.

The example can be stated completely explicitly: one can take 

 

 

 and one can verify by a brief calculation that 

 and 

 

 While this is an extremely quick verification, the construction presented in this fashion appears like a massive miracle. The polynomial  has degree seven, so a priori the Jacobian  ought to be a polynomial in three variables of degree as large as , so the fact that all non-constant coefficients of this polynomial vanish looks like a massive cancellation involving  equations, which is much larger than the  degrees of freedom for a generic degree seven polynomial map of three variables. So finding such a polynomial looks highly unlikely to be located by brute force.

The example has since been retroactively [explained in more geometric terms](https://x.com/davikrehalt/status/2079175065695035442). As a “digestion” exercise to myself, I sought to write this explanation with relatively little use of algebraic geometry, in a manner that minimizes the amount of “miracles” required, although there are still a few places where some remarkable phenomena occur.

It is convenient to use the local injectivity formulation, and to generalize the domain  to an equivalent affine variety. Namely, we will show

Theorem 3 (Counterexample, reformulated)  There exists an affine variety  that is isomorphic to  by polynomial changes of variable, and a polynomial map  which is locally injective, but not globally injective. 

Clearly one can get from Theorem [3](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#jac2) to Theorem [2](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#jac1) by composing with the isomorphism  and using the previously mentioned fact that local injectivity implies non-zero constant Jacobian. Our objective is now to find data ,  that obeys three separate properties: 

 
- (a)  is locally injective on . 
- (b)  is not globally injective on . 
- (c)  is isomorphic to  by polynomial changes of variable. 

 The advantage of splitting the problem in to these three components is that we can build towards each of them separately.

(A pedantic remark: strictly speaking, in the arguments below, we not only replace the domain  of  by an equivalent variety , but also replace the range  of  by an equivalent variety . But the equivalence between  and  is a boring linear isomorphism ( will just be a hyperplane in a four-dimensional vector space ), so we do not highlight this aspect of the construction.)

It turns out that  and  can be built out of the operation of multiplication of low degree polynomials. Namely, consider the following three simple affine spaces: 

 
-  The space  of linear homogeneous polynomials  of two complex variables . 
-  The space  of quadratic homogeneous polynomials  of two complex variables . 
-  The space  of cubic homogeneous polynomials  of two complex variables . 

 (The notation  here refers to the  [symmetric power](https://en.wikipedia.org/wiki/Symmetric_power) of a vector space .) Clearly these spaces are isomorphic to  respectively. Furthermore, we have a multiplication map , mapping a pair  of a linear polynomial  and a quadratic polynomial  to a cubic polynomial 

 (Right now, the domain and range of this map  is larger dimensional than the target of three; we will cut the dimensions down to three as the argument progresses.) 

The map , essentially a map from  to , is clearly polynomial; it is given explicitly in coordinates as 

 The map  also enjoys two basic (and commuting) symmetries: 

 
-  If one applies a scaling  for some non-zero complex numbers , then the product  is scaled by : . 
-  If one applies a change of variables  for some invertible linear transformation , then the product  is transformed by : . 

 So this map enjoys a huge amount of equivariance, basically with respect to an action of the five-dimensional group .

The five-dimensional domain  is of course larger than the four-dimensional range , so the map  clearly cannot be injective. This can already be seen from the scaling symmetry, as the specific scalings 

 for  modify the linear and quadratic polynomials  but not their product . But even if one quotients out by this symmetry [(3)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#specific) to cut the dimension of the domain down to four, the map  is still not injective for the following basic reason. A generically chosen cubic polynomial  will split into the product  of three independent linear polynomials. Then there are three pairs 

 which all map to the same cubic polynomial 

 under the multiplication map , but are not related to each other by scaling symmetry [(3)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#specific). Thus, we see that even after quotienting out by the scaling symmetry [(3)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#specific), the multiplication map  is generically non-injective in a three-to-one fashion. Thus we already have achieved something resembling goal (b)!

It will be convenient to “spend” the scaling symmetry  to obtain a useful normalization. If  is a linear polynomial and  is a quadratic polynomial, the (homogeneous) [resultant](https://en.wikipedia.org/wiki/Resultant#Homogeneous_resultant)  can be defined by the determinant 

 If we have a factorization 

 then the resultant can also be described as 

 Thus the resultant measures whether the linear polynomial  and the quadratic polynomial  share a common root. A fundamental fact about resultants is that they are -invariant: for any , we have 

 One way to see this is to check it first for translations  (which translate the roots  by  while leaving  unchanged) and for inversions  (which map  to  while mapping  to  and  respectively), and then noting that these transformations generate all of . They also interact very nicely with scaling: 

 In particular, the scaling symmetry [(3)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#specific) multiplies  by : 

 Thus, we can (generically) normalize away this scaling symmetry by imposing the condition 

We now have a restricted multiplication map (which by abuse of notation we will continue to call ) from the four-dimensional variety 

 to the four-dimensional space . This map  is still not globally injective, as we can take the three pairs in [(4)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#l123) from before and apply the scaling [(3)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#specific) separately to each of the three pairs to obtain the normalization [(7)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#res1). So we have kept property (b). Furthermore, this map retains the -equivariance (and also one remaining scaling symmetry, though we will not make much further use of that symmetry).

But we now also have property (a)! Suppose we want to show the local injectivity of  in the neighborhood of a pair  with . As the resultant is non-vanishing, the root  of  (which exists in the Riemann sphere, or projective line if you prefer) is distinct from the two roots  of  (though the latter two roots could be equal to each other). Applying the  action (which performs Möbius transforms on the roots), one can assume without loss of generality that  is the point at infinity (or equivalently ), thus  for some complex number  and  for some complex numbers , with the resultant condition [(7)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#res1) simplifies to  (so in particular  are also non-zero). It is then clear that if one perturbs  and  by a small amount (say, modifying each coefficient by ), then the root  of  will perturb to something large (), while the roots  of  stay bounded. Thus, just from knowledge of the product , one can reconstruct which of the three roots of this cubic polynomial will be the perturbed root of , and which two will be the perturbed roots of ; from this and [(6)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#scal), [(7)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#res1) we can also reconstruct the leading coefficient  of , and this completely determines both  and . This establishes the local injectivity property (a). (In fact it is [étale](https://en.wikipedia.org/wiki/Formally_%C3%A9tale_morphism), but we will not need the machinery of étale maps here.)

Unfortunately, (the four-dimensional analogue of) condition (c) fails: the quadric hypersurface [(8)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#quad) is not isomorphic to the affine space . But we can try to get around this by passing to a three-dimensional slice. Let  be some three-dimensional affine plane of  (which we will take to avoid the origin for technical reasons), then we can restrict  as a map from the set 

 

 to .  is clearly identifiable (by linear changes of coordinate) to . As  was already locally invertible, it remains locally invertible under restriction; and because generic cubic polynomials  had three preimages under  in [(8)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#quad), this continues to be the case after restricting to [(9)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#quad-v) (unless  was somehow so degenerate that it had no generic elements, but this turns out to be impossible). So we have retained properties (a) and (b). The miracle is that, with a good choice of , we can also obtain (c) and obtain the desired counterexample to the Jacobian conjecture: despite appearances, the variety [(9)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#quad-v) is in fact equivalent to the affine space  by polynomial changes of variable!

Let’s see how. The affine hyperplanes in  avoiding the origin are parameterized by the dual space of  avoiding the origin, which one can think of as the non-zero third order homogeneous differential operators  in two variables. Indeed, every such operator  generates an affine hyperplane  that avoids the origin, and conversely by duality every affine hyperplane avoiding the origin arises in this form uniquely. Just as the cubic polynomials in  can be factored into three linear polynomials, the differential operators in the dual space  can also be factored into three linear differential operators, e.g., 

 in the case that  is non-zero. The  action moves the roots  around the Riemann sphere by Möbius transformations. As these transformations are -transitive, the actual selection of such roots is not too important (and the scaling symmetry similarly makes the choice of leading coefficient  unimportant); the only thing to keep track of is whether the roots repeat. Up to the symmetries, there are in fact just three different equivalence classes of differential operator  (and thus of affine hyperplane ) to consider: 

 
-  Operators where the three roots  are all distinct, thus  for independent first-order operators . 
-  Operators where two roots coincide and one is distinct, thus  for independent first-order operators . 
-  Operators where all three roots coincide, thus  for some first-order operator . 

It turns out that the affine miracle for [(9)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#quad-v) occurs precisely in the second case, when  has two identical roots. I do not have a completely satisfactory geometric explanation for this miracle, but one can verify it by the following coordinate computation.

By applying the  action, we can normalize so that , thus  is now the affine hyperplane of cubic polynomials  with . Using [(2)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#mult) and [(5)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#reslq), the variety [(9)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#quad-v) can now be described explicitly in coordinates as 

 At first glance this seems to be a generic-looking variety cut out by a cubic equation and a quadratic equation – hardly a candidate to be affine! But observe that if  is non-zero, then the second equation  can be solved for , 

 and the first equation  can be solved for , 

 Putting these two equations together, we see that as long as one removes the case , the quintuple  is uniquely determined by  by a change of variables which is Laurent in  and polynomial in . Thus we have a nice birational equivalence 

 

 Thus we have already almost established property (c): the variety [(9)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#quad-v) becomes birationally equivalent to  after cutting out the  subvariety. In particular, for each fixed non-zero value  of , the corresponding fiber 

 of [(10)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#explicit) is equivalent to  by polynomial changes of variable, since we can reconstruct  from the coordinates  by the polynomial formulae 

So we just need to glue back in the  fiber. Indeed, from [(10)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#explicit) we see that the fiber at  is just 

 Now we observe a key miracle: the cubic equation  and quadratic equation  have a unique affine solution  (as opposed to the six possible solutions that Bezout’s theorem might suggest – the other five solutions live on the line at infinity). So the fiber here is also affine: 

 This is extremely encouraging for the purposes of establishing property (c), as it strongly suggests that the variety [(10)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#explicit) has the structure of an -bundle over , which is already extremely close to being isomorphic to the affine space . The main remaining task is to make sure that nothing singular happens in the limit , and that a global polynomial coordinate chart for [(10)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#explicit) that covers both the  and  fibers can be constructed.

The standard way to proceed here is to manipulate various tangent spaces using the modern machinery of algebraic geometry and commutative algebra, but given my own background, I prefer to adopt the language of analysis, and in particular big-O notation (in place of the ideals used in algebraic geometry), in order to investigate the limit  by hand. On the variety [(10)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#explicit), let us use  to denote any multiple of  by a polynomial expression in . Thus, for instance, the equation  implies that 

 while the equation  implies that 

 as well as the more refined estimate 

 In the  case we could conclude that . Now we perturb this observation. Multiplying [(13)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#bc-1) by  we have , which on substitution into [(14)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#bc-2) gives ; substituting this back into either [(13)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#bc-1) or [(14)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#bc-2) also gives .

We can get some more precise asymptotics by also taking advantage of [(15)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#bc-3). Substituting  into [(15)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#bc-3), we obtain after some algebra 

 So if we write  more explicitly as , then we have 

 and thus 

 Substituting this back into [(11)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#d-eq) gives an asymptotic for : 

 

 

 Finally, one can insert these estimates into [(12)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#e-eq), although one only gets a trivial bound in this case: 

 

 

Expanding the  error term in [(16)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#c-eq) as , and doing a little more algebra, we thus have a polynomial change of variables 

 

 

 

 

 which completely parameterizes the variety [(10)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#explicit) by polynomial combinations of three coordinates . This already gives (c) and thus completes the proof of Theorem [3](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#jac2).

The previous computations, when expanded out, also gives polynomial inverse maps: 

 

 

 The map from  to the  coefficients of  (dropping the  coefficient which is constrained to equal ), we obtain a polynomial map 

 with 

 which theory predicts to have a constant Jacobian, and indeed one can calculate that the Jacobian is . This is essentially the original example up to trivial changes of variable; indeed, one can check that the map 

 is exactly the map  given in [(1)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#explicit-ex).

AI disclosure: I [used an AI chatbot](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56) to discuss various aspects of this problem and to confirm several of the calculations made here.

### Share this:

- [Print (Opens in new window)
				Print](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#print?share=print)
- [Email a link to a friend (Opens in new window)
				Email](mailto:?subject=%5BShared%20Post%5D%20A%20digestion%20of%20the%20Jacobian%20conjecture%20counterexample&body=https%3A%2F%2Fterrytao.wordpress.com%2F2026%2F07%2F21%2Fa-digestion-of-the-jacobian-conjecture-counterexample%2F&share=email)
- [More](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#)
- 
- [Share on X (Opens in new window)
				X](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/?share=twitter)
- [Share on Facebook (Opens in new window)
				Facebook](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/?share=facebook)
- [Share on Reddit (Opens in new window)
				Reddit](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/?share=reddit)
- [Share on Pinterest (Opens in new window)
				Pinterest](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/?share=pinterest)
- Like Loading...	
		

### Recent Comments

				
					[Terence Tao](http://www.math.ucla.edu/~tao) on [247B, Notes 1: Restriction…](https://terrytao.wordpress.com/2020/03/29/247b-notes-1-restriction-theory/comment-page-3/#comment-694157)[Terence Tao](http://www.math.ucla.edu/~tao) on [285G, Lecture 0: Riemannian ma…](https://terrytao.wordpress.com/2008/03/26/285g-lecture-0-riemannian-manifolds-and-curvature/comment-page-2/#comment-694156)Anonymous on [Palomar – a registry of…](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/comment-page-1/#comment-694154)Michael M. Ross on [Quantitative bounds for sets l…](https://terrytao.wordpress.com/2026/08/20/quantitative-bounds-for-sets-lacking-polynomial-progressions-with-shifted-prime-difference/comment-page-1/#comment-694152)Huzaifa Mumit on [285G, Lecture 0: Riemannian ma…](https://terrytao.wordpress.com/2008/03/26/285g-lecture-0-riemannian-manifolds-and-curvature/comment-page-2/#comment-694149)Anonymous on [Almost all Collatz orbits atta…](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/comment-page-5/#comment-694148)yfhouag on [247B, Notes 1: Restriction…](https://terrytao.wordpress.com/2020/03/29/247b-notes-1-restriction-theory/comment-page-3/#comment-694147)Anonymous on [Palomar – a registry of…](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/comment-page-1/#comment-694146)[Terence Tao](http://www.math.ucla.edu/~tao) on [Noether’s theorem, and t…](https://terrytao.wordpress.com/2014/03/02/noethers-theorem-and-the-conservation-laws-for-the-euler-equations/comment-page-1/#comment-694145)[Terence Tao](http://www.math.ucla.edu/~tao) on [285G, Lecture 0: Riemannian ma…](https://terrytao.wordpress.com/2008/03/26/285g-lecture-0-riemannian-manifolds-and-curvature/comment-page-2/#comment-694144)[Terence Tao](http://www.math.ucla.edu/~tao) on [Nonlinear dispersive equations…](https://terrytao.wordpress.com/books/nonlinear-dispersive-equations-local-and-global-analysis/comment-page-3/#comment-694143)[Terence Tao](http://www.math.ucla.edu/~tao) on [247B, Notes 1: Restriction…](https://terrytao.wordpress.com/2020/03/29/247b-notes-1-restriction-theory/comment-page-3/#comment-694142)Anonymous on [Nonlinear dispersive equations…](https://terrytao.wordpress.com/books/nonlinear-dispersive-equations-local-and-global-analysis/comment-page-3/#comment-694140)Anonymous on [285G, Lecture 0: Riemannian ma…](https://terrytao.wordpress.com/2008/03/26/285g-lecture-0-riemannian-manifolds-and-curvature/comment-page-2/#comment-694139)Anonymous on [Noether’s theorem, and t…](https://terrytao.wordpress.com/2014/03/02/noethers-theorem-and-the-conservation-laws-for-the-euler-equations/comment-page-1/#comment-694137)				
				
	
		
		
	

### Top Posts

- [Rotating needles in space: the road to the Kakeya conjecture, and why it matters](https://terrytao.wordpress.com/2026/08/25/rotating-needles-in-space-the-road-to-the-kakeya-conjecture-and-why-it-matters/)
- [Career advice](https://terrytao.wordpress.com/career-advice/)
- [Palomar - a registry of Lean verified mathematics](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/)
- [A digestion of the Jacobian conjecture counterexample](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- [A digestion of the proof of Sendov's conjecture](https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/)
- [Books](https://terrytao.wordpress.com/books/)
- [Mathematical Discourse](https://terrytao.wordpress.com/2026/08/22/mathematical-discourse/)
- [Does one have to be a genius to do maths?](https://terrytao.wordpress.com/career-advice/does-one-have-to-be-a-genius-to-do-maths/)
- [On writing](https://terrytao.wordpress.com/advice-on-writing-papers/)
- [Analysis I](https://terrytao.wordpress.com/books/analysis-i/)

### Archives

			
					
- [August 2026](https://terrytao.wordpress.com/2026/08/) (6)
	
- [July 2026](https://terrytao.wordpress.com/2026/07/) (9)
	
- [June 2026](https://terrytao.wordpress.com/2026/06/) (3)
	
- [May 2026](https://terrytao.wordpress.com/2026/05/) (1)
	
- [March 2026](https://terrytao.wordpress.com/2026/03/) (4)
	
- [February 2026](https://terrytao.wordpress.com/2026/02/) (3)
	
- [January 2026](https://terrytao.wordpress.com/2026/01/) (4)
	
- [December 2025](https://terrytao.wordpress.com/2025/12/) (5)
	
- [November 2025](https://terrytao.wordpress.com/2025/11/) (5)
	
- [September 2025](https://terrytao.wordpress.com/2025/09/) (1)
	
- [August 2025](https://terrytao.wordpress.com/2025/08/) (3)
	
- [July 2025](https://terrytao.wordpress.com/2025/07/) (1)
	
- [June 2025](https://terrytao.wordpress.com/2025/06/) (2)
	
- [May 2025](https://terrytao.wordpress.com/2025/05/) (5)
	
- [April 2025](https://terrytao.wordpress.com/2025/04/) (2)
	
- [March 2025](https://terrytao.wordpress.com/2025/03/) (1)
	
- [February 2025](https://terrytao.wordpress.com/2025/02/) (3)
	
- [January 2025](https://terrytao.wordpress.com/2025/01/) (1)
	
- [December 2024](https://terrytao.wordpress.com/2024/12/) (3)
	
- [November 2024](https://terrytao.wordpress.com/2024/11/) (4)
	
- [October 2024](https://terrytao.wordpress.com/2024/10/) (1)
	
- [September 2024](https://terrytao.wordpress.com/2024/09/) (4)
	
- [August 2024](https://terrytao.wordpress.com/2024/08/) (3)
	
- [July 2024](https://terrytao.wordpress.com/2024/07/) (3)
	
- [June 2024](https://terrytao.wordpress.com/2024/06/) (1)
	
- [May 2024](https://terrytao.wordpress.com/2024/05/) (1)
	
- [April 2024](https://terrytao.wordpress.com/2024/04/) (5)
	
- [March 2024](https://terrytao.wordpress.com/2024/03/) (1)
	
- [December 2023](https://terrytao.wordpress.com/2023/12/) (2)
	
- [November 2023](https://terrytao.wordpress.com/2023/11/) (2)
	
- [October 2023](https://terrytao.wordpress.com/2023/10/) (1)
	
- [September 2023](https://terrytao.wordpress.com/2023/09/) (3)
	
- [August 2023](https://terrytao.wordpress.com/2023/08/) (3)
	
- [June 2023](https://terrytao.wordpress.com/2023/06/) (8)
	
- [May 2023](https://terrytao.wordpress.com/2023/05/) (1)
	
- [April 2023](https://terrytao.wordpress.com/2023/04/) (1)
	
- [March 2023](https://terrytao.wordpress.com/2023/03/) (2)
	
- [February 2023](https://terrytao.wordpress.com/2023/02/) (1)
	
- [January 2023](https://terrytao.wordpress.com/2023/01/) (2)
	
- [December 2022](https://terrytao.wordpress.com/2022/12/) (3)
	
- [November 2022](https://terrytao.wordpress.com/2022/11/) (3)
	
- [October 2022](https://terrytao.wordpress.com/2022/10/) (3)
	
- [September 2022](https://terrytao.wordpress.com/2022/09/) (1)
	
- [July 2022](https://terrytao.wordpress.com/2022/07/) (3)
	
- [June 2022](https://terrytao.wordpress.com/2022/06/) (1)
	
- [May 2022](https://terrytao.wordpress.com/2022/05/) (2)
	
- [April 2022](https://terrytao.wordpress.com/2022/04/) (2)
	
- [March 2022](https://terrytao.wordpress.com/2022/03/) (5)
	
- [February 2022](https://terrytao.wordpress.com/2022/02/) (3)
	
- [January 2022](https://terrytao.wordpress.com/2022/01/) (1)
	
- [December 2021](https://terrytao.wordpress.com/2021/12/) (2)
	
- [November 2021](https://terrytao.wordpress.com/2021/11/) (2)
	
- [October 2021](https://terrytao.wordpress.com/2021/10/) (1)
	
- [September 2021](https://terrytao.wordpress.com/2021/09/) (2)
	
- [August 2021](https://terrytao.wordpress.com/2021/08/) (1)
	
- [July 2021](https://terrytao.wordpress.com/2021/07/) (3)
	
- [June 2021](https://terrytao.wordpress.com/2021/06/) (1)
	
- [May 2021](https://terrytao.wordpress.com/2021/05/) (2)
	
- [February 2021](https://terrytao.wordpress.com/2021/02/) (6)
	
- [January 2021](https://terrytao.wordpress.com/2021/01/) (2)
	
- [December 2020](https://terrytao.wordpress.com/2020/12/) (4)
	
- [November 2020](https://terrytao.wordpress.com/2020/11/) (2)
	
- [October 2020](https://terrytao.wordpress.com/2020/10/) (4)
	
- [September 2020](https://terrytao.wordpress.com/2020/09/) (5)
	
- [August 2020](https://terrytao.wordpress.com/2020/08/) (2)
	
- [July 2020](https://terrytao.wordpress.com/2020/07/) (2)
	
- [June 2020](https://terrytao.wordpress.com/2020/06/) (1)
	
- [May 2020](https://terrytao.wordpress.com/2020/05/) (2)
	
- [April 2020](https://terrytao.wordpress.com/2020/04/) (3)
	
- [March 2020](https://terrytao.wordpress.com/2020/03/) (9)
	
- [February 2020](https://terrytao.wordpress.com/2020/02/) (1)
	
- [January 2020](https://terrytao.wordpress.com/2020/01/) (3)
	
- [December 2019](https://terrytao.wordpress.com/2019/12/) (4)
	
- [November 2019](https://terrytao.wordpress.com/2019/11/) (2)
	
- [September 2019](https://terrytao.wordpress.com/2019/09/) (2)
	
- [August 2019](https://terrytao.wordpress.com/2019/08/) (3)
	
- [July 2019](https://terrytao.wordpress.com/2019/07/) (2)
	
- [June 2019](https://terrytao.wordpress.com/2019/06/) (4)
	
- [May 2019](https://terrytao.wordpress.com/2019/05/) (6)
	
- [April 2019](https://terrytao.wordpress.com/2019/04/) (4)
	
- [March 2019](https://terrytao.wordpress.com/2019/03/) (2)
	
- [February 2019](https://terrytao.wordpress.com/2019/02/) (5)
	
- [January 2019](https://terrytao.wordpress.com/2019/01/) (1)
	
- [December 2018](https://terrytao.wordpress.com/2018/12/) (6)
	
- [November 2018](https://terrytao.wordpress.com/2018/11/) (2)
	
- [October 2018](https://terrytao.wordpress.com/2018/10/) (2)
	
- [September 2018](https://terrytao.wordpress.com/2018/09/) (5)
	
- [August 2018](https://terrytao.wordpress.com/2018/08/) (3)
	
- [July 2018](https://terrytao.wordpress.com/2018/07/) (3)
	
- [June 2018](https://terrytao.wordpress.com/2018/06/) (1)
	
- [May 2018](https://terrytao.wordpress.com/2018/05/) (4)
	
- [April 2018](https://terrytao.wordpress.com/2018/04/) (4)
	
- [March 2018](https://terrytao.wordpress.com/2018/03/) (5)
	
- [February 2018](https://terrytao.wordpress.com/2018/02/) (4)
	
- [January 2018](https://terrytao.wordpress.com/2018/01/) (5)
	
- [December 2017](https://terrytao.wordpress.com/2017/12/) (5)
	
- [November 2017](https://terrytao.wordpress.com/2017/11/) (3)
	
- [October 2017](https://terrytao.wordpress.com/2017/10/) (4)
	
- [September 2017](https://terrytao.wordpress.com/2017/09/) (4)
	
- [August 2017](https://terrytao.wordpress.com/2017/08/) (5)
	
- [July 2017](https://terrytao.wordpress.com/2017/07/) (5)
	
- [June 2017](https://terrytao.wordpress.com/2017/06/) (1)
	
- [May 2017](https://terrytao.wordpress.com/2017/05/) (3)
	
- [April 2017](https://terrytao.wordpress.com/2017/04/) (2)
	
- [March 2017](https://terrytao.wordpress.com/2017/03/) (3)
	
- [February 2017](https://terrytao.wordpress.com/2017/02/) (1)
	
- [January 2017](https://terrytao.wordpress.com/2017/01/) (2)
	
- [December 2016](https://terrytao.wordpress.com/2016/12/) (2)
	
- [November 2016](https://terrytao.wordpress.com/2016/11/) (2)
	
- [October 2016](https://terrytao.wordpress.com/2016/10/) (5)
	
- [September 2016](https://terrytao.wordpress.com/2016/09/) (4)
	
- [August 2016](https://terrytao.wordpress.com/2016/08/) (4)
	
- [July 2016](https://terrytao.wordpress.com/2016/07/) (1)
	
- [June 2016](https://terrytao.wordpress.com/2016/06/) (3)
	
- [May 2016](https://terrytao.wordpress.com/2016/05/) (5)
	
- [April 2016](https://terrytao.wordpress.com/2016/04/) (2)
	
- [March 2016](https://terrytao.wordpress.com/2016/03/) (6)
	
- [February 2016](https://terrytao.wordpress.com/2016/02/) (2)
	
- [January 2016](https://terrytao.wordpress.com/2016/01/) (1)
	
- [December 2015](https://terrytao.wordpress.com/2015/12/) (4)
	
- [November 2015](https://terrytao.wordpress.com/2015/11/) (6)
	
- [October 2015](https://terrytao.wordpress.com/2015/10/) (5)
	
- [September 2015](https://terrytao.wordpress.com/2015/09/) (5)
	
- [August 2015](https://terrytao.wordpress.com/2015/08/) (4)
	
- [July 2015](https://terrytao.wordpress.com/2015/07/) (7)
	
- [June 2015](https://terrytao.wordpress.com/2015/06/) (1)
	
- [May 2015](https://terrytao.wordpress.com/2015/05/) (5)
	
- [April 2015](https://terrytao.wordpress.com/2015/04/) (4)
	
- [March 2015](https://terrytao.wordpress.com/2015/03/) (3)
	
- [February 2015](https://terrytao.wordpress.com/2015/02/) (4)
	
- [January 2015](https://terrytao.wordpress.com/2015/01/) (4)
	
- [December 2014](https://terrytao.wordpress.com/2014/12/) (6)
	
- [November 2014](https://terrytao.wordpress.com/2014/11/) (5)
	
- [October 2014](https://terrytao.wordpress.com/2014/10/) (4)
	
- [September 2014](https://terrytao.wordpress.com/2014/09/) (3)
	
- [August 2014](https://terrytao.wordpress.com/2014/08/) (4)
	
- [July 2014](https://terrytao.wordpress.com/2014/07/) (5)
	
- [June 2014](https://terrytao.wordpress.com/2014/06/) (5)
	
- [May 2014](https://terrytao.wordpress.com/2014/05/) (5)
	
- [April 2014](https://terrytao.wordpress.com/2014/04/) (2)
	
- [March 2014](https://terrytao.wordpress.com/2014/03/) (4)
	
- [February 2014](https://terrytao.wordpress.com/2014/02/) (5)
	
- [January 2014](https://terrytao.wordpress.com/2014/01/) (4)
	
- [December 2013](https://terrytao.wordpress.com/2013/12/) (4)
	
- [November 2013](https://terrytao.wordpress.com/2013/11/) (5)
	
- [October 2013](https://terrytao.wordpress.com/2013/10/) (4)
	
- [September 2013](https://terrytao.wordpress.com/2013/09/) (5)
	
- [August 2013](https://terrytao.wordpress.com/2013/08/) (1)
	
- [July 2013](https://terrytao.wordpress.com/2013/07/) (7)
	
- [June 2013](https://terrytao.wordpress.com/2013/06/) (12)
	
- [May 2013](https://terrytao.wordpress.com/2013/05/) (4)
	
- [April 2013](https://terrytao.wordpress.com/2013/04/) (2)
	
- [March 2013](https://terrytao.wordpress.com/2013/03/) (2)
	
- [February 2013](https://terrytao.wordpress.com/2013/02/) (6)
	
- [January 2013](https://terrytao.wordpress.com/2013/01/) (1)
	
- [December 2012](https://terrytao.wordpress.com/2012/12/) (4)
	
- [November 2012](https://terrytao.wordpress.com/2012/11/) (7)
	
- [October 2012](https://terrytao.wordpress.com/2012/10/) (6)
	
- [September 2012](https://terrytao.wordpress.com/2012/09/) (4)
	
- [August 2012](https://terrytao.wordpress.com/2012/08/) (3)
	
- [July 2012](https://terrytao.wordpress.com/2012/07/) (4)
	
- [June 2012](https://terrytao.wordpress.com/2012/06/) (3)
	
- [May 2012](https://terrytao.wordpress.com/2012/05/) (3)
	
- [April 2012](https://terrytao.wordpress.com/2012/04/) (4)
	
- [March 2012](https://terrytao.wordpress.com/2012/03/) (5)
	
- [February 2012](https://terrytao.wordpress.com/2012/02/) (5)
	
- [January 2012](https://terrytao.wordpress.com/2012/01/) (4)
	
- [December 2011](https://terrytao.wordpress.com/2011/12/) (8)
	
- [November 2011](https://terrytao.wordpress.com/2011/11/) (8)
	
- [October 2011](https://terrytao.wordpress.com/2011/10/) (7)
	
- [September 2011](https://terrytao.wordpress.com/2011/09/) (6)
	
- [August 2011](https://terrytao.wordpress.com/2011/08/) (8)
	
- [July 2011](https://terrytao.wordpress.com/2011/07/) (9)
	
- [June 2011](https://terrytao.wordpress.com/2011/06/) (8)
	
- [May 2011](https://terrytao.wordpress.com/2011/05/) (11)
	
- [April 2011](https://terrytao.wordpress.com/2011/04/) (3)
	
- [March 2011](https://terrytao.wordpress.com/2011/03/) (10)
	
- [February 2011](https://terrytao.wordpress.com/2011/02/) (3)
	
- [January 2011](https://terrytao.wordpress.com/2011/01/) (5)
	
- [December 2010](https://terrytao.wordpress.com/2010/12/) (5)
	
- [November 2010](https://terrytao.wordpress.com/2010/11/) (6)
	
- [October 2010](https://terrytao.wordpress.com/2010/10/) (9)
	
- [September 2010](https://terrytao.wordpress.com/2010/09/) (9)
	
- [August 2010](https://terrytao.wordpress.com/2010/08/) (3)
	
- [July 2010](https://terrytao.wordpress.com/2010/07/) (4)
	
- [June 2010](https://terrytao.wordpress.com/2010/06/) (8)
	
- [May 2010](https://terrytao.wordpress.com/2010/05/) (8)
	
- [April 2010](https://terrytao.wordpress.com/2010/04/) (8)
	
- [March 2010](https://terrytao.wordpress.com/2010/03/) (8)
	
- [February 2010](https://terrytao.wordpress.com/2010/02/) (10)
	
- [January 2010](https://terrytao.wordpress.com/2010/01/) (12)
	
- [December 2009](https://terrytao.wordpress.com/2009/12/) (11)
	
- [November 2009](https://terrytao.wordpress.com/2009/11/) (8)
	
- [October 2009](https://terrytao.wordpress.com/2009/10/) (15)
	
- [September 2009](https://terrytao.wordpress.com/2009/09/) (6)
	
- [August 2009](https://terrytao.wordpress.com/2009/08/) (13)
	
- [July 2009](https://terrytao.wordpress.com/2009/07/) (10)
	
- [June 2009](https://terrytao.wordpress.com/2009/06/) (11)
	
- [May 2009](https://terrytao.wordpress.com/2009/05/) (9)
	
- [April 2009](https://terrytao.wordpress.com/2009/04/) (11)
	
- [March 2009](https://terrytao.wordpress.com/2009/03/) (14)
	
- [February 2009](https://terrytao.wordpress.com/2009/02/) (13)
	
- [January 2009](https://terrytao.wordpress.com/2009/01/) (18)
	
- [December 2008](https://terrytao.wordpress.com/2008/12/) (8)
	
- [November 2008](https://terrytao.wordpress.com/2008/11/) (9)
	
- [October 2008](https://terrytao.wordpress.com/2008/10/) (10)
	
- [September 2008](https://terrytao.wordpress.com/2008/09/) (5)
	
- [August 2008](https://terrytao.wordpress.com/2008/08/) (6)
	
- [July 2008](https://terrytao.wordpress.com/2008/07/) (7)
	
- [June 2008](https://terrytao.wordpress.com/2008/06/) (8)
	
- [May 2008](https://terrytao.wordpress.com/2008/05/) (11)
	
- [April 2008](https://terrytao.wordpress.com/2008/04/) (12)
	
- [March 2008](https://terrytao.wordpress.com/2008/03/) (12)
	
- [February 2008](https://terrytao.wordpress.com/2008/02/) (13)
	
- [January 2008](https://terrytao.wordpress.com/2008/01/) (17)
	
- [December 2007](https://terrytao.wordpress.com/2007/12/) (10)
	
- [November 2007](https://terrytao.wordpress.com/2007/11/) (9)
	
- [October 2007](https://terrytao.wordpress.com/2007/10/) (9)
	
- [September 2007](https://terrytao.wordpress.com/2007/09/) (7)
	
- [August 2007](https://terrytao.wordpress.com/2007/08/) (9)
	
- [July 2007](https://terrytao.wordpress.com/2007/07/) (9)
	
- [June 2007](https://terrytao.wordpress.com/2007/06/) (6)
	
- [May 2007](https://terrytao.wordpress.com/2007/05/) (10)
	
- [April 2007](https://terrytao.wordpress.com/2007/04/) (11)
	
- [March 2007](https://terrytao.wordpress.com/2007/03/) (9)
	
- [February 2007](https://terrytao.wordpress.com/2007/02/) (4)
			

			

### Categories

			
					
- [expository](https://terrytao.wordpress.com/category/expository/) (327)

	
- [tricks](https://terrytao.wordpress.com/category/expository/tricks/) (13)

	
- [guest blog](https://terrytao.wordpress.com/category/guest-blog/) (10)

	
- [Mathematics](https://terrytao.wordpress.com/category/mathematics/) (926)

	
- [math.AC](https://terrytao.wordpress.com/category/mathematics/mathac/) (9)

	
- [math.AG](https://terrytao.wordpress.com/category/mathematics/mathag/) (43)

	
- [math.AP](https://terrytao.wordpress.com/category/mathematics/mathap/) (115)

	
- [math.AT](https://terrytao.wordpress.com/category/mathematics/mathat/) (17)

	
- [math.CA](https://terrytao.wordpress.com/category/mathematics/mathca/) (199)

	
- [math.CO](https://terrytao.wordpress.com/category/mathematics/mathco/) (207)

	
- [math.CT](https://terrytao.wordpress.com/category/mathematics/mathct/) (9)

	
- [math.CV](https://terrytao.wordpress.com/category/mathematics/mathcv/) (40)

	
- [math.DG](https://terrytao.wordpress.com/category/mathematics/mathdg/) (37)

	
- [math.DS](https://terrytao.wordpress.com/category/mathematics/mathds/) (90)

	
- [math.FA](https://terrytao.wordpress.com/category/mathematics/mathfa/) (24)

	
- [math.GM](https://terrytao.wordpress.com/category/mathematics/mathgm/) (16)

	
- [math.GN](https://terrytao.wordpress.com/category/mathematics/mathgn/) (21)

	
- [math.GR](https://terrytao.wordpress.com/category/mathematics/mathgr/) (90)

	
- [math.GT](https://terrytao.wordpress.com/category/mathematics/mathgt/) (17)

	
- [math.HO](https://terrytao.wordpress.com/category/mathematics/mathho/) (14)

	
- [math.IT](https://terrytao.wordpress.com/category/mathematics/mathit/) (13)

	
- [math.LO](https://terrytao.wordpress.com/category/mathematics/mathlo/) (54)

	
- [math.MG](https://terrytao.wordpress.com/category/mathematics/mathmg/) (48)

	
- [math.MP](https://terrytao.wordpress.com/category/mathematics/mathmp/) (31)

	
- [math.NA](https://terrytao.wordpress.com/category/mathematics/mathna/) (26)

	
- [math.NT](https://terrytao.wordpress.com/category/mathematics/mathnt/) (214)

	
- [math.OA](https://terrytao.wordpress.com/category/mathematics/mathoa/) (22)

	
- [math.PR](https://terrytao.wordpress.com/category/mathematics/mathpr/) (114)

	
- [math.QA](https://terrytao.wordpress.com/category/mathematics/mathqa/) (6)

	
- [math.RA](https://terrytao.wordpress.com/category/mathematics/mathra/) (49)

	
- [math.RT](https://terrytao.wordpress.com/category/mathematics/mathrt/) (21)

	
- [math.SG](https://terrytao.wordpress.com/category/mathematics/mathsg/) (4)

	
- [math.SP](https://terrytao.wordpress.com/category/mathematics/mathsp/) (48)

	
- [math.ST](https://terrytao.wordpress.com/category/mathematics/mathst/) (11)

	
- [non-technical](https://terrytao.wordpress.com/category/non-technical/) (214)

	
- [admin](https://terrytao.wordpress.com/category/non-technical/admin/) (49)

	
- [advertising](https://terrytao.wordpress.com/category/non-technical/advertising/) (83)

	
- [diversions](https://terrytao.wordpress.com/category/non-technical/diversions-non-technical/) (7)

	
- [media](https://terrytao.wordpress.com/category/non-technical/media/) (15)
	
	
- [journals](https://terrytao.wordpress.com/category/non-technical/media/journals/) (4)

	

	
- [obituary](https://terrytao.wordpress.com/category/non-technical/obituary/) (15)

	
- [opinion](https://terrytao.wordpress.com/category/opinion/) (37)

	
- [paper](https://terrytao.wordpress.com/category/paper/) (273)

	
- [book](https://terrytao.wordpress.com/category/paper/book/) (23)

	
- [Companion](https://terrytao.wordpress.com/category/paper/companion/) (13)

	
- [update](https://terrytao.wordpress.com/category/paper/update/) (26)

	
- [question](https://terrytao.wordpress.com/category/question/) (128)

	
- [polymath](https://terrytao.wordpress.com/category/question/polymath/) (87)

	
- [talk](https://terrytao.wordpress.com/category/talk/) (69)

	
- [DLS](https://terrytao.wordpress.com/category/talk/dls/) (20)

	
- [teaching](https://terrytao.wordpress.com/category/teaching/) (190)

	
- [245A – Real analysis](https://terrytao.wordpress.com/category/teaching/245a-real-analysis/) (11)

	
- [245B – Real analysis](https://terrytao.wordpress.com/category/teaching/245b-real-analysis/) (22)

	
- [245C – Real analysis](https://terrytao.wordpress.com/category/teaching/245c-real-analysis/) (6)

	
- [246A – complex analysis](https://terrytao.wordpress.com/category/teaching/246a-complex-analysis/) (11)

	
- [246B – complex analysis](https://terrytao.wordpress.com/category/teaching/246b-complex-analysis/) (5)

	
- [246C – complex analysis](https://terrytao.wordpress.com/category/teaching/246c-complex-analysis/) (5)

	
- [247B – Classical Fourier Analysis](https://terrytao.wordpress.com/category/teaching/247b-classical-fourier-analysis/) (5)

	
- [254A – analytic prime number theory](https://terrytao.wordpress.com/category/teaching/254a-analytic-prime-number-theory/) (19)

	
- [254A – ergodic theory](https://terrytao.wordpress.com/category/teaching/254a-ergodic-theory/) (18)

	
- [254A – Hilbert's fifth problem](https://terrytao.wordpress.com/category/teaching/254a-hilberts-fifth-problem/) (12)

	
- [254A – Incompressible fluid equations](https://terrytao.wordpress.com/category/teaching/254a-incompressible-fluid-equations/) (5)

	
- [254A – random matrices](https://terrytao.wordpress.com/category/teaching/254a-random-matrices/) (14)

	
- [254B – expansion in groups](https://terrytao.wordpress.com/category/teaching/254b-expansion-in-groups/) (8)

	
- [254B – Higher order Fourier analysis](https://terrytao.wordpress.com/category/teaching/254b-higher-order-fourier-analysis/) (9)

	
- [255B – incompressible Euler equations](https://terrytao.wordpress.com/category/teaching/255b-incompressible-euler-equations/) (2)

	
- [275A – probability theory](https://terrytao.wordpress.com/category/teaching/275a-probability-theory/) (6)

	
- [285G – poincare conjecture](https://terrytao.wordpress.com/category/teaching/285g-poincare-conjecture/) (20)

	
- [Logic reading seminar](https://terrytao.wordpress.com/category/teaching/logic-reading-seminar/) (8)

	
- [The sciences](https://terrytao.wordpress.com/category/the-sciences/) (1)

	
- [travel](https://terrytao.wordpress.com/category/travel/) (26)

			

			

### 

[additive combinatorics](https://terrytao.wordpress.com/tag/additive-combinatorics/)
[approximate groups](https://terrytao.wordpress.com/tag/approximate-groups/)
[arithmetic progressions](https://terrytao.wordpress.com/tag/arithmetic-progressions/)
[Artificial Intelligence](https://terrytao.wordpress.com/tag/artificial-intelligence/)
[Ben Green](https://terrytao.wordpress.com/tag/ben-green/)
[Cauchy-Schwarz](https://terrytao.wordpress.com/tag/cauchy-schwarz/)
[Cayley graphs](https://terrytao.wordpress.com/tag/cayley-graphs/)
[central limit theorem](https://terrytao.wordpress.com/tag/central-limit-theorem/)
[Chowla conjecture](https://terrytao.wordpress.com/tag/chowla-conjecture/)
[compressed sensing](https://terrytao.wordpress.com/tag/compressed-sensing/)
[correspondence principle](https://terrytao.wordpress.com/tag/correspondence-principle/)
[cosmic distance ladder](https://terrytao.wordpress.com/tag/cosmic-distance-ladder/)
[distributions](https://terrytao.wordpress.com/tag/distributions/)
[divisor function](https://terrytao.wordpress.com/tag/divisor-function/)
[eigenvalues](https://terrytao.wordpress.com/tag/eigenvalues/)
[Elias Stein](https://terrytao.wordpress.com/tag/elias-stein/)
[Emmanuel Breuillard](https://terrytao.wordpress.com/tag/emmanuel-breuillard/)
[entropy](https://terrytao.wordpress.com/tag/entropy/)
[equidistribution](https://terrytao.wordpress.com/tag/equidistribution/)
[Erdos](https://terrytao.wordpress.com/tag/erdos/)
[ergodic theory](https://terrytao.wordpress.com/tag/ergodic-theory/)
[Euler equations](https://terrytao.wordpress.com/tag/euler-equations/)
[exponential sums](https://terrytao.wordpress.com/tag/exponential-sums/)
[finite fields](https://terrytao.wordpress.com/tag/finite-fields/)
[Fourier transform](https://terrytao.wordpress.com/tag/fourier-transform/)
[Freiman's theorem](https://terrytao.wordpress.com/tag/freimans-theorem/)
[Gowers uniformity norm](https://terrytao.wordpress.com/tag/gowers-uniformity-norm/)
[Gowers uniformity norms](https://terrytao.wordpress.com/tag/gowers-uniformity-norms/)
[graph theory](https://terrytao.wordpress.com/tag/graph-theory/)
[Gromov's theorem](https://terrytao.wordpress.com/tag/gromovs-theorem/)
[GUE](https://terrytao.wordpress.com/tag/gue/)
[Hilbert's fifth problem](https://terrytao.wordpress.com/tag/hilberts-fifth-problem/)
[ICM](https://terrytao.wordpress.com/tag/icm/)
[incompressible Euler equations](https://terrytao.wordpress.com/tag/incompressible-euler-equations/)
[inverse conjecture](https://terrytao.wordpress.com/tag/inverse-conjecture/)
[Joni Teravainen](https://terrytao.wordpress.com/tag/joni-teravainen/)
[Kaisa Matomaki](https://terrytao.wordpress.com/tag/kaisa-matomaki/)
[Kakeya conjecture](https://terrytao.wordpress.com/tag/kakeya-conjecture/)
[Lie algebras](https://terrytao.wordpress.com/tag/lie-algebras/)
[Lie groups](https://terrytao.wordpress.com/tag/lie-groups/)
[Liouville function](https://terrytao.wordpress.com/tag/liouville-function/)
[Littlewood-Offord problem](https://terrytao.wordpress.com/tag/littlewood-offord-problem/)
[Maksym Radziwill](https://terrytao.wordpress.com/tag/maksym-radziwill/)
[Mobius function](https://terrytao.wordpress.com/tag/mobius-function/)
[Navier-Stokes equations](https://terrytao.wordpress.com/tag/navier-stokes-equations/)
[nilpotent groups](https://terrytao.wordpress.com/tag/nilpotent-groups/)
[nilsequences](https://terrytao.wordpress.com/tag/nilsequences/)
[nonstandard analysis](https://terrytao.wordpress.com/tag/nonstandard-analysis/)
[Paul Erdos](https://terrytao.wordpress.com/tag/paul-erdos/)
[politics](https://terrytao.wordpress.com/tag/politics/)
[polymath1](https://terrytao.wordpress.com/tag/polymath1/)
[polymath8](https://terrytao.wordpress.com/tag/polymath8/)
[Polymath15](https://terrytao.wordpress.com/tag/polymath15/)
[polynomial method](https://terrytao.wordpress.com/tag/polynomial-method/)
[polynomials](https://terrytao.wordpress.com/tag/polynomials/)
[prime gaps](https://terrytao.wordpress.com/tag/prime-gaps/)
[prime numbers](https://terrytao.wordpress.com/tag/prime-numbers/)
[prime number theorem](https://terrytao.wordpress.com/tag/prime-number-theorem/)
[random matrices](https://terrytao.wordpress.com/tag/random-matrices/)
[randomness](https://terrytao.wordpress.com/tag/randomness/)
[Ratner's theorem](https://terrytao.wordpress.com/tag/ratners-theorem/)
[regularity lemma](https://terrytao.wordpress.com/tag/regularity-lemma/)
[Ricci flow](https://terrytao.wordpress.com/tag/ricci-flow/)
[Riemann zeta function](https://terrytao.wordpress.com/tag/riemann-zeta-function/)
[Schrodinger equation](https://terrytao.wordpress.com/tag/schrodinger-equation/)
[Shannon entropy](https://terrytao.wordpress.com/tag/shannon-entropy/)
[sieve theory](https://terrytao.wordpress.com/tag/sieve-theory/)
[structure](https://terrytao.wordpress.com/tag/structure/)
[Szemeredi's theorem](https://terrytao.wordpress.com/tag/szemeredis-theorem/)
[Tamar Ziegler](https://terrytao.wordpress.com/tag/tamar-ziegler/)
[ultrafilters](https://terrytao.wordpress.com/tag/ultrafilters/)
[universality](https://terrytao.wordpress.com/tag/universality/)
[Van Vu](https://terrytao.wordpress.com/tag/van-vu/)
[wave maps](https://terrytao.wordpress.com/tag/wave-maps/)
[Yitang Zhang](https://terrytao.wordpress.com/tag/yitang-zhang/)

###  [The Polymath Blog](https://polymathprojects.org)

- [Polymath News and AI](https://polymathprojects.org/2026/04/03/polymath-news-and-ai/)
- [Polymath projects 2021](https://polymathprojects.org/2021/02/20/polymath-projects-2021/)
- [A sort of Polymath on a famous MathOverflow problem](https://polymathprojects.org/2019/06/09/a-sort-of-polymath-on-a-famous-mathoverflow-problem/)
- [Ten Years of Polymath](https://polymathprojects.org/2019/02/03/ten-years-of-polymath/)
- [Updates and Pictures](https://polymathprojects.org/2018/10/19/updates-and-pictures/)
- [Polymath proposal: finding simpler unit distance graphs of chromatic number 5](https://polymathprojects.org/2018/04/10/polymath-proposal-finding-simpler-unit-distance-graphs-of-chromatic-number-5/)
- [A new polymath proposal (related to the Riemann Hypothesis) over Tao’s blog](https://polymathprojects.org/2018/01/26/a-new-polymath-proposal-related-to-the-riemann-hypothesis-over-taos-blog/)
- [Spontaneous Polymath 14 – A success!](https://polymathprojects.org/2018/01/26/spontaneous-polymath-14-a-success/)
- [Polymath 13 – a success!](https://polymathprojects.org/2017/08/22/polymath-13-a-success/)
- [Non-transitive Dice over Gowers’s Blog](https://polymathprojects.org/2017/05/15/non-transitive-dice-over-gowerss-blog/)

	
		
			

## 158 comments

			

[Comments feed for this article](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/feed/)
		

	
		
	
		
			

[27 July, 2026 at 11:22 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693681)
			

[Roland](http://rolandglueck.de/)
					

		
						

Right before the introduction of the resultant, the definition of  seems to be missing. Otherwise, thanks for the post!

[Corrected, thanks -T.]
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693681#respond)		
	
	
	
		
			

[27 July, 2026 at 2:11 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693684)
			

Anonymous
					

		
						

The provenance question comes up a lot in this thread… for what it’s worth, this is currently tracked as “pending peer review,” not fully verified, at openconjectures.org/c/kill-jacobian-2026, credited to Claude Fable 5 with Levent Alpöge. Worth checking back once (if) it clears formal review rather than treating Tao’s writeup as the verification step itself.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693684#respond)		
	

	
	
		
			

[28 July, 2026 at 10:22 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693690)
			

Anonymous
					

		
						

It is credited to Levent Alpöge, with Claude Fable 5 (Anthropic), not vice versa. Anyone with high school math competence can verify the counterexample.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693690#respond)		
	

	
	
		
			

[27 July, 2026 at 6:53 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693687)
			

[정동우](http://www.makonea.com)
					

		
						

My question is about how you use AI rather than about the mathematics itself.

I could follow parts of your discussion of the Jacobian counterexample, and I was particularly interested in the way you moved between different representations of the problem. For example, you considered restrictions such as (c_2=1), hyperplane sections, and a fixed resultant level set. My impression was that the resultant condition removed a scaling degree of freedom and reduced the complexity of the problem.

From the conversation, I inferred a workflow roughly like this:

Define the problem and identify the invariants that must be preserved.

Generate several nearby representations or modeling hypotheses.

Systematically perturb and test those models by looking for counterexamples, equivalent formulations, special cases, and hidden structure.

Prefer models that explain more with fewer assumptions and make the calculations shorter.

Translate the resulting structure back into the original formulation and verify it there.

As a programmer, I was tempted to describe the third step as a kind of domain-specific semantic fuzzing or metamorphic testing: instead of inserting random program inputs, one varies the representation of the problem while checking that certain relationships and invariants remain intact.

I may be overinterpreting a single conversation, but I am interested in extracting a general workflow that could be applied outside mathematics as well. When you use GPT for research, is this broadly similar to your usual approach, or was this conversation atypical?

I realize this is a personal and somewhat meta-level question, so please do not feel any obligation to reply. I am simply trying to understand what it takes to use AI as effectively as you do.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693687#respond)		
	
	
	
		
			

[28 July, 2026 at 11:32 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693692)
			

kittenspeedyfa57a3f9ea
					

		
						

A mechanical Bass–Connell–Wright reduction of Alpöge’s ℂ³ counterexample, yielding a cubic Keller map of ℂ¹⁹ that is 3-to-1 over a point. Worked out and verified with Claude (Fable 5). 

 [https://rhicksrad.github.io/jacobian-degree3/](https://rhicksrad.github.io/jacobian-degree3/)
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693692#respond)		
	

	
	
		
			

[29 July, 2026 at 7:04 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693697)
			

Anonymous
					

		
						

there’s something special about the natural number two that causes it to behave differently than natural numbers greater than two for a whole bunch of conjectures. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693697#respond)		
	

	
	
		
			

[29 July, 2026 at 5:13 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693695)
			

Anonymous
					

		
						

“the conjecture is false in three dimensions (and thus in higher dimensions as well)”

Why is this implication true? Could anyone give me a link or quick explanation? Sorry if this is a dumb question.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693695#respond)		
	

	
	
		
			

[29 July, 2026 at 9:33 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693704)
			

[Terence Tao](http://www.math.ucla.edu/~tao)
					

		
						

Lemma 3.1 of [the preprint mentioned in a recent comment](https://arxiv.org/abs/2607.22198) establishes this implication, which is a simple matter of adding dummy variables to one’s polynomial.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693704#respond)		
	

	
	
		
			

[29 July, 2026 at 5:43 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693696)
			

Anonymous
					

		
						

I am a mathematician and not at all an expert on AI. I guess Alpöge has not been the first to ask AI about Jacobi’s conjecture.  Do we know how did he get an answer? What prompt did he ask? Any specific training for the AI? How much did the AI work on his prompt?  
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693696#respond)		
	
	
	
		
			

[29 July, 2026 at 7:11 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693698)
			

Christopher
					

		
						

Suggestion: the link for resultant should be changed to [https://en.wikipedia.org/wiki/Resultant#Homogeneous_resultant](https://en.wikipedia.org/wiki/Resultant#Homogeneous_resultant)

[Updated, thanks – T.]
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693698#respond)		
	
	
	
		
			

[29 July, 2026 at 7:13 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693699)
			

Anonymous
					

		
						

There’s another route to proving the Jacobian conjecture in two dimensions, and that is by proving the Hessian conjecture in four dimensions:

[https://arxiv.org/abs/2607.22198](https://arxiv.org/abs/2607.22198)
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693699#respond)		
	
	
	
		
			

[29 July, 2026 at 7:52 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693701)
			

Christopher
					

		
						

Hmm, for equation (16), is the derivation that using the analytic definition c = 1 – 3ay/2 + O(a^2), but then since we know that c is a polynomial from c = 1 + O(a), than O(a^2) must also be a polynomial?
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693701#respond)		
	

	
	
		
			

[29 July, 2026 at 9:24 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693702)
			

[Terence Tao](http://www.math.ucla.edu/~tao)
					

		
						

No analysis (in particular, no Neumann series or Taylor series) is used here; the big-O notation is meant to evoke analytic intuition, but has an algebraic interpretation.  Because we already know that , the  term can be simplified to , and the  term can similarly be simplified to .
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693702#respond)		
	

	
	
		
			

[29 July, 2026 at 9:41 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693705)
			

Anonymous
					

		
						

Contrary to all the hype, the Jacobian conjecture counterexample is not that exciting because it relies on techniques established by Vitushkin in his 1999 paper. So there really is nothing new here. The only thing different is that here it’s applied to three dimensions and one gets a polynomial map, whereas in two dimensions one only gets a rational map. 

If it were a human being who came up with this counterexample instead of a large language model, it’ll just be a writeup in Quanta Magazine, and then people move on because the techniques used in the proof aren’t new or that interesting, and the two dimensional case was always the more interesting one to algebraic geometers and still did not get resolved. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693705#respond)		
	

	
	
		
			

[30 July, 2026 at 5:51 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693711)
			

Anonymous
					

		
						

The hype for the Jacobian conjecture counterexample is because Abhyankar and Moh made the conjecture famous in the 1970s and 1980s among mathematicians in academia. It has nothing to do with AI. Any human being who came up with the counterexample will be made instantly famous for disproving a famous conjecture. 

You’re going to have to go back in time and stop Abhyankar and Moh from popularizing the Jacobian conjecture if you don’t want hype for disproving the Jacobian conjecture. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693711#respond)		
	

	
	
		
			

[30 July, 2026 at 11:12 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693726)
			

Anonymous
					

		
						

But the fact is, when Abhyankar and Moh named “Jacobian conjecture” in the 1970-80s, they only referred to the 2-dimensional version. When such a conjecture is named, it really requires many positive results and strong evidence; this is only satisfied for 2D version. The higher dimensional generalization is only one extension of problem to see what’s possibly true and what’s not. But later some other mathematicians named the n-version “Jacobian conjecture” is kind of misleading, just like some named the n-version “Dixmier conjecture”, while Dixmier primarily focused on .
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693726#respond)		
	

	
	
		
			

[31 July, 2026 at 6:24 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693732)
			

[Terence Tao](http://www.math.ucla.edu/~tao)
					

		
						

I don’t think that, prior to 2026, there was any consensus as to whether the planar Jacobian conjecture or the general dimensional Jacobian conjecture was the more “fundamental” one.  To give four data points to complement the writings of Abhyankar and Moh:

-  In 1998, Steven Smale listed the general dimensional conjecture as Problem #16 on his high-profile [list of “problems for the next century”](http://smaleinstitute.com/Mathematical_problems_for_the_next_century.pdf), explicitly calling it “The Jacobian Conjecture”. In his own words, he holds “a belief that the question, its solution, partial results or even attempts at its solution are likely to have great importance for mathematics and its               development in the next century.”.  His commentary around this problem (see page 19) only discusses the general dimensional case, and does not even mention the planar case at all as worthy of any particular attention.

-  The [last version of the Wikipedia page on the conjecture before the counterexample discovery, dated 29 June 2026](https://en.wikipedia.org/w/index.php?title=Jacobian_conjecture&oldid=1361627214), does (in my opinion) a reasonable job of approximating what the conventional wisdom towards the conjecture was at that moment; the two-dimensional case is mentioned and discussed, but does not have a central role, and the conjecture is formally stated in general dimension. (However, it is noted on that page that the two-dimensional conjecture was claimed (with a flawed proof) by Kraus in 1884, launching a very long line of failed proofs of this conjecture.)

-  I myself briefly mentioned the Jacobian conjecture in a [blog post from 2009](https://terrytao.wordpress.com/2009/03/07/infinite-fields-finite-fields-and-the-ax-grothendieck-theorem/); at the time, I had no impression that the  case was of any particular significance. In particular, the result of Rudin discussed in that post that an injective polynomial map was automatically bijective with polynomial inverse works in all dimensions, and serves perhaps as a weak hint that the Jacobian conjecture is most naturally phrased in the general dimensional setting.

-  In the [original 1938 paper of Keller](https://link.springer.com/article/10.1007/BF01695502), the conjecture is already formulated in all dimensions (contrary to some later accounts of this paper, which are in error), although he does single out the two-dimensional case as already being difficult. On page 301, Keller writes “die Frage, ob Polynome mit der Funktionaldeterminante 1 sich stets durch Polyhome umkehren lassen … mir scheint die Frage eine Untersuchung sehr zu lohnen, sie scheint jedoch bereits im ebenen Fall sehr schwierig zu sein.”  (“the question of whether polynomials with a functional determinant of 1 can always be inverted by polynomials … it seems to me that this question is very worth investigating, however, it already seems to be very difficult in the planar case.”)

In hindsight, we now know that the planar Jacobian conjecture is the more interesting question, but to say that this was the accepted conventional wisdom before 2026 is not strongly supported by the historical record.  I think the most honest assessment one can make is the planar problem and the general-dimensional problem were both considered to be of interest, though individual mathematicians might choose to focus on one of the questions over the other.  In retrospect it would probably have been a good idea to give these two conjectures slightly different names rather than calling them both “the Jacobian conjecture”, but going forward one can easily make a distinction between the (still open) planar Jacobian conjecture and the (now disproven) general-dimensional Jacobian conjecture.

An analogy might be with the Riemann hypothesis.  When Riemann first introduced the hypothesis, it was solely about the Riemann zeta function.  Over time, the hypothesis was generalized far beyond Riemann’s original intent, first to Dirichlet L-functions, then to Dedekind L-functions, and to many other L-functions besides.  Similar to the situation with Rudin’s theorem, many of the partial or auxiliary results around RH tend to have analogues for GRH (though often with more technical difficulty in the proofs). Is there a current consensus as to which of RH and GRH is “more important”?  As a thought experiment, suppose that in a few years an advanced AI discovers a way to construct an L-function that serves as a counterexample to GRH.  Would this be considered a significant result?  Or would the reaction be that it was “misleading” to talk about the generalized Riemann hypothesis at all, and that one should only be discussing Riemann’s original form of the hypothesis, rather than the now falsified generalizations introduced by “some other mathematicians”?

The Kakeya conjecture is another prominent example of a problem that was first posed in the plane in its original formulation, but subsequently became generalized to higher dimensions.  In this case, it was the higher-dimensional case that turned out to be far more interesting.  So one cannot always use the original historical formulation as a definitive ruling on what the most natural formulation of a problem is.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693732#respond)		
	

	
	
		
			

[31 July, 2026 at 7:28 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693733)
			

Anonymous
					

		
						

The earliest appearance of this problem was in 1884 by Kraus, who focused on 2D. Keller’s work on general dimension problem was well-known, but all these false proofs before 1970s by Kraus, Segre, Gröbner, Engel and after that, the failed attempt during doctoral study by Yitang Zhang, wrong proofs by Amel’kin, Yucai Su focused on 2D. I do not oppose that the n-dimensional problem is and was important. I said 2D is central because disproving 2D automatically implies disproving the n-D version, as tried by Vitushkin; and proving 2D almost leads to the highest honor in math. Because of this, Abhyankar, Moh, and Vitushkin focused on 2D so hard that they did much less on higher dimensions and people only said “almost no evidence supports the higher dimension claim”, even without tries on finding counter examples (except for Moh who did a bit computation but even didn’t check if the algorithm was correct or not). Later people tend to higher dimensional case and equivalent formulations (conjectures) largely because it’s just so desperate to prove the 2D Jacobian conjecture directly, and people tend to produce more works on this topic. I agree that the new counter example is still an important achievement, but just one of these works in the long history of its reseach, even together with a few wrong proofs (which still contain correct lemmas). But clearly the claim by media and companies “the Jacobian conjecture was resolved” is highly misleading.
		
		
						
	
	
	
		
			

[31 July, 2026 at 7:58 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693736)
			

[Terence Tao](http://www.math.ucla.edu/~tao)
					

		
						

The wording I would use here is that the AI-generated example resolves one, but not both, of the two commonly accepted versions of the Jacobian conjecture.  For instance, it resolves the version of the Jacobian conjecture as stated by Smale’s Problem #16 (with this explicit name), by Keller (though he calls it “die Frage [nach] Polynome mit der Funktionaldeterminante 1” rather than “the Jacobian conjecture”), or by Wikipedia as of June 2026.
		
		
						
	
	
	
		
			

[31 July, 2026 at 7:43 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693734)
			

dutifullyb3c31ab42c
					

		
						

I agree that mathematicians are truly free to make conjectures, at least in the before-AI ages, even without calculating any examples, because the mathematical world knows how to evaluate the works. But now I’m just afraid that the AI companies manipulate the public opinion so much that the evaluation system by mathematicians is affected and even mathematicians are misled (of course mathematicians even in algebraic geometry are not familiar with all subfields). Previously I see that even some people put the JC wiki page under the “Anthropic” category, like it’s their property. (Categories surve to mark the defining characteristics rather than tags). Later someone reverts the edit, but it seems the people opposing this change are the minority on Wiki page.
		
		
						
	
	
	
		
			

[31 July, 2026 at 8:23 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693738)
			

dutifullyb3c31ab42c
					

		
						

I’m not sure if Smale really meant this “universal Jacobian conjecture”, as he didn’t say “for any n” or “let n be…”. In the literature, the Jacobian conjecture is very commonly indexed by dimensions. So now we are playing games of words, but for sure the media reports have led to large misleading, for instance many said “the AI disproved Jacobian conjecture” and then said “this problem indirectly led to Yitang Zhang’s years of working odd jobs to survive”. I wish the media reports could be more clear on this, while it seems just hopeless, like maybe after a few days or years, even if someone proves the 2D Jacobian conjecture, he or she will not obtain the deserved honor and Anthropic will be on top of them for this.  
		
		
						
	
	
	
		
			

[31 July, 2026 at 10:40 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693741)
			

[Terence Tao](http://www.math.ucla.edu/~tao)
					

		
						

I can’t find any interpretation of Smale’s formulation of problem 16 that indicates that he was particularly interested in any specific value of n, such as n=2, rather than asking the question for arbitrary n.  This can be contrasted with his discussion of problem 2 (the Poincare conjecture), which he formulates for arbitrary n, but has a detailed discussion of specific values of n, in particular highlighting the n=3 case as being the primary case to consider for this problem.  It is also worth noting that none of the other problems on Smale’s list appears to be parameterized by any sort of dimensional parameter, so there appears to be no reason to assume that such a parameterization is secretly in effect just for this problem. (As explicitly noted on the first page of the paper, he is seeking questions “with a yes or no answer”, which to me strongly suggests that he is not introducing any additional parameters to these problems.)

In fact, it is notable that for Problems 2, 5, 6, 7, and 15 the dimension is explicitly fixed to a numerical constant to arrive at a “yes or no” question even though these questions also make sense in other dimensions, but for Problem 16 (and also Problem 12) he pointedly refuses to do so (though for Problem 12 he does isolate the case of a 2-sphere as a key special case).

Also, his problem 18 (limits of intelligence) is surprisingly relevant in the current context.
		
		
						
	
	
	
		
			

[31 July, 2026 at 11:31 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693742)
			

dutifullyb3c31ab42c
					

		
						

But the reference he used, the work by van den Essen wrote clearly “the cases of dimension two and that of dimension bigger than two are
essentially different” on the first page, and labeled the Jacobian conjecture as “JC(n)” on the second page. Anyway, as wrote by Smale on the first page, the question were mainly collected but not asked by him. The statement of the Jacobian conjecture was quite varying at that period, and it makes more sense that mathematicians were in general interested in what we can get instead of whether or not it holds for every n. Would they regard the problem not important if it’s proved to hold only for 2D (to be proved)? I suspect so. Btw, I do not mean to criticize the people who made JC “general for all n”. But one fact is, in the 1980s (even up to 2 months before), the base to support the JC_n (n>=3) is not mature (people in recent 30 years frequently said almost no evidence supports it). Probably because of  those positive results of 2D, people didn’t realize there were huge differences for dimensions at that time, and jumped a bit fast. On the contrary, coherent theory of L-functions, strong analogies across different families, the Weil conjectures proved by Deligne, and extensive computations strongly support GRH. This makes both proving and disproving super striking.
		
		
						
	
	
	
		
			

[31 July, 2026 at 12:10 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693744)
			

[Terence Tao](http://www.math.ucla.edu/~tao)
					

		
						

In that referenced paper of van Essen, any reference to “the Jacobian conjecture” without any qualifier on  (e.g., in the conclusions of Proposition 1.5, Theorem 1.6, or Theorem 1.7) clearly is in reference to the general dimension Jacobian conjecture.  This is even more clear in another [1997 paper of van Essen](https://seminariomatematico.polito.it/rendiconti/cartaceo/55-4/283.pdf), in which again the default interpretation of the Jacobian conjecture is taken to be the general dimensional one, starting with the first line of the abstract “there is no good reason to believe that the Jacobian conjecture holds” (whilst in the body of the article he makes it abundantly clear that there is quite strong evidence that the planar Jacobian conjecture (which is referred to using terms such as “the Jacobian conjecture for “) is true).

Again, I think the only honest reading here is that both forms of the Jacobian conjecture were considered of interest prior to 2026.  As the 1997 paper of van Essen shows, there was more evidence in favor of the planar Jacobian conjecture than the general conjecture, but not overwhelmingly so (cf., the “62.4% verdict” that the general Jacobian conjecture (which van Essen simply calls “the Jacobian conjecture”) is false at the end of the article).  I also find it noteworthy that while the 1997 van Essen paper is unusually opinionated for a mathematical research publication, and goes to great lengths to distinguish the planar Jacobian conjecture from the general Jacobian conjecture, even in this paper no opinion is given as to which of the two forms of the Jacobian conjecture is more interesting to study (or which one is more important to resolve). In particular, the de facto status of the general dimensional Jacobian conjecture as the “default” interpretation of that conjecture is not contested by that article.
		
		
						
	
	
	
		
			

[31 July, 2026 at 12:01 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693743)
			

dutifullyb3c31ab42c
					

		
						

And of course even for a conjecture one has no positive results on it, one can still assume it fails/holds and have some results. But when generalizing some previous conjecture, one always needs to be cautious and try to avoid the same name for different problems. This happens in the case of Dixmier’s conjecture. After generalizing to , it’s good to call it “generalized Dixmier conjecture”, but sometimes if people ignore the “generalized”, then a problem arises. People say “Dixmier conjecture is wrong”, but Dixmier’s formulation is on , which remains open. 

Btw, there is another “Generalized Jacobian Conjecture” established by Miyanishi from the aspect of affine algebraic geometry, in which he described the generalized Jacobian conjecture more like a condition for an algebraic variety instead of a universal statement, because he stated the conjection and at the same time provided counter examples.
		
		
						
	
	
	
		
			

[31 July, 2026 at 2:11 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693749)
			

dutifullyb3c31ab42c
					

		
						

The “yes or no” clearly means not some ambiguous statement like “what is the xxxx”? For instance, when someone mentions about Kakeya conjecture, in case someone in future disproves some higher dimensional case, would he think the importance of 3D proof weaker? That would be ridiculous. (FYI, I’m working on analysis). Also, the second problem is not a good example for your argument. Smale is clearly an expert of Poincaré conjecture, and the only open case for Top was 3d at that time. For the problems 6, 10, 11, 13, they in fact support my claim that “when Smale didn’t write clearly ‘for any xx'”, he means these are parameters and the cases are important to distinguish for different parameters. For 16, the reason why he didn’t write claims for different n is not only he isn’t an expert in this field, but also that there were just no yes or no results for nontrivial dimensions available at that time. Your understanding that “he pointedly refuses to do so” lacks support. Finally, for the paper van den Essen, I’d like to point out that 62.4% reflects people’s attitude, but the differences in evidence were indeed overwhelming: he wrote explicitly “there is an overwhelming evidence for the 2 dim JC”, and “no good reason to believe the (universal) Jacobian conjecture”, and “enormous contrast between the 2-dimensional case and the cases n>=3”. Btw, it’s obvious that people working on this field have preferences over 2D or higher dimensional JC (maybe this difference results from almost nothing to break through in 2D from their point of view). Abhyankar, Moh, Vitushkin, Lih-Chung Wang, Heitmann, Yitang Zhang (in the past), Tráng, Hochster, Formanek, etc. clearly focused on 2D, and Bass, Connell, Wright, van den Essen, Wenhua Zhao, etc. clearly focused on general dimensional case (or even the universal case). This clearly explains why van den Essen mentions JC(n) and at the same time work on the universal conjecture (which was proved to be false).
		
		
						
	
	
	
		
			

[1 August, 2026 at 11:54 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693754)
			

Anonymous
					

		
						

RE: Wikipedia. 

A Wikipedia user named D.Lazard just undid all the distinguishing between the 2D and the general case in the article: 

[https://en.wikipedia.org/w/index.php?title=Jacobian_conjecture&diff=prev&oldid=1367187138](https://en.wikipedia.org/w/index.php?title=Jacobian_conjecture&diff=prev&oldid=1367187138)

Looks like Abhyankar and Moh and the proponents of “Jacobian conjecture” to refer to the 2D case just lost the war on Wikipedia. The Jacobian conjecture just refers to the general n dimensional case according to Wikipedia now. 
		
		
						
	
	
	
		
			

[2 August, 2026 at 6:50 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693766)
			

Anonymous
					

		
						

All that the Wikipedia editors did was move that information to a new history section. The last paragraph of that section explicitly says that the two dimensional conjecture was “especially well studied” and that mathematicians like Abhyankar and Moh used “Jacobian conjecture” to refer to the 2D problem. Think that’s a win for the people who think the 2D problem was more important historically than the general nD problem. 
		
		
						
	
	
	
		
			

[2 August, 2026 at 7:45 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693768)
			

Anonymous
					

		
						

“Abhyankar and Moh and the proponents of “Jacobian conjecture” to refer to the 2D case”

That war over the proper usage of “Jacobian conjecture” was lost in 1998 when Moh started mentioning higher dimensions in his formulating of the Jacobian conjecture. Abhyankar is dead. The only people left fighting that war are clueless math students who seem stuck in the 1970s and haven’t gotten themselves acquainted with the recent literature on the topic where the authors always mention that the Jacobian conjecture is parameterized by dimension. 
		
		
						
	
	
	
		
			

[8 August, 2026 at 10:42 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693856)
			

Anonymous
					

		
						

“The last paragraph of that section explicitly says that the two dimensional conjecture was “especially well studied””

The Wikipedia article might state that in the history section, but the results section on the two dimensional case is just a paragraph on that people have ruled out counterexamples to the conjecture up to degree 108 or something. Where are all the other results in two dimensions if the two dimensional conjecture is “especially well studied”? 

Compare with the n dimensional case where there are over a dozen paragraphs in the results section for the general n dimensional case. 
		
		
						
	
	
	
		
			

[14 August, 2026 at 11:47 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693931)
			

Anonymous
					

		
						

Wikipedia is having a huge debate over whether the ‘Jacobian conjecture’ simpliciter is disproved or not:

[https://en.wikipedia.org/wiki/Talk:Jacobian_conjecture#Categories](https://en.wikipedia.org/wiki/Talk:Jacobian_conjecture#Categories)
		
		
						
	

	
	
		
			

[31 July, 2026 at 1:45 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693748)
			

Anonymous
					

		
						

The first published use of the term “Jacobian conjecture” was by Masayoshi Miyanishi in 1973 and referred to the general n dimensional case. Abhyankar and Moh only started publishing their stuff on the 2D Jacobian conjecture in the later half of the 1970s. 

So, Abhyankar and Moh should be the ones to be blamed for confusing things and making “Jacobian conjecture” refer to the two dimensional case, when “Jacobian conjecture” was originally used for the n dimensional case. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693748#respond)		
	

	
	
		
			

[2 August, 2026 at 11:29 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693770)
			

Anonymous
					

		
						

There’re no absolute rules on “determining the name by the first published existence”. There are some examples of naming by unpublished works, e.g. Frobenius coin problem and Gauss–Lucas theorem (Gauss part). I think history will judge this fairly (in case the mathematical community or humans still exist at that time). In case the 2D case is proved, then this will be highly striking and its importance will greatly surpass the general-dimension version, unless people find all possible counter-examples. But for now, it’s fair to index the JC by dimensions and say “n-variable Jacobian conjecture”, not the universal one that claims “for all n”.
		
		
						
	
	
	
		
			

[2 August, 2026 at 12:34 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693772)
			

Anonymous
					

		
						

Abhyankar and Moh should be blamed for not publishing a paper in the late 1960s and early 1970s. They started using the word “Jacobian conjecture” for the two dimensional conjecture privately amongst themselves after Oscar Zariski told them sometime in the 1960s that the conjecture was still unnamed. Had they published a paper back then, then it would have been in official public publication before the n dimensional conjecture shills got their hands on “Jacobian conjecture”, and then the n dimensional conjecture shills would have had to instead use a different name like “generalized Jacobian conjecture” or something similar. 
		
		
						
	
	
	
		
			

[2 August, 2026 at 5:00 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693773)
			

Anonymous
					

		
						

Moh himself is a “n dimensional conjecture shill” then because in his 1998 paper he defined the Jacobian conjecture parameterized by n. 
		
		
						
	
	
	
		
			

[3 August, 2026 at 6:21 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693779)
			

Anonymous
					

		
						

Moh said in response to the discovery of the three dimensional counterexample that he always only ever cared about the two dimensional conjecture; how does that make him a “n dimensional conjecture shill”?
		
		
						
	
	
	
		
			

[4 August, 2026 at 12:18 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693789)
			

Anonymous
					

		
						

Because the original commenter says that anybody who defines Jacobian conjecture in terms of n dimensions is an “n dimensional conjecture shill”. Which I think is extremely dumb. 

I’m trying to point out to the original commenter that even Moh who is famous for working only on the two dimension version defines the Jacobian conjecture in n dimensions these days, but seems like there are three people who disagree with me for some reason because they downvoted my comment. 
		
		
						
	

	
	
		
			

[30 July, 2026 at 6:07 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693715)
			

Anonymous
					

		
						

The actual technique is “Construct a space with a marked factor, then forget the mark” according to a mathematician on twitter (forgot who it was). 

What’s actually new is that thanks to the AI hype, mathematicians are now applying the technique to other conjectures that aren’t the Jacobian conjecture and disproving them. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693715#respond)		
	
	
	
		
			

[30 July, 2026 at 12:46 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693720)
			

Anonymous
					

		
						

Probably a bit extreme but the general idea is correct. People concentrated on 2D because it’s the most attractive (with too many wrong proofs) and disproving it leads to disproving all dimensions. The latter is considered by Vitushkin, who clearly focused on finding the obstruction for an easy 2D counter example without caring about 3D or higher. JC is a great treasure, and it should really belong to someone who prove $JC_2$ (probably in hundreds of years), and the recent work is just one step out of the very long history of research on it. However, Anthropic clearly used any ways of advertising to claim that “[they resolved JC](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)“, with a Wiki link, and then immediately someone added the Wiki article to categories “Anthropic”, “2026 AI”, like the JC is their propery. I’m so afraid that major mathematicians forget that the core problem is $JC_2$, in which case it means that the history has been distorted.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693720#respond)		
	
	
	
		
			

[1 August, 2026 at 7:41 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693759)
			

Anonymous
					

		
						

People are moving on from the Jacobian conjecture in the real world because AI is too busy proving too many theorems. Connes rigidity conjecture and the construction of non-soric groups are far more impressive results than the Jacobian conjecture. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693759#respond)		
	

	
	
		
			

[2 August, 2026 at 9:48 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693769)
			

Anonymous
					

		
						

Connes rigidity conjecture and non-sofic groups don’t have the drama over which version of the Jacobian conjecture is supposed to be the main version of the Jacobian conjecture. People will debate endlessly over whether the two dimensional or the n dimensional Jacobian conjecture is more important and not move on.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693769#respond)		
	

	
	
		
			

[2 August, 2026 at 5:26 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693774)
			

Anonymous
					

		
						

With the n dimensional version solved for n > 2, I think it’s fair to say that the two dimensional version has won the battle and is now the more important version going forwards, and so the debate is over and people will move on. 

Now as for the historical importance, I don’t think most people care about that issue, just as most people don’t care about the history of mathematics more broadly. Mathematicians are largely here to prove theorems, not contemplate about the historical and social factors behind what makes certain conjectures famous and notable. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693774#respond)		
	
	
	
		
			

[4 August, 2026 at 6:33 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693785)
			

Anonymous
					

		
						

The construction of a non-sofic group is just a clever application of two results derived by Gabor Kun and Andreas Thom in two separate papers:

[https://mathoverflow.net/a/513885](https://mathoverflow.net/a/513885)

So it’s like the Jacobian conjecture counterexample in that it relies on previous papers by humans. Once again, something that Quanta Magazine would write about in an article if a human found this non-sofic group, but nothing too earth shattering to warrant all this hype. Andreas Thom himself said at the bottom of his post that he was looking for such a mechanism when the AI beat him to it. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693785#respond)		
	

	
	
		
			

[2 August, 2026 at 12:02 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693771)
			

Anonymous
					

		
						

I agree. These results seem to be more interesting than the 3D or higher dimensional Jacobian conjectures
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693771#respond)		
	
	
	
		
			

[4 August, 2026 at 6:50 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693786)
			

Anonymous
					

		
						

Soficity is also not that important in group theory compared to some other more general properties of groups, just like how the multidimensional Jacobian conjecture is not that interesting compared to the two-dimensional Jacobian conjecture. More interesting would be constructing a non-hyperlinear group because it would refute Connes’ embedding problem. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693786#respond)		
	

	
	
		
			

[7 August, 2026 at 7:07 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693841)
			

Anonymous
					

		
						

Conjectures don’t lie in a vacuum. They have consequences on the truth or falsehood of other conjectures, and people care about the implications on the other conjectures. 

So there are many algebraic geometers who do care about how the Jacobian conjecture being falsified impacts for instance the Diximer conjecture or the Hessian conjecture or the weak Markus–Yamabe conjecture. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693841#respond)		
	
	
	
		
			

[8 August, 2026 at 10:33 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693855)
			

Anonymous
					

		
						

The proof approaches for the two dimensional Jacobian conjecture have a lot to do with low dimensional topology and singularity theory, so is significantly different from the proof approach for the Jacobian conjecture in more than two dimensions. 

The whole field of low dimensional topology is due to the fact that lower dimensions behave differently than higher dimensions so it shouldn’t be surprising that resolving the Jacobian conjecture in low dimensions requires different techniques than resolving the Jacobian conjecture in higher dimensions. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693855#respond)		
	

	
	
		
			

[29 July, 2026 at 10:37 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693706)
			

[Some thoughts about Anthropic’s new cryptanalysis results – A Few Thoughts on Cryptographic Engineering](https://www.recentic.net/some-thoughts-about-anthropics-new-cryptanalysis-results/)
					

		
						

[…] probably notice that many of the exciting recent mathematical results have had this flavor: they either include a machine-checkable proof of a […]
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693706#respond)		
	
	
	
		
			

[30 July, 2026 at 5:54 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693712)
			

Christopher
					

		
						

Instead of guessing which of the three options we should go with, is there a way we could’ve solved for (f,g,h,i) that gives the right affine plane? Like come up with an equation that tells you when (f,g,h,i) satisfies theorem 3? Of course based on the reasoning that followed their would be many solutions (any case the operator has two identical roots) but showing such an equation has at least one solution let’s you jump to theorem 3 with no guessing needed!
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693712#respond)		
	
	
	
		
			

[30 July, 2026 at 9:08 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693717)
			

info 19tet
					

		
						

Does this mean we can come up with arbitrary other counterexamples, maybe families of counterexamples? Where has the goalpost moved?
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693717#respond)		
	

	
	
		
			

[31 July, 2026 at 12:47 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693747)
			

Anonymous
					

		
						

The goalpost has moved to solving the 2D version of the conjecture. Many people argue that the Jacobian conjecture always was about the 2D version and that this 3D counterexample is irrelevant since it doesn’t affect the status of the 2D version. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693747#respond)		
	

	
	
		
			

[30 July, 2026 at 5:05 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693724)
			

Anonymous
					

		
						

Provenance, since it matters for how much to trust the above: the computations and the write-up were done by Claude (Anthropic) in a working session, and I am posting them rather than vouching for them personally. All of it is machine-checkable and I am happy to share the scripts. If any of this is already in the thread and I have missed it, apologies for the noise.

Regarding the remark that there is no completely satisfactory geometric explanation for why only the repeated-root hyperplane class works — here is a computation that may add something, though parts of it are probably known to Will Sawin already. Following his observation that on fixing the marked point `(u:v)` both the hyperplane `H` and the ramification divisor `R` cut out *lines* in the `(a:b:c)`-plane, one can descend. Let `E ⊂ O^3` be the rank-two subbundle spanned by the two line-forms. As `μ_p` is linear and `λ_p` quadratic in the marked point, there is a bundle map `O(-1) ⊕ O(-2) → O^3` with image `E`, and evaluating at the base point gives `O^3 ↠ O(3-s)`, where `s` is the number of marked points at which the two lines coincide. Hence `deg E = s – 3`. Writing `B` for the projectivised pencil minus the two sections, `U → B` is an `A^1`-bundle and `#U = q·#B`. Then: – `s = 1` (the `2+1` class): the map drops rank once, `deg E = -2`, and since `E ⊇ O(-1)` with no degree-zero sub-line-bundle (a fixed linear form would have to lie in every pencil), `E ≅ O(-1)^2`, so `P(E) = F_0`. This is exactly Sawin’s trivialisation, and the two sections meet once, giving `B ≅ A^2`. – `s = 0` (the `1+1+1` class): the map is fibrewise injective and degrees agree, so `E ≅ O(-1) ⊕ O(-2)` and `P(E) = F_1`. The sections are disjoint, so `B` is `F_1` minus the zero and infinity sections of a degree-one line bundle, i.e. `B ≅ A^2 ∖ {0}`. So `B` fails to be `A^2` by exactly one point, and the collision in the repeated-root case is what fills that point in; multiplied by the `A^1` fibre this is precisely the `q` points separating `q^3 – q` from `q^3`. In the `1+1+1` case `U` is a non-trivial `A^1`-torsor over `A^2∖{0}` with affine total space, the same shape as `{xz + yw = 1} → A^2∖{0}`. The reason I think this is worth mentioning: the divisor-class criterion from the Secret Blogging Seminar thread has been read in a few places as *the* explanation, and it cannot be. For `2+1` and `1+1+1` the data on `U` is identical — `H` irreducible, two prime divisors removed, classes `(2,1)` and `(1,1)`, unimodular, so `Cl(U) = 0` with constant units — yet the second has `q^3 – q` points. Descending does not rescue it either: both give `Cl(B) = 0` with only constant units, since `A^2∖{0}` is the standard example of a variety passing both tests without being affine space, or affine at all. The criterion accounts cleanly for the reducible (`3`) class, and for `d ≥ 4` and `|a-b| ≠ 1`, but the `2+1` vs `1+1+1` distinction sits in its blind spot at both levels. What separates them is `F_0` versus `F_1`. The invariant is the expected one: the discriminant of the apolar quadratic equals the discriminant of the dual cubic as a polynomial identity, and `s ≥ 1` forces it to vanish (each pairwise resultant of the three cubics cutting out the collision carries the discriminant as a factor). Caveats. The `A^1`-bundle structure and the closed count `#B = q^2 – 1 + s` were verified exhaustively over `F_q` for small `q` rather than derived in general; the degree and splitting computations above are symbolic. Point counts are of course necessary-only, and the affineness in the `2+1` case is your Theorem, not reproved here — the descent just gives `B ≅ A^2` and then triviality of `A^1`-torsors over `A^2`. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693724#respond)		
	
	
	
		
			

[31 July, 2026 at 12:28 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693745)
			

David Fillmore
					

		
						

The Alpoge-Fable map appears to be angular momentum addition in disguise via the Majorana stellar representation of spin.  Briefly –

- A pure spin state can be written as a completely symmetric collection of spin-one-half spinors

- Their projective rays are identified as “stars” on the sphere – Bloch, Riemann, or Celestial, depending on your preferred interpretation (quantum, complex-geometric, or relativistic); the number of stars is twice the spin, and coincident stars record repeated factors

- A linear binary form is a spin-one-half state with one star; a quadratic is a spin-one state with two stars; a cubic is a spin-three-halves state with three stars. See Penrose & Rindler I, Proposition (3.5.18), pp. 162–163

- Tao’s reconstruction encodes each input as the spin-one-half factor together with the spin-one factor: one distinguished star plus an unordered pair. The factor dictionary is P&R I, Proposition (3.5.18), p. 162.

- Multiplication is the completely symmetric, highest-spin part of adding spin one-half to spin one. It joins the single star to the pair and produces the three-star spin-three-halves constellation. See P&R I, equations (3.5.19)–(3.5.21), p. 162.

- The output retains the constellation but forgets which star came from the spin-one-half factor. A generic triple therefore has three possible preimages.

		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693745#respond)		
	
	
	
		
			

[1 August, 2026 at 9:30 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693753)
			

Anonymous
					

		
						

[Provenance: computations and write-up by Claude (Anthropic) in a working session; I am posting rather than personally vouching. Everything below is machine-verified and checkable in minutes with sympy; scripts available on request.] Three findings related to the July 30 comment above: The intrinsic invariant requested there exists at all degrees . For , the Grothendieck-ring class depends only on the maximal root multiplicity  of the dual binary form of : it equals  for ,  for , and  for root type . Hence  iff  with type : in every degree, the counterexample’s slice is the only affine-space slice. The mechanism does not descend to the plane through any slice so far tested. In the chart ,  with , , , , write  for the  coefficients of  (then ). One has the exact identities  and  with . These lead to machine-certified proofs that no fiber of any linear, -only, or  target coordinate is ; sample check: on  the function  is a nonconstant unit (the ideal  is the unit ideal). Since an  coordinate-fiber would give a degree-3 etale, hence Keller, self-map of the plane, these are conditional planar-JC statements. Still open: coordinates mixing  nonlinearly with . Cheapest check:  is already 3-to-1 on real points; the cubic  (roots ) has three real marked factorizations with , in exact rational arithmetic.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693753#respond)		
	
	
	
		
			

[1 August, 2026 at 8:03 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693760)
			

Anonymous
					

		
						

Small remark: The phrase “a candidate to be affine” would usually refer to being an affine variety, not isomorphic to an affine space.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693760#respond)		
	
	
	
		
			

[2 August, 2026 at 6:22 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693777)
			

Anonymous
					

		
						

Dear Professor Tao,Thanks for your blog posts. I didn’t know about the Jacobian conjecture previously. I believe the string method could be used to produce the counterexample also.Dr Hayes 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693777#respond)		
	
	
	
		
			

[3 August, 2026 at 7:09 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693783)
			

Anonymous
					

		
						

I found a way to derive more counterexample maps from the map posted by Alpöge, even complex coefficient ones, the idea is simple! While the components of these maps have more terms, one question that could be an important endeavor for mathematicians, is whether the original map posted by Alpöge is the minimal structure map that is a counterexample to the JC. 

I’m also focused on the intriguing 1 + xy, to me it is the backbone of the counterexample. Still thinking … I need to discover the idea, then give it to mathematicians to do wonders with it.

I’m a physicist by the way, I find this problem simple enough to understand but challenging enough to promote creativity.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693783#respond)		
	
	
	
		
			

[4 August, 2026 at 1:27 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693793)
			

darkmeerkat276d789e38
					

		
						

Thanks to Professor Tao for the blog post where I learned the first counterexample. I worked with Claude Fable 5 to generalize the example to higher dimensions. The outcome is a paper posted at
[https://arxiv.org/abs/2608.00222](https://arxiv.org/abs/2608.00222)
which gives a general construction (based on parametrized hypersurfaces) for counterexamples in every dimension greater than two and, in each dimension, of arbitrarily large geometric degree.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693793#respond)		
	
	
	
		
			

[4 August, 2026 at 7:22 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693795)
			

Anonymous
					

		
						

How does one express polynomial maps on an n-dimensional vector space and the Jacobian determinant of a polynomial map in a coordinate-free manner?
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693795#respond)		
	

	
	
		
			

[5 August, 2026 at 12:35 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693803)
			

[Terence Tao](http://www.math.ucla.edu/~tao)
					

		
						

There are a number of ways to do this.  From an analysis point of view, one can view a degree  polynomial map  on a vector space to be any smooth map whose  derivative  vanishes (this can be defined in a coordinate-free manner), and the Jacobian is the multiplier of the action of  on volume forms.  Algebraically, I think these maps can be described in the homogeneous setting as  (the formula gets a bit trickier in the inhomogeneous case), but perhaps there is a cleaner way to describe it.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693803#respond)		
	

	
	
		
			

[4 August, 2026 at 8:08 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693796)
			

[Christian Oppel](http://www.qspire-algebra.com)
					

		
						

Excellent article. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693796#respond)		
	
	
	
		
			

[5 August, 2026 at 1:49 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693804)
			

Anonymous
					

		
						

Kossivi Adjamagbo’s separable Jacobian conjecture for positive characteristic fields just got disproven for all dimensions n > 1:

[https://arxiv.org/abs/2607.20968](https://arxiv.org/abs/2607.20968)

[https://arxiv.org/abs/2608.02634](https://arxiv.org/abs/2608.02634)
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693804#respond)		
	

	
	
		
			

[6 August, 2026 at 11:55 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693824)
			

[David Speyer](http://www.math.lsa.umich.edu/~speyer)
					

		
						

The first observation about passing to characteristic 2, dimension 3, has been recorded elsewhere; see Timothy Chow [https://mathoverflow.net/a/513393/297](https://mathoverflow.net/a/513393/297) and N8Programs [https://xcancel.com/N8Programs/status/2079061392649302185](https://xcancel.com/N8Programs/status/2079061392649302185) . That said, I am in favor of results being recorded in clearly written versions posted to repositories like the arXiv, so good for Irit Huq-Kuruvilla for putting in the work.

And here is a reward for Huq-Kuruvilla’s work — the two dimensional case in characteristic two! That’s really exciting. Maybe we’ll see the two dimensional case in some other characteristics soon!
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693824#respond)		
	

	
	
		
			

[7 August, 2026 at 6:00 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693840)
			

Anonymous
					

		
						

The weak Markus–Yamabe conjecture in algebraic geometry is refuted as a result of the Jacobian conjecture counterexampe:

[https://arxiv.org/abs/2608.05392](https://arxiv.org/abs/2608.05392)
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693840#respond)		
	
	
	
		
			

[7 August, 2026 at 9:31 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693844)
			

Michael M. Ross
					

		
						

In the (1,2) case with one cut, the two classes other than (2,1) can be ruled out directly: for (3) the cut reads ac = 1, so a is a nonconstant unit on V and V is not affine space of any dimension; for (1,1,1) decomposing by a gives χ(V) = 0 ≠ 1 = χ(ℂ³). This can be extended to Sym¹ × Sym^k with any number of cuts, where the same Euler characteristic argument gives χ(V) = (k−1)N and hence forces k = 2. Two notes and verification code: [https://github.com/michaelmross/jacobian](https://github.com/michaelmross/jacobian)
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693844#respond)		
	

	
	
		
			

[8 August, 2026 at 7:10 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693852)
			

Anonymous
					

		
						

The extension to multiplication of a linear polynomial by a degree k polynomial to yield a degree k + 1 polynomial is important as it makes it clear why k = 2 is the only valid option here and why k = 1 (Vitushkin’s idea) or k > 2 doesn’t work. 
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693852#respond)		
	

	
	
		
			

[9 August, 2026 at 12:10 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693870)
			

Michael M. Ross
					

		
						

Thanks. I didn’t know about Vitushkin’s paper. Looks like his 2D construction produces a rational map with the 1/s fraction, while k = 2 produces a genuine polynomial one.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693870#respond)		
	

	
	
		
			

[8 August, 2026 at 11:08 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693857)
			

Anonymous
					

		
						

The Jacobian conjecture after July 2026 will be like the Poincaré conjecture after Smale’s 1961 proof of the Poincaré conjecture for n > 4 and Freedman’s 1982 proof of the Poincaré conjecture for n = 3. 

People will end up using “Jacobian conjecture” to refer to only the two dimensional Jacobian conjecture, just like they used “Poincaré conjecture” to refer to only the three dimensional Poincaré conjecture after 1982.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693857#respond)		
	

	
	
		
			

[9 August, 2026 at 1:21 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693862)
			

dutifullyb3c31ab42c
					

		
						

The case seems to be different. In the literature, the Poincaré conjecture mostly only referred to the 3D version, even before Smale’s proof, because people suspected the higher-dimensional version at that time. But I agree that the conventions on the names can change, depending on what the major mathematicians in this field think of.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693862#respond)		
	
	
	
		
			

[25 August, 2026 at 11:13 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-694102)
			

Anonymous
					

		
						

Freedman’s 1982 proof of the Poincaré conjecture for n = 4.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=694102#respond)		
	

	
	
		
			

[12 August, 2026 at 2:22 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693885)
			

Anonymous
					

		
						

This article from Towards Data Science by a CS professor explains the counter example in simple terms that are mostly easy to understand for non-mathematicians: [https://towardsdatascience.com/a-simplified-view-of-the-jacobian-conjecture/](https://towardsdatascience.com/a-simplified-view-of-the-jacobian-conjecture/)
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693885#respond)		
	
	
	
		
			

[13 August, 2026 at 6:59 am](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693899)
			

Anonymous
					

		
						

The 2D Jacobian conjecture should really be considered a problem in low dimensional topology. What’s so special about the Euclidean plane vs higher dimensions that Keller maps seem to behave differently on the Euclidean plane?
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693899#respond)		
	

	
	
		
			

[15 August, 2026 at 7:52 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693950)
			

Anonymous
					

		
						

Apparently Moh is retired now and so is no longer working on the Jacobian conjecture:

[https://en.wikipedia.org/wiki/Talk:Jacobian_conjecture#Results_in_the_2D_Jacobian_conjecture](https://en.wikipedia.org/wiki/Talk:Jacobian_conjecture#Results_in_the_2D_Jacobian_conjecture)
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693950#respond)		
	

	
	
		
			

[18 August, 2026 at 3:06 pm](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/#comment-693968)
			

Anonymous
					

		
						

i don’t understand a single thing but wow math is cool.
		
		
				[Reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-2/?replytocom=693968#respond)		
	

	
		[« Older Comments](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comments)
		
	

	

		
		

### Leave a comment [Cancel reply](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#respond)

			
			

Δ
	
	

	

	

	

### For commenters

			

To enter in LaTeX in comments, use $latex <Your LaTeX code>$ (without the < and > signs, of course; in fact, these signs should be avoided as they can cause formatting errors). Also, backslashes \ need to be doubled as \\.  See the [about page](https://terrytao.wordpress.com/about/) for details and for other commenting policy.

		
	

	

	
		
							[« Two more apps: visualizing the zeta process and the motions of the heavens](https://terrytao.wordpress.com/2026/07/16/two-more-apps-visualizing-the-zeta-process-and-the-motions-of-the-heavens/)
			[A partial digestion of the HRT counterexample »](https://terrytao.wordpress.com/2026/08/06/a-partial-digestion-of-the-hrt-counterexample/)
				
	

	
		
			

[Blog at WordPress.com.](https://wordpress.com/?ref=footer_blog)Ben Eastaugh and Chris Sternal-Johnson. 
		
		
			

[Subscribe to feed.](https://terrytao.wordpress.com/feed/)
		
	

	

		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
								
- 
						[Comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/#comments)
					
									
- 
						Reblog
					
									
- 
								Subscribe
		Subscribed
							
							
							
															
											
- 
			[What's new](https://terrytao.wordpress.com)
		
										
									
																						Join 12,361 other subscribers
																					
										
										
										
										
										
										
																				
											
												Sign me up											
										
									
									
- 
										
											Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fterrytao.wordpress.com%2F2026%2F07%2F21%2Fa-digestion-of-the-jacobian-conjecture-counterexample%2F&signup_flow=account)										
									
								
															
						
					
							
- 
								
					
					
						
								
- 
			[What's new](https://terrytao.wordpress.com)
		
								
- 
										Subscribe
		Subscribed
								
														
- [Sign up](https://wordpress.com/start/)
							
- [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fterrytao.wordpress.com%2F2026%2F07%2F21%2Fa-digestion-of-the-jacobian-conjecture-counterexample%2F&signup_flow=account)
																
- 
										[Copy shortlink](https://wp.me/p3qzP-4FN)
									
																
- 
									[Report this content](https://wordpress.com/abuse/?report_url=https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
								
															
- 
									[View post in Reader](https://wordpress.com/reader/blogs/817149/posts/17967)
								
															
- 
									[Manage subscriptions](https://subscribe.wordpress.com/)
								
																
- Collapse this bar
														
					
				
			
		
	
	

	
	
						
	

	
	%d
