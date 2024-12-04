// store the theme preference inside local storage
let theme = localStorage.getItem("theme")
const themeToggler = document.querySelector("#theme-toggler")

const enableDarkMode = () => {
  document.body.classList.add("dark")
  localStorage.setItem("theme", "dark")
}

const disableDarkMode = () => {
  document.body.classList.remove("dark")
  localStorage.setItem("theme", null)
}

if (theme === "dark" ) enableDarkMode()

themeToggler.addEventListener("click", () => {
  theme = localStorage.getItem("theme")
  theme !== "dark" ? enableDarkMode() : disableDarkMode()
})