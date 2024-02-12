function checkPalindromo() {
    const inputText = document
        .getElementById("inputText")
        .value.toLowerCase()
        .replace(/[^a-z0-9]/g, "");

    const reverseText = inputText.split("").reverse().join("");
    const resultElement = document.getElementById("result");
    if (inputText === reverseText) {
        resultElement.textContent = "É um palíndromo";
    } else {
        resultElement.textContent = "Não é um palíndromo";
    }
    // alert(reverseText);
}
