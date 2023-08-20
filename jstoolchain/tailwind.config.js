/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../todo/templates/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}

