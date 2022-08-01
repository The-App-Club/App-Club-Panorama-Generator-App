function zeroPadding(number) {
  return String(number).padStart(2, "0");
}

const contentDom = document.querySelector(`.content`);
const num = 40;
for (let index = 1; index < num; index++) {
  const div = document.createElement(`div`);
  div.classList.add("item");
  div.style.setProperty("--item-index", index + 0);
  div.style.backgroundImage = `url(./images/${zeroPadding(index)}.webp)`;
  contentDom.appendChild(div);
}
