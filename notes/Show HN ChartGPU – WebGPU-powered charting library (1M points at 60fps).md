---
title: "Show HN: ChartGPU – WebGPU-powered charting library (1M points at 60fps)"
url: https://github.com/ChartGPU/ChartGPU
clipped: 2026-06-17 01:55:14
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: ChartGPU – WebGPU-powered charting library (1M points at 60fps)](https://github.com/ChartGPU/ChartGPU)

## Digest Summary
ChartGPU is an open‑source charting library built on WebGPU, enabling high‑performance, GPU‑accelerated visualizations for web applications. The project is hosted on GitHub and distributed via npm, providing developers with a ready‑to‑install package. It includes a live demo showcasing various chart types, such as candlestick charts, demonstrating the library’s rendering capabilities. The repository lists its licensing information, allowing unrestricted use under the specified terms. Overall, ChartGPU offers a modern, GPU‑based solution for creating interactive, aesthetically pleasing charts directly in the browser.

## Discussion Summary
Enthusiasm dominates the discussion, with many noting the remarkable smoothness, high frame rates and scalability of the WebGPU charts, especially for large datasets and live‑streaming scenarios. Practical feedback highlights bugs such as slider drift, panning thresholds, and missing fallback for browsers lacking WebGPU, alongside requests for columnar data layouts, worker‑thread/offscreen support, and integration with existing ecosystems like Vega, React Native or Jupyter. Skeptical voices question the necessity for extreme point counts, cite compatibility gaps on Safari, Firefox and some Linux setups, and raise security concerns about GPU access. Overall the project is praised for its performance while prompting several usability and portability improvements.

---

## Full Article

[![ChartGPU](https://github.com/ChartGPU/ChartGPU/raw/main/docs/assets/chartgpu.png)](https://github.com/ChartGPU/ChartGPU/blob/main/docs/assets/chartgpu.png)

The fastest open-source charting library — 50M points at 60 FPS.

ChartGPU is a TypeScript charting library built on WebGPU for smooth, interactive rendering—especially when you have lots of data.

[![ChartGPU demo](https://raw.githubusercontent.com/chartgpu/chartgpu/main/docs/assets/chart-gpu-demo.gif)](https://raw.githubusercontent.com/chartgpu/chartgpu/main/docs/assets/chart-gpu-demo.gif)

### Streaming Multi-Chart Dashboard

Five live charts. Annotations ticking in real time. Latency percentiles, throughput, error rates, resource utilization — all streaming simultaneously at 60 FPS on a single shared `GPUDevice`. This is what ChartGPU was built for.

Want to build your own? Check out the [Multi-Chart Dashboard Cookbook](https://github.com/ChartGPU/ChartGPU/blob/main/docs/guides/multichart-dashboard-cookbook.md) for hands-on recipes and tips to get started!

[![Streaming multi-chart dashboard example](https://github.com/ChartGPU/ChartGPU/raw/main/docs/assets/streaming-dashboard-example.png)](https://github.com/ChartGPU/ChartGPU/blob/main/docs/assets/streaming-dashboard-example.png)

35,000,000 points rendered at ~72 FPS (benchmark mode).

[![35 million point benchmark at 72 FPS](https://github.com/ChartGPU/ChartGPU/raw/main/docs/assets/35-million-ultimate-benchmark-example.png)](https://github.com/ChartGPU/ChartGPU/blob/main/docs/assets/35-million-ultimate-benchmark-example.png)

```
import { ChartGPU } from 'chartgpu';
const container = document.getElementById('chart')!;
await ChartGPU.create(container, {
  series: [{ type: 'line', data: [[0, 1], [1, 3], [2, 2]] }],
});
```

Add reference lines, point markers, and text overlays to highlight important data features:

```
await ChartGPU.create(container, {
  series: [{ type: 'line', data: [[0, 1], [1, 3], [2, 2]] }],
  annotations: [
    // Horizontal reference line
    {
      id: 'ref-y',
      type: 'lineY',
      y: 2.5,
      layer: 'belowSeries',
      style: { color: '#ffd166', lineWidth: 2, lineDash: [8, 6], opacity: 0.95 },
      label: { text: 'threshold' },
    },
    // Point marker at peak
    {
      id: 'peak',
      type: 'point',
      x: 1,
      y: 3,
      layer: 'aboveSeries',
      marker: { symbol: 'circle', size: 8, style: { color: '#ff4ab0' } },
      label: { template: 'peak={y}', decimals: 2 },
    },
  ],
});
```

See [Annotations Documentation](https://github.com/chartgpu/chartgpu/blob/main/docs/api/options.md#annotations) and the [annotations example](https://github.com/chartgpu/chartgpu/tree/main/examples/annotation-authoring).

* 🚀 WebGPU-accelerated rendering for high FPS with large datasets
* 📈 Multiple series types: line, area, bar, scatter, pie, candlestick
* 🌡️ Scatter density/heatmap mode (`mode: 'density'`) for large point clouds — see [`docs/api/options.md#scatterseriesconfig`](https://github.com/ChartGPU/ChartGPU/blob/main/docs/api/options.md#scatterseriesconfig) and [`examples/scatter-density-1m/`](https://github.com/ChartGPU/ChartGPU/blob/main/examples/scatter-density-1m)
* 📍 Annotation overlays: reference lines (horizontal/vertical), point markers, and text labels — see [`docs/api/options.md#annotations`](https://github.com/ChartGPU/ChartGPU/blob/main/docs/api/options.md#annotations) and [`examples/annotations/`](https://github.com/ChartGPU/ChartGPU/blob/main/examples/annotations)
* 🧭 Built-in interaction: hover highlight, tooltip, crosshair
* 🔁 Streaming updates via `appendData(...)` with typed-array support (`XYArraysData`, `InterleavedXYData`, `DataPoint[]`) — see [`examples/cartesian-data-formats/`](https://github.com/ChartGPU/ChartGPU/blob/main/examples/cartesian-data-formats)
* 🔌 Line/area segmentation via `null` data entries — gaps for exchange outages, maintenance windows, etc. `connectNulls` option bridges gaps — see [`examples/exchange-gaps/`](https://github.com/ChartGPU/ChartGPU/blob/main/examples/exchange-gaps)
* 🔍 X-axis zoom (inside gestures + optional slider UI)
* 🎛️ Theme presets (`'dark' | 'light'`) and custom theme support
* 🔗 Shared GPUDevice support for multi-chart dashboards (efficient GPU resource management) — see [`docs/api/chart.md#shared-gpudevice`](https://github.com/ChartGPU/ChartGPU/blob/main/docs/api/chart.md#shared-gpudevice)
* 🧱 Shared pipeline cache for multi-chart dashboards (dedupe shader modules + render pipelines across charts) — see [`docs/api/chart.md#pipeline-cache-cgpu-pipeline-cache`](https://github.com/ChartGPU/ChartGPU/blob/main/docs/api/chart.md#pipeline-cache-cgpu-pipeline-cache)

Financial OHLC (open-high-low-close) candlestick rendering with classic/hollow style toggle and color customization. The live streaming demo renders **5 million candlesticks at over 100 FPS** with real-time updates.

[![Candlestick chart example](https://github.com/ChartGPU/ChartGPU/raw/main/docs/assets/candle-stick-example.png)](https://github.com/ChartGPU/ChartGPU/blob/main/docs/assets/candle-stick-example.png)

### Scatter Density (1M points)

GPU-binned density/heatmap mode for scatter plots (`mode: 'density'`) to reveal structure in overplotted point clouds. See [`docs/api/options.md#scatterseriesconfig`](https://github.com/ChartGPU/ChartGPU/blob/main/docs/api/options.md#scatterseriesconfig) and the demo in [`examples/scatter-density-1m/`](https://github.com/ChartGPU/ChartGPU/blob/main/examples/scatter-density-1m).

[![Scatter density chart example (1M points)](https://github.com/ChartGPU/ChartGPU/raw/main/docs/assets/scatter-plot-density-chart-1million-points-example.png)](https://github.com/ChartGPU/ChartGPU/blob/main/docs/assets/scatter-plot-density-chart-1million-points-example.png)

### Interactive Annotation Authoring

Full-featured annotation authoring system with interactive editing capabilities. Create, edit, drag, and delete annotations with an intuitive UI. Supports all annotation types: reference lines (horizontal/vertical), point markers, text annotations (plot-space + data-space tracking), labels, and styling options.

[![Annotations comprehensive demo](https://github.com/ChartGPU/ChartGPU/raw/main/docs/assets/annotations.png)](https://github.com/ChartGPU/ChartGPU/blob/main/docs/assets/annotations.png)

**Key features:**

* **Right-click empty space** → Add vertical/horizontal line or text note with custom color, style & label
* **Click & drag annotations** → Reposition them (lines constrained to their axis)
* **Right-click on annotation** → Edit properties or delete
* **Full styling control** → Color picker, line style (solid/dashed), line width, and label customization
* **Undo/Redo support** → All annotations are reversible
* **Scroll to zoom, Drag to pan** → Standard chart interactions work seamlessly

[![Annotation configuration dialog](https://github.com/ChartGPU/ChartGPU/raw/main/docs/assets/annontations-add-indicator.png)](https://github.com/ChartGPU/ChartGPU/blob/main/docs/assets/annontations-add-indicator.png)

The annotation authoring system is demonstrated in the [`examples/annotation-authoring/`](https://github.com/ChartGPU/ChartGPU/blob/main/examples/annotation-authoring) example.

**GitHub Packages:**

```
npm install @chartgpu/chartgpu
```

For GitHub Packages, configure your `.npmrc`:

```
@chartgpu:registry=https://npm.pkg.github.com
```

React bindings are available via [`chartgpu-react`](https://github.com/ChartGPU/chartgpu-react):

```
npm install chartgpu-react
```

```
import { ChartGPUChart } from 'chartgpu-react';

function MyChart() {
  return (
    <ChartGPUChart
      options={{
        series: [{ type: 'line', data: [[0, 1], [1, 3], [2, 2]] }],
      }}
    />
  );
}
```

See the [chartgpu-react repository](https://github.com/ChartGPU/chartgpu-react) for full documentation and examples.

Browser support (WebGPU required)
---------------------------------

* Chrome 113+ or Edge 113+ (WebGPU enabled by default)
* Safari 18+ (WebGPU enabled by default)
* Firefox: Windows 114+, Mac 145+, Linux nightly

See the [gpuweb repository](https://github.com/gpuweb/gpuweb/wiki/Implementation-Status) for full Implementation Status

ChartGPU is a young project and we'd love to hear how you're using it! If your team or project uses ChartGPU, [open a pull request](https://github.com/chartgpu/chartgpu/pulls) to add your name here.

* Browse examples: [`examples/`](https://github.com/chartgpu/chartgpu/tree/main/examples)
* Run locally:
  + `npm install`
  + `npm run dev` (opens `http://localhost:5173/examples/`)

See [`CONTRIBUTING.md`](https://github.com/chartgpu/chartgpu/blob/main/CONTRIBUTING.md).

MIT — see [`LICENSE`](https://github.com/chartgpu/chartgpu/blob/main/LICENSE).

ChartGPU follows a functional-first architecture. `ChartGPU.create(...)` owns the canvas and WebGPU lifecycle, delegating render orchestration to a modular render coordinator with 11 specialized modules.

For the full architecture diagram, see [`docs/ARCHITECTURE.md`](https://github.com/ChartGPU/ChartGPU/blob/main/docs/ARCHITECTURE.md). For deep internal notes, see [`docs/api/INTERNALS.md`](https://github.com/ChartGPU/ChartGPU/blob/main/docs/api/INTERNALS.md).