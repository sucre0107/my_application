/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './ai_apps/templates/**/*.html',
      './ai_apps/templates/*.html',
      './pknight_docs/templates/**/*.html',
      './pknight_docs/templates/*.html',
      './ai_apps/forms.py',
      // 只要是用到 tailwind 的地方都要加入
      './pknight_docs/static/pknight_docs/js/zoomable-img.js',

  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

