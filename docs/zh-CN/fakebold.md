---
title: 伪粗体 fakebold
lang: zh-CN
---

# 伪粗体

## 简介

Cuti 利用 `text` 的 `stroke` 属性生成伪粗体。该工具通常可用于为宋体、黑体、楷体等字体提供“粗体”。Cuti 使用 0.02857em 作为 `stroke` 的参数。在 Microsoft Office 中，使用伪粗体会给字符添加一个 0.02857em 的描边。（实际上，精确值可能是 1/35。）

效果展示如下：

::: details

**Part 1**: `font: ("Times New Roman", "SimSun")`

```typst
#set text(font: ("Times New Roman", "SimSun"))
#grid(
    columns: 2,
    column-gutter: 0.2em,
    row-gutter: 0.6em,
    [Regular:], [你说得对，但是《Cuti》是一个用于伪粗体和伪斜体的包。],
    [Bold(Font Only):], text(weight: "bold")[你说得对，但是《Cuti》是一个用于伪粗体和伪斜体的包。],
    [Bold(Fake Only):], fakebold[你说得对，但是《Cuti》是一个用于伪粗体和伪斜体的包。],
    [Bold(Fake+Font):], show-cn-fakebold(text(weight: "bold")[你说得对，但是《Cuti》是一个用于伪粗体和伪斜体的包。]),
)
```

**Part 2:** `font: "Source Han Serif SC"`

```typst
#set text(font: "Source Han Serif SC")
#grid(
    columns: 2,
    column-gutter: 0.2em,
    row-gutter: 0.6em,
    [Regular:], [前面忘了。同时，逐步发掘「Typst」的奥妙。],
    [Bold(Font Only):], text(weight: "bold")[前面忘了。同时，逐步发掘「Typst」的奥妙。],
    [Bold(Fake Only):], fakebold[前面忘了。同时，逐步发掘「Typst」的奥妙。],
    [Bold(Fake+Font):], show-cn-fakebold(text(weight: "bold")[前面忘了。同时，逐步发掘「Typst」的奥妙。])
)
```

:::

## 快速使用

```typst no-render
#import "@preview/cuti:0.3.0": show-cn-fakebold
#show: show-cn-fakebold
```

对于大部分“论文”式需求，在文档开头处添加上述代码，并设置字体为 `#set text(font: ("Times New Roman", "中文字体名"))` ，即可快速实现使用中文字体时也能使用粗体。例如，宋体 + 粗体：

```typst
#import "@preview/cuti:0.3.0": show-cn-fakebold
#set text(font: ("Times New Roman", "SimSun"))
+ 使用 `cuti` 前：春江潮水连海平，*海上明月共潮生*。
#show: show-cn-fakebold
+ 使用 `cuti` 后：春江潮水连海平，*海上明月共潮生*。
```

## `fakebold`

不带其他参数的 `#fakebold[]` 会为字符添加**伪粗体**效果。

```typst
- Fakebold: #fakebold[#lorem(5)]
- Bold: #text(weight: "bold", lorem(5))
- Bold + Fakebold: #fakebold[#text(weight: "bold", lorem(5))]
```

`#fakebold` 可以接受与 `#text` 相同的参数。

- 指定 `stroke` 参数会被忽略。
- 若指定 `weight` 参数，可以用于指定基于某种字重进行描边。默认为 `auto`，可选 `auto` `none` 或者表示字重的 `int` / `str`。
  - `none` - 基于 `regular` 字重进行描边；
  - `auto` - 基于当前字重进行描边（可能产生副作用，请见下文说明）；
  - `int` / `str` - 请查看官方文档说明 <https://typst.app/docs/reference/text/text/#parameters-weight> 。

```typst
- Regular: #lorem(5)
- Regular + Fakebold: #fakebold[#lorem(5)]
- Bold: #text(weight: "bold")[#lorem(5)]
- Bold + Fakebold: #fakebold(weight: "bold")[#lorem(5)]
- Bold + Fakebold: #set text(weight: "bold"); #fakebold[#lorem(5)]
```

::: tip 兼容性说明
`cuti:^0.3.0` （适配 Typst 0.12.0） 保留了 `base-weight` 作为 `weight` 的别名，以兼容旧版本，且 `base-weight` 的优先级高于 `weight`。

在 `cuti:^0.2.1` （适配 Typst 0.11.x） 中，`weight` 的默认值为 `none` ，表示基于当前字重进行描边。
:::

如果将文字设置为彩色，伪粗体描边也将变成相应的颜色。

```typst
- Blue + Fakebold: #fakebold(fill: blue)[花生瓜子八宝粥，啤酒饮料矿泉水。#lorem(5)]
- Gradient + Fakebold: #set text(fill: gradient.conic(..color.map.rainbow)); #fakebold[花生瓜子八宝粥，啤酒饮料矿泉水。#lorem(5)]
```

## `regex-fakebold`

`#regex-fakebold` 设计上是用于多语言、多字体情境的，可以根据参数 `reg-exp` 内的正则表达式只将匹配到的字符应用伪粗体格式。它也可以接受与 `#fakebold` 相同的参数。

