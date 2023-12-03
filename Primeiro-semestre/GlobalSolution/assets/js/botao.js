document.addEventListener("DOMContentLoaded", function () {
    var tamanhoFonte = 16; // tamanho inicial da fonte em pixels
    var elementosAjustaveis = document.querySelectorAll(".ajustavel");
  
    document
      .getElementById("botaoFlutuanteMais")
      .addEventListener("click", function () {
        tamanhoFonte += 2;
        elementosAjustaveis.forEach(function (elemento) {
          elemento.style.fontSize = tamanhoFonte + "px";
        });
      });
  
    document
      .getElementById("botaoFlutuanteMenos")
      .addEventListener("click", function () {
        tamanhoFonte -= 2;
        elementosAjustaveis.forEach(function (elemento) {
          elemento.style.fontSize = tamanhoFonte + "px";
        });
      });
  
    var elementosH2 = document.getElementsByTagName("h2");
    for (var i = 0; i < elementosH2.length; i++) {
      elementosH2[i].addEventListener("click", function () {
        tamanhoFonte -= 2;
        elementosAjustaveis.forEach(function (elemento) {
          elemento.style.fontSize = tamanhoFonte + "px";
        });
      });
    }
  });
  