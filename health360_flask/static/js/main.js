document.addEventListener("DOMContentLoaded", () => {
  // Small interaction polish for keyboard users and responsive navigation.
  document.querySelectorAll("a.nav-link").forEach(link => {
    link.addEventListener("focus", () => link.classList.add("keyboard-focus"));
    link.addEventListener("blur", () => link.classList.remove("keyboard-focus"));
  });
});
