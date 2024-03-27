/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      color: {
        coverColor: 'rgb(165, 233, 255)',
      },
      fontfamily: {
        'newFont1': ['Raleway'],
        'newFont2': ['Nunito'],
      },
    },
  },
  plugins: [],
}