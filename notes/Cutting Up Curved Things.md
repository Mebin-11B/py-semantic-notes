---
title: "Cutting Up Curved Things"
url: https://campedersen.com/tessellation
clipped: 2026-06-17 01:51:31
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Cutting Up Curved Things](https://campedersen.com/tessellation)

## Digest Summary
GPU rendering is limited to triangles, so any curved surface must be tessellated into a triangle mesh. The mesh is stored as two arrays: a flat list of vertex coordinates (x, y, z) and an index list grouping vertices into triples. Flat polygonal faces are triangulated by fan‑triangulation (n‑2 triangles for an n‑gon). Cylindrical faces are sampled on a UV grid: the u‑parameter spans 0…2π around the axis, v is derived from projecting boundary vertices onto the cylinder axis to obtain the height range; each grid cell yields two triangles. Spherical faces use latitude/longitude sampling, with special handling at the poles where rows collapse to a single vertex and triangles form a fan. For faces with holes, a bridge is created between the outer boundary and an inner loop to form a single polygon, then ear‑clipping is applied: repeatedly remove ears—convex triples containing no other vertices—until only one triangle remains. The final output is a `TriangleMesh{ vertices: Vec, indices: Vec }`, compatible with GPUs, STL files, and physics engines.

## Discussion Summary
The comment emphasizes that modern GPUs support rendering methods beyond triangle rasterization, such as analytical ray tracing, signed distance fields, and direct NURBS ray tracing, allowing smooth surfaces without tessellation. It corrects the misconception that all on‑screen smooth objects rely on tiny flat triangles, noting triangles remain practical but are not universally required. Historical challenges of triangulating curved geometry are mentioned, alongside improvements in angle‑optimizing algorithms. The tone concludes with appreciation for the referenced website and its explanation.

---

## Full Article

Your GPU doesn't know what a cylinder is.

It knows triangles! That's it. Three points, maybe a color. The entire vocabulary of graphics hardware fits on an index card.

12 triangles. That's all a cube is.

So before any curved surface can be rendered, someone has to chop it into triangles. Lots of them! Arranged just right so the illusion holds.

That's tessellation.

Triangles all the way down
--------------------------

A triangle mesh is just two arrays:

```
vertices: [x₀, y₀, z₀, x₁, y₁, z₁, x₂, y₂, z₂, ...]
indices:  [0, 1, 2, 0, 2, 3, ...]
```

Vertices are points in space, and indices say which three points form each triangle. That's the entire data structure!

Every 3D model you've ever seen - every game character, every CAD render, every Pixar frame - is just these two arrays, fed to a GPU that draws triangles really, really fast.

The translation problem
-----------------------

In vcad's kernel, a cylinder isn't triangles. It's a mathematical function:

```
fn point_on_cylinder(u: f64, v: f64) -> Point3 {
    Point3::new(
        radius * u.cos(),
        radius * u.sin(),
        v
    )
}
```

Give me an angle `u` and a height `v`, and I'll give you the exact point. Infinite precision! No facets.

Beautiful for math, but useless for rendering.

The tessellator's job is to sample this function enough times to build a convincing mesh.

Sampling a surface
------------------

How do you turn a smooth surface into triangles?

You sample it!

Lay down a grid in parameter space, the flat (u, v) domain. Evaluate the surface at each grid point to get 3D coordinates, then connect adjacent points into triangles.

More samples = smoother result = more triangles = slower everything.

32 segments around a circle is plenty for most CAD. 64 if you're zooming in. 128 if you're patient!

The easy case: flat faces
-------------------------

Planar faces don't need sampling because the vertices are already there in the topology. You just need to connect them!

For convex polygons, fan triangulation works perfectly:

Pick one vertex, draw triangles to every other pair, and you're done!

A square becomes 2 triangles, a hexagon becomes 4, and an n-gon becomes n-2.

Curved faces: cylinders
-----------------------

Cylinders need the UV grid approach.

The `u` parameter goes around (0 to 2π) and the `v` parameter goes up and down.

But the surface equation extends infinitely, so we need to know where to stop! The answer: look at the boundary edges and project them onto the cylinder axis to find the height range.

```
for vertex in boundary {
    let v = (vertex - center).dot(axis);
    v_min = v_min.min(v);
    v_max = v_max.max(v);
}
```

Now sample a grid from `v_min` to `v_max` and around the full circle. Each grid cell becomes two triangles!

Curved faces: spheres
---------------------

Same idea, but latitude/longitude instead of angle/height.

There's a catch though: the poles.

UV space9 vertices at top row→3D sphereall map to same point!

show fix

At the north and south poles, an entire row of UV samples collapse to a single point. If you make normal quads there, you get degenerate slivers!

The fix: at the poles, emit triangles instead of quads. The pole vertex becomes the tip of a fan, shared by every triangle in that ring.

Like the segments of an orange, all meeting at the stem!

The hard case: holes
--------------------

Everything above assumes simple faces: one boundary, no holes.

But what happens when you drill through a plate?

outerhole

can't fan-triangulate - would cover the hole

problemfind pointsbridge

The face now has an inner loop. Fan triangulation would cover the hole! We need something smarter.

The trick: cut a bridge.

Find the rightmost point of the hole, find the nearest point on the outer boundary, and connect them with two edges (there and back), merging both loops into one continuous polygon.

Now there's no hole! Just a weird-shaped polygon with a slit. And we can triangulate weird-shaped polygons.

Ear clipping
------------

The merged polygon isn't convex, so fan triangulation won't work. Time for the real algorithm!

non-convex polygon - can't use fan triangulation

← back1 / 9next →reset

An ear is three consecutive vertices where:

1. The middle vertex is convex (bends outward)
2. No other vertices are inside the triangle

Find an ear, clip it off as a triangle, and repeat until only three vertices remain!

It's like eating a pizza from the crust inward, one bite at a time, always picking a bite that doesn't overlap with toppings.

ear!

this slice sticks out - it's an ear!

hide eartake a bite!

How do we check "convex"? See if the vertex bends outward by checking which side of a line it's on. How do we check "inside"? See if a point is surrounded by all three edges of the triangle. Both checks are just a few multiplications - fast enough to run in real-time!

The output
----------

Every surface (planes, cylinders, spheres, cones, faces with holes) eventually becomes:

```
TriangleMesh {
    vertices: Vec<f32>,  // [x, y, z, x, y, z, ...]
    indices: Vec<u32>,   // [i, j, k, i, j, k, ...]
}
```

This is the format GPUs want, the format STL files use, and the format physics engines expect.

The tessellator is the last stop in CAD-land before geometry enters the real world!

The illusion
------------

Remember: your GPU doesn't know what a sphere is.

what you see: a smooth sphere

reveal the illusion

Every smooth surface you've ever seen on a screen was actually tiny flat triangles, packed so tightly your eyes couldn't tell the difference. That's the trick. That's the whole trick!

The tessellator is the magician's assistant - it does the work so the illusion can happen. It takes beautiful mathematical curves and quietly, invisibly, chops them into something a GPU can actually draw.

And when you look at the result spinning on your screen, smooth and perfect?

You'd never know.