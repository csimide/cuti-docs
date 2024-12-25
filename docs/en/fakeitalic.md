---
title: Fake Italic
lang: en
---

# Fake Italic

## Intro

Cuti implements fake italic using the `skew` function. In `cuti:^0.2.1` (compatible with Typst 0.11.x), `skew` was provided by Typst issue #2749 (https://github.com/typst/typst/issues/2749) by Enivex; in Typst 0.12.0, the `skew` functionality has been integrated into Typst itself.

Cuti uses -0.32175 as the default slant angle. In Microsoft Office, fake italic adds a slant effect of arctan(1/3) to characters. You may need to adjust the angle yourself to achieve the best aesthetic effect.

::: tip CJK Typography Notice
Using italics in CJK text may compromise typographic aesthetics. A common practice is to use alternative fonts instead of italics to achieve emphasis. For example, in LaTeX, Chinese text typically uses Kaiti (楷体) instead of italics. You can visit https://typst-doc-cn.github.io/guide/FAQ/chinese-skew.html (in Chinese) for more information.

Cuti does not recommend CJK users to use the fake italic functionality provided by this package, even though it has made some adaptations for CJK characters.
:::

::: details DEMO

```typst
#fakeitalic[#lorem(30)]
```

:::

## `fakeitalic`

`#fakeitalic[]` will apply the _fakeitalic_ effect to characters.

```typst
- Regular: #lorem(5)
- Italic: #text(style: "italic", lorem(5))
- Fakeitalic: #fakeitalic[#lorem(5)]
- Fakeitalic + Fakebold: #fakeitalic[#fakebold[#lorem(5)]]
```

The angle of skew can be adjusted through the `ang` parameter, which accepts a value of type `angle` and defaults to `-18.4deg` (i.e., arctan(1/3)).

```typst
- -10deg: #fakeitalic(ang: -10deg)[#lorem(5)]
- -20deg: #fakeitalic(ang: -20deg)[#lorem(5)]
- +20deg: #fakeitalic(ang:  20deg)[#lorem(5)]
```

::: tip
`fakeitalic` is based on `regex-fakeitalic`. In `cuti:0.3.0`, the regular expression used by `fakeitalic` is:

```regex
(?:\b[^\p{Script=Han}\p{Script=Hiragana}\p{Script=Katakana}\p{Script=Hangul}！-･〇-〰—]+?\b|[\p{Script=Han}\p{Script=Hiragana}\p{Script=Katakana}\p{Script=Hangul}])
```

This regular expression originates from [cuti PR #5](https://github.com/csimide/cuti/pull/5) by [Tetragramm](https://github.com/Tetragramm), and was later improved for CJK character support.

**Note that this regular expression does not match punctuation marks.** This is because including punctuation marks in the matching range might cause additional typography breakage.
:::

## `regex-fakeitalic`

`regex-fakeitalic` provides the functionality to apply fake italics to specified content based on regular expressions. Use the `reg-exp` parameter to specify the regular expression, and the `ang` parameter to specify the slant angle.

```typst
+ RegExp `[a-o]`: #regex-fakeitalic(reg-exp: "[a-o]")[#lorem(5)]
+ RegExp `\p{script=Han}`: #regex-fakeitalic(reg-exp: "\p{script=Han}")[衬衫的价格是9磅15便士。]
+ RegExp `\p{script=Han}`: #set text(style: "italic"); #regex-fakeitalic(reg-exp: "\p{script=Han}", ang: -10deg)[衬衫的价格是9磅15便士。]
```

## Issues at hand

The pseudo-italic effect provided by `cuti` is often not ideal and is not recommended for use throughout the entire text. We welcome issues or pull requests to help us improve it.
