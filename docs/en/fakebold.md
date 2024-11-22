---
title: Fake bold
lang: en
---

# Fake bold `fakebold`

## Intro

Cuti simulates fake bold by utilizing the `stroke` attribute of `text`. This package is typically used on fonts that do not have a `bold` weight, such as "SimSun". This package uses 0.02857em as the parameter for stroke. In Microsoft Office software, enabling fake bold will apply a border of about 0.02857em to characters. This is where the value of 0.02857em is derived from. (In fact, the exact value may be $1/35$.)

::: details DEMO

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

## `fakebold`

`#fakebold[]` with no parmerter will apply the **fakebold** effect to characters.

```typst
- Fakebold: #fakebold[#lorem(5)]
- Bold: #text(weight: "bold", lorem(5))
- Bold + Fakebold: #fakebold[#text(weight: "bold", lorem(5))]
```

`#fakebold` can accept the same parameters as `#text`.

- The `stroke` parameter, if specified, will be ignored.
- If the `weight` parameter is specified, it can be used to define which font weight to base the stroke on. The default is `auto`, and the options are `auto`, `none`, or an `int`/`str` representing font weight.
  - `none` - Stroke based on `regular` weight;
  - `auto` - Stroke based on current weight (may have side effects, see explanation below);
  - `int`/`str` - Please refer to the official documentation <https://typst.app/docs/reference/text/text/#parameters-weight>.

```typst
- Regular: #lorem(5)
- Regular + Fakebold: #fakebold[#lorem(5)]
- Bold: #text(weight: "bold")[#lorem(5)]
- Bold + Fakebold: #fakebold(weight: "bold")[#lorem(5)]
- Bold + Fakebold: #set text(weight: "bold"); #fakebold[#lorem(5)]
```

::: tip Compatibility Note
`cuti:^0.3.0` (compatible with Typst 0.12.0) retains `base-weight` as an alias for `weight` for backward compatibility, and `base-weight` has higher priority than `weight`.

In `cuti:^0.2.1` (compatible with Typst 0.11.x), the default value of `weight` is `none`, indicating stroke based on current weight.
:::

If the text is set to a color, the fake bold stroke will also change to the corresponding color.

```typst
- Blue + Fakebold: #fakebold(fill: blue)[花生瓜子八宝粥，啤酒饮料矿泉水。#lorem(5)]
- Gradient + Fakebold: #set text(fill: gradient.conic(..color.map.rainbow)); #fakebold[花生瓜子八宝粥，啤酒饮料矿泉水。#lorem(5)]
```

## `regex-fakebold`

The `#regex-fakebold` is designed to be used in multilingual and multi-font scenarios. It allows the use of a RegExp string as the `reg-exp` parameter to match characters that will have the fake bold effect applied. It can also accept the same parameters as `#fakebold`.

```typst
+ RegExp `[a-o]`: #regex-fakebold(reg-exp: "[a-o]")[#lorem(5)]
+ RegExp `\p{script=Han}`: #regex-fakebold(reg-exp: "\p{script=Han}")[衬衫的价格是9磅15便士。]
+ RegExp `\p{script=Han}`: #set text(weight: "bold"); #regex-fakebold(reg-exp: "\p{script=Han}")[衬衫的价格是9磅15便士。]
```

In Example 3, `9` and `15` are the real bold characters from the font file, while the other characters are simulated as "fake bold" based on the `regular` weight.

## `show-fakebold`

In multilingual and multi-font scenarios, different languages often utilize their own fonts, but not all fonts contain the `bold` weight. It can be inconvenient to use `#fakebold` or `#regex-fakebold` each time we require `strong` or `bold` effects. Therefore, the `#show-fakebold` function is introduced for `show` rule.

`show-fakebold` and `regex-fakebold` share the same parameters. By default:

- `show-fakebold` uses `"."` as the regular expression, meaning all characters with bold or `strong` attributes will be fake-bolded;
- `show-fakebold` uses `weight: none` as the default base weight:
  - In `cuti:^0.2.1` (compatible with Typst 0.11.x), it will apply fake bold based on the current font weight.
  - In `cuti:^0.3.0` (compatible with Typst 0.12.0), it will apply fake bold based on the `regular` font weight.

```typst
#show: show-fakebold
- Regular: #lorem(10)
- Bold: #text(weight: "bold")[#lorem(10)]
```

::: danger Why the new version no longer defaults to boldening based on current weight
In Typst 0.11.x, boldening based on current weight generally didn't cause issues. However, in Typst 0.12.0, `show` rules might match already processed characters again, leading to infinite loops. Therefore, in `cuti:0.3.0`, `cuti` changed its default behavior.
:::

Under normal circumstances, the combination of font-provided bold and fake bold is not the effect we want. Generally, we need to specify regular expressions to define the scope where fake bold should take effect.

```typst
#show: show-fakebold.with(reg-exp: "\p{script=Han}")
- Regular: 我正在使用 Typst 排版。
- Strong: *我正在使用 Typst 排版。*
```

## cn-fakebold & show-cn-fakebold

`cn-fakebold` and `show-cn-fakebold` are encapsulations of the above `regex-fakebold` and `show-fakebold`, pre-configured for use with Chinese text. Please refer to the Chinese documentation for detailed usage instructions.