```typst
+ RegExp `[a-o]`: #regex-fakebold(reg-exp: "[a-o]")[#lorem(5)]
+ RegExp `\p{script=Han}`: #regex-fakebold(reg-exp: "\p{script=Han}")[衬衫的价格是9磅15便士。]
+ RegExp `\p{script=Han}`: #set text(weight: "bold"); #regex-fakebold(reg-exp: "\p{script=Han}")[衬衫的价格是9磅15便士。]
```

在上面的例子 3 中, `9` 和 `15` 是字体提供的“真”粗体，而其他字符是用 `bold` 字重描边得到的伪粗体。

## `show-fakebold`

在多语言、多字体的场景中，不同的语言通常使用不同的字体，但是不是所有的字体都自带 `bold` 字重。需要 `strong` 或者 `bold` 效果时，每次都使用 `#fakebold` `#regex-fakebold` 并不方便。所以， Cuti 提供了用于设置 `show` 规则 `#show-fakebold` 函数。

`show-fakebold` 和 `regex-fakebold` 有着相同的参数。默认情况下：

- `show-fakebold` 使用 `"."` 作为正则表达式，也就是说，所有字符带加粗或 `strong` 属性都会被伪粗体加粗；
- `show-fakebold` 会使用 `weight: none` 作为默认的基准字重：
  - 在 `cuti:^0.2.1` （适配 Typst 0.11.x）中，会在当前字重的基础上加粗。
  - 在 `cuti:^0.3.0` （适配 Typst 0.12.0）中，会在 `regular` 字重的基础上加粗。
  - **但是** ，在当前的所有版本中，使用 `#strong[]` 或其语法糖 `*strong*` 加粗会导致基准字重为 `bold` 字重，该行为暂时无法更改。（如果您有解决这一问题的办法，欢迎提出 PR 或 issue ）

```typst
#show: show-fakebold
- Regular: #lorem(10)
- Bold: #text(weight: "bold")[#lorem(10)]
```

::: danger 为什么新版本不再默认基于当前字重加粗
在 Typst 0.11.x 中，基于当前字重加粗一般不会遇到问题。但是，在 Typst 0.12.0 中，`show` 规则可能会再次匹配到已被处理的字符，导致无限循环。因此，在 `cuti:0.3.0` 中，`cuti` 变更了默认行为。
:::

正常情况下字体提供的加粗与伪粗体叠加的效果不是我们想要的。一般需要指定正则表达式、指定伪粗体的生效范围。

```typst
#show: show-fakebold.with(reg-exp: "\p{script=Han}")
- Regular: 我正在使用 Typst 排版。
- Strong: *我正在使用 Typst 排版。*
```

## `cn-fakebold` & `show-cn-fakebold`

`cn-fakebold` 是 `regex-fakebold` 的封装。

`cn-fakebold` 会将中文和常见符号进行伪粗体处理，基准字重为 `regular` 字重。请注意，在混排中英文时，英文部分不会被加粗。如果需要使得英文部分也加粗，请指定一个有 `bold` 字重的英文字体，并指定 `weight: "bold"`，如下方代码第一行所示。

```typst
#set text(font: ("Libertinus Serif", "SimSun"))
- Regular: 有时，我们点击链接，打开的却是《Never Gonna Give You Up》这首歌。
- `cn-fakebold`: #cn-fakebold[《Never Gonna Give You Up》是英国歌手 Rick Astley 演唱的歌曲，于 1987 年发行。]
#set text(weight: "bold")
- Bold:《Never Gonna Give You Up》已经成为了一种网络迷因。
- Bold + `cn-fakebold`: #cn-fakebold[在 2024 年的今天，《Never Gonna Give You Up》仍有独特的魅力。]
```

`show-cn-fakebold` 是 `show-fakebold` 的封装，默认的正则范围是中文字符与常见标点符号。

```typst
#show: show-cn-fakebold
- Regular: 滚滚长江东逝水，浪花淘尽英雄。 #lorem(5)
- Bold: #text(weight: "bold")[滚滚长江东逝水，浪花淘尽英雄。 #lorem(5)]
- Strong: *滚滚长江东逝水，浪花淘尽英雄。 #lorem(5)*
```

```typst
#show-cn-fakebold[
- Regular: 滚滚长江东逝水，浪花淘尽英雄。 #lorem(5)
- Strong: *滚滚长江东逝水，浪花淘尽英雄。 #lorem(5)*
]
```

这两个函数也可以接受 `#font` 相同的参数，以指定中文字符加粗的效果。

## 已知问题

- 使用 `strong` 加粗时，基准字重固定为 `bold`。

```typst
#show: show-cn-fakebold
- Regular: 滚滚长江东逝水，浪花淘尽英雄。 #lorem(5)
- Bold: #text(weight: "bold")[滚滚长江东逝水，浪花淘尽英雄。]
- Strong + Bug: *滚滚长江东逝水，浪花淘尽英雄。 #lorem(5)*
```

- `text.tracking` 可能会不生效。

```typst
#set text(tracking: 1em)
滚滚长江#text(weight: "bold")[东逝水，浪花。]淘尽英雄
```

如有解决方案或 workaround ，欢迎 PR/issue 。
