var link = document.querySelector(".nav");
var image = document.querySelector(".gatofoto");

function showAlert() {
    alert("Oh no 😕 Você se molhou❗ 😭😭");
}

link.addEventListener("click", showAlert);
image.addEventListener("click", showAlert);


var input = document.getElementById("myInput");

input.addEventListener("keydown", function (event) {
    if (event.keyCode === 13) {
        alert("🫡 Você se salvou 💗😀");
    }
})