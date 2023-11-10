let pontuacao = { equipeA: 0, equipeB: 0 };
let eventos = [];
let jogoAnterior = null;

function iniciarNovaPartida() {
  document.getElementById("opcoes").style.display = "none";
  document.getElementById("jogo").style.display = "block";
  document.getElementById("voltar").style.display = "block";
}

function carregarJogoAnterior() {
  if (jogoAnterior) {
    pontuacao = jogoAnterior.pontuacao;
    eventos = jogoAnterior.eventos;
    document.getElementById("pontuacaoEquipeA").innerText = pontuacao.equipeA;
    document.getElementById("pontuacaoEquipeB").innerText = pontuacao.equipeB;
    const listaEventos = document.getElementById("listaEventos");
    listaEventos.innerHTML = "";
    eventos.forEach((evento) => {
      const itemLista = document.createElement("li");
      itemLista.innerText = `${evento.jogador}: ${evento.descricao}`;
      listaEventos.appendChild(itemLista);
    });
  } else {
    alert("Não há jogo anterior para carregar.");
  }
}

function verEstatisticas() {
  alert(`Estatísticas:
    Pontuação da equipe A: ${pontuacao.equipeA}
    Pontuação da equipe B: ${pontuacao.equipeB}
    Total de eventos: ${eventos.length}`);
}

function marcarPonto(equipe) {
  pontuacao[equipe]++;
  document.getElementById("pontuacaoEquipeA").innerText = pontuacao.equipeA;
  document.getElementById("pontuacaoEquipeB").innerText = pontuacao.equipeB;
}

function registrarEvento() {
  const jogador = document.getElementById("jogadorEvento").value;
  const descricao = document.getElementById("descricaoEvento").value;
  eventos.push({ jogador, descricao });
  const listaEventos = document.getElementById("listaEventos");
  listaEventos.innerHTML = "";
  eventos.forEach((evento) => {
    const itemLista = document.createElement("li");
    itemLista.innerText = `${evento.jogador}: ${evento.descricao}`;
    listaEventos.appendChild(itemLista);
  });
}

function encerrarSet() {
  if (pontuacao.equipeA >= 25) {
    alert("A equipe A venceu o set!");
    pontuacao.equipeA = 0;
    pontuacao.equipeB = 0;
  } else if (pontuacao.equipeB >= 25) {
    alert("A equipe B venceu o set!");
    pontuacao.equipeA = 0;
    pontuacao.equipeB = 0;
  } else {
    alert("O set ainda não terminou.");
  }
}

function encerrarJogo() {
  if (pontuacao.equipeA >= 3) {
    alert("A equipe A venceu o jogo!");
  } else if (pontuacao.equipeB >= 3) {
    alert("A equipe B venceu o jogo!");
  } else {
    alert("O jogo ainda não terminou.");
  }
}

function reiniciarJogo() {
  jogoAnterior = { pontuacao: { ...pontuacao }, eventos: [...eventos] };
  pontuacao.equipeA = 0;
  pontuacao.equipeB = 0;
  eventos = [];
  document.getElementById("pontuacaoEquipeA").innerText = pontuacao.equipeA;
  document.getElementById("pontuacaoEquipeB").innerText = pontuacao.equipeB;
  alert("O jogo foi reiniciado.");
}

function voltarParaOpcoes() {
  document.getElementById("opcoes").style.display = "block";
  document.getElementById("jogo").style.display = "none";
  document.getElementById("voltar").style.display = "none";
}
