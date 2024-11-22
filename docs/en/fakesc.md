---
title: Fake Small Capitals
lang: en
---

# Fake Small Capitals

## Intro

Cuti implements small capitals through font size variation.

::: tip
This feature was introduced by [cuti PR \#5](https://github.com/csimide/cuti/pull/5) by [Tetragramm](https://github.com/Tetragramm).
:::

::: details DEMO

```typst
#fakesc[#lorem(30)]
```

:::

## `fakesc`

`fakesc` is used to generate small capitals. By default, small capitals are `0.75` times the size of regular text, which can be adjusted using the `scaling` parameter.

```typst
#fakesc[#lorem(10)]

#fakesc(scaling: 0.5)[#lorem(10)]
```
