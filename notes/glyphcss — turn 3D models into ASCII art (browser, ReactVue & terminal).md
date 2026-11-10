---
title: "glyphcss — turn 3D models into ASCII art (browser, React/Vue & terminal)"
url: https://glyphcss.com
clipped: 2026-08-31 12:26:33
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [glyphcss — turn 3D models into ASCII art (browser, React/Vue & terminal)](https://glyphcss.com)

## Full Article

[[glyphcss] _](https://glyphcss.com/)                 ``      Loading…         

#  glyphcss 

 

 >
Turn 3D models into ASCII art, rendered as text in a single
 `<pre>` . No WebGL. No  `<canvas>`  —
              inspect, hover, and click every cell.
 

 >
Load OBJ, glTF, GLB, STL, and MagicaVoxel VOX — with UV textures and
              material colors. Works with vanilla JS, React, and Vue, or straight
              in your terminal.
  ``    [[ View on GitHub ★ … ]](https://github.com/apresmoi/glyphcss) [[ Browse gallery ]](https://glyphcss.com/gallery)   runtimes: vanilla js react vue      [ INSTALLATION ]    

 ┌─ package managers ─┐    terminal  `$  `npm install glyphcss` `   terminal  `$  `npm install @glyphcss/react` `   terminal  `$  `npm install @glyphcss/vue` `      

 ┌─ cdn ─┐    index.html  ` `<script type="module" src="https://esm.sh/glyphcss/elements"></script>` `         [ HOW IT WORKS ]     ``    

 >
glyphcss loads OBJ, glTF, GLB, STL, and VOX mesh files. Each scene
              renders into a single  `<pre>` : the rasteriser
              projects every polygon, fills a  `cols × rows`  character
              grid, and writes one string to  `textContent`  per render.
              There are no per-polygon DOM nodes and no  `matrix3d` .
 

 >
Interactivity is opt-in and sparse: drop a  `<GlyphHotspot>` 
at any 3D anchor and glyphcss emits one absolutely-positioned
 `<div>`  over the projected cell. Real DOM events,
              real  `:hover`  styles, real  `role="button"` 
accessibility — without one DOM node per polygon.
 

 [[ → core concepts ]](https://glyphcss.com/core-concepts)      [ HELLO WORLD ]   

 >
glyphcss provides custom elements ( `<glyph-scene>` ,  `<glyph-mesh>` ),
              an imperative  `createGlyphScene`  API, and optional React / Vue bindings.
              Use whichever entry point fits your stack.
       ~/project/   vanilla js  React  Vue     ` `<script type="module" src="https://esm.sh/glyphcss/elements"></script>

<glyph-camera rot-x="23" zoom="1.3">
  <glyph-scene>
    <glyph-orbit-controls drag wheel></glyph-orbit-controls>
    <glyph-mesh geometry="dodecahedron">
      <glyph-hotspot at="0,1,0"></glyph-hotspot>
    </glyph-mesh>
  </glyph-scene>
</glyph-camera>` `  ` `import { GlyphCamera, GlyphScene, GlyphOrbitControls, GlyphMesh, GlyphHotspot } from "@glyphcss/react";

export function App() {
  return (
    <GlyphCamera rotX={23} zoom={1.3}>
      <GlyphScene>
        <GlyphOrbitControls drag wheel />
        <GlyphMesh geometry="dodecahedron">
          <GlyphHotspot at={[0, 1.2, 0]} onClick={() => alert("vertex")} />
        </GlyphMesh>
      </GlyphScene>
    </GlyphCamera>
  );
}` `  ` `<template>
  <GlyphCamera :rot-x="23" :zoom="1.3">
    <GlyphScene>
      <GlyphOrbitControls drag wheel />
      <GlyphMesh geometry="dodecahedron">
        <GlyphHotspot :at="[0, 1.2, 0]" @click="onVertex" />
      </GlyphMesh>
    </GlyphScene>
  </GlyphCamera>
</template>
<script setup lang="ts">
import { GlyphCamera, GlyphScene, GlyphOrbitControls, GlyphMesh, GlyphHotspot } from "@glyphcss/vue";
function onVertex() { alert("vertex"); }
</script>` `   

 [[ → api reference ]](https://glyphcss.com/api/headless)
