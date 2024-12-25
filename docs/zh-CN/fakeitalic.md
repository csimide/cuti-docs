---
title: 伪斜体 fakeitalic
lang: zh-CN
---

# 伪斜体

## 简介

Cuti 利用 `skew` 函数实现伪斜体。在 `cuti:^0.2.1` （适配 Typst 0.11.x） ， `skew` 由 Typst issue \#2749 (https://github.com/typst/typst/issues/2749) by Enivex 提供；在 Typst 0.12.0 ，`skew` 功能已被合入 Typst 本体。

Cuti 使用 -0.32175 作为默认的倾斜角度。在 Microsoft Office 中，使用伪粗体会给字符添加一个 arctan(1/3) 的倾斜效果。请注意，由于不同的英文字体拥有不同的倾斜角度，需要自行寻找一个合适的角度。如果使用 Times New Roman 与中易宋体，则默认的角度是比较合适的。

::: tip 中文排版提醒
在中文中使用斜体可能会破坏排版美感。常用的做法是，使用其他字体代替斜体，实现强调的效果。如 LaTeX 中一般使用楷体代替斜体。您可以查看 https://typst-doc-cn.github.io/guide/FAQ/chinese-skew.html 以获得相关信息。

Cuti 不建议中文用户使用本 package 提供的伪斜体功能，即使它针对 CJK 字符进行了一些适配。
:::

效果展示如下：

::: details

```typst
#fakeitalic[#lorem(30)]

#fakeitalic[你说得对，但是《Typst》是一款由 Typst GmbH 与众多贡献者开发的一款开放世界冒险排版游戏。游戏发生在一个被称作「typst.app」的线上世界。在这里，后面忘了——同时，逐步发掘排版的真相。Typst，启动！]
```

:::

## `fakeitalic`

`#fakeitalic[]` 会为字符添加 _伪斜体_ 效果。

```typst
- Regular: #lorem(5)
- Italic: #text(style: "italic", lorem(5))
- Fakeitalic: #fakeitalic[#lorem(5)]
- Fakeitalic + Fakebold: #fakeitalic[#fakebold[#lorem(5)]]
```

`fakeitalic` 提供了一个 `ang` 参数用于调整字符的倾斜程度，类型为 `angle`，默认值为 `-18.4deg` （即 arctan(1/3) ）。

```typst
- -10deg: #fakeitalic(ang: -10deg)[#lorem(5)]
- -20deg: #fakeitalic(ang: -20deg)[#lorem(5)]
- +20deg: #fakeitalic(ang:  20deg)[#lorem(5)]
```

::: tip
`fakeitalic` 是基于 `regex-fakeitalic` 的。在 `cuti:0.3.0` 中，`fakeitalic` 使用的正则表达式是

```regex
(?:\b[^\p{Script=Han}\p{Script=Hiragana}\p{Script=Katakana}\p{Script=Hangul}！-･〇-〰—]+?\b|[\p{Script=Han}\p{Script=Hiragana}\p{Script=Katakana}\p{Script=Hangul}])
```

这条正则源自 [cuti PR \#5](https://github.com/csimide/cuti/pull/5) by [Tetragramm](https://github.com/Tetragramm) ，后续因 CJK 字符需要进行了改进。

**实际上，这条正则不会匹配标点符号。** 这是因为如果将标点符号纳入匹配范围，可能会导致额外的排版崩坏。
:::

## `regex-fakeitalic`

`regex-fakeitalic` 提供了基于正则表达式对指定内容进行伪斜体的功能，使用 `reg-exp` 参数指定正则表达式，并使用 `ang` 参数指定倾斜角度。

```typst
+ RegExp `[a-o]`: #regex-fakeitalic(reg-exp: "[a-o]")[#lorem(5)]
+ RegExp `\p{script=Han}`: #regex-fakeitalic(reg-exp: "\p{script=Han}")[衬衫的价格是9磅15便士。]
+ RegExp `\p{script=Han}`: #set text(style: "italic"); #regex-fakeitalic(reg-exp: "\p{script=Han}", ang: -10deg)[衬衫的价格是9磅15便士。]
```

## 是不是缺了点什么？

是的，目前还没有 `show-fakeitalic` 与 `show-cn-fakeitalic` 。

这是因为 `cuti` 提供的伪斜体效果常常不尽如人意，并不推荐在全篇中使用。欢迎提交 issue 或 pr 以帮助我们完善。
