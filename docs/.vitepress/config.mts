import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Cuti documentation",
  base: "/cuti-docs/",
  description:
    "The documentation for cuti, a typst package for fakebold / fakeitalic / fakesc",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    // nav: [
    //   { text: "Home", link: "/" },
    //   // { text: 'Examples', link: '/markdown-examples' }
    // ],

    // sidebar: [
    //   {
    //     text: "Examples",
    //     items: [
    //       { text: "Markdown Examples", link: "/markdown-examples" },
    //       { text: "Runtime API Examples", link: "/api-examples" },
    //     ],
    //   },
    // ],

    socialLinks: [
      { icon: "github", link: "https://github.com/csimide/cuti" },
    ],
    outline: {
      level: [2, 3],
    },
  },
  locales: {
    en: {
      label: "English",
      lang: "en",
      themeConfig: {
        nav: [
          { text: "Home", link: "/" },
        ],
        sidebar: [
          {
            // text: "Cuti Documentation",
            items: [
              { text: "Intro", link: "/en/" },
              { text: "Fake Bold", link: "/en/fakebold" },
              { text: "Fake Italic", link: "/en/fakeitalic" },
              { text: "Fake Small Captials", link: "/en/fakesc" },
            ],
          },
        ],
      },
    },
    "zh-CN": {
      label: "简体中文",
      lang: "zh-CN",
      themeConfig: {
        nav: [
          { text: "主页", link: "/" },
        ],
        sidebar: [
          {
            items: [
              { text: "简介", link: "/zh-CN/" },
              { text: "伪粗体", link: "/zh-CN/fakebold" },
              { text: "伪斜体", link: "/zh-CN/fakeitalic" },
              { text: "伪小型大写字母", link: "/zh-CN/fakesc" },
            ],
          },
        ],
      },
    },
  },
});
