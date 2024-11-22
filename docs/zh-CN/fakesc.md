---
title: 伪小型大写字母 fakesc
lang: zh-CN
---

# 伪小型大写字母

## 简介

Cuti 使用字号变化来实现小型大写字母（small capitals）。

::: tip
该功能由 [cuti PR \#5](https://github.com/csimide/cuti/pull/5) by [Tetragramm](https://github.com/Tetragramm) 引入。
:::

效果展示如下：
::: details

```typst
#fakesc[#lorem(30)]
```

:::

## `fakesc`

`fakesc` 用于生成小型大写字母。默认情况下，小型大写字母的大小是正常字号的 `0.75` 倍，可以通过 `scaling` 参数调整。

```typst
#fakesc[#lorem(10)]

#fakesc(scaling: 0.5)[#lorem(10)]
```
