function enlarge(element) {
    const isEnlarged = element.classList.contains("enlarged");

    const elements = document.querySelectorAll(".coluna1, .coluna2, .coluna3");
    elements.forEach((item) => item.classList.remove("enlarged"));

    if (!isEnlarged) {
        element.classList.add("enlarged");
    }
}
