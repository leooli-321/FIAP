let gameStarted = false;

document.addEventListener("keydown", (event) => {
  if (!gameStarted) {
    gameStarted = true;
    document.getElementById("startScreen").style.display = "none";
  // Inicie o jogo aqui
  const mario = document.querySelector(".mario");
  const pipe = document.querySelector(".pipe");
  const scoreDisplay = document.getElementById("score");
  const highScoreDisplay = document.getElementById("highScore");
  const gameOverScreen = document.getElementById("gameOverScreen");
  const gameOverSound = document.getElementById("gameOverSound");
  const nicePointsSound = document.getElementById("nicePointsSound");

  let score = 0;
  let highScore = localStorage.getItem("highScore") || 0;
  let canDoubleJump = true;

  const jump = () => {
    mario.classList.add("jump");
    setTimeout(() => {
      mario.classList.remove("jump");
    }, 500); // Ajuste este valor conforme necessário
  };

  const handleJump = (event) => {
    event.preventDefault();
    if (!mario.classList.contains("jump")) {
      if (canDoubleJump) {
        canDoubleJump = false;
        jump();
      } else {
        jump();
        canDoubleJump = true;
      }
    }
  };

  const gameLoop = () => {
    const pipePosition = pipe.offsetLeft;
    const marioPosition = parseInt(window.getComputedStyle(mario).bottom);

    if (pipePosition <= 100 && pipePosition > 0 && marioPosition < 60) {
      pipe.style.animation = "none";
      pipe.style.left = `${pipePosition}px`;
      mario.style.animation = "none";
      mario.style.bottom = `${marioPosition}px`;

      mario.src = "./img/game-over.png";
      mario.style.width = "75px";
      mario.style.marginLeft = "50px";

      gameOverScreen.style.display = "flex";
      gameOverSound.play();

      if (score > highScore) {
        highScore = score;
        localStorage.setItem("highScore", highScore);
      }

      cancelAnimationFrame(gameLoop);

      setTimeout(() => {
        location.reload();
      }, 2500);
    } else {
      score++;
      scoreDisplay.textContent = `Pontuação: ${score}`;
      highScoreDisplay.textContent = `Recorde: ${highScore}`;

      // Adicione um efeito de troca de cores quando a pontuação for um múltiplo de 1000
      if (score % 1000 === 0) {
        scoreDisplay.style.color =
          scoreDisplay.style.color === "red" ? "blue" : "red";
        scoreDisplay.classList.add("text-flicker-out-glow");
        nicePointsSound.play();
        setTimeout(() => {
          scoreDisplay.style.color = "black";
          scoreDisplay.classList.remove("text-flicker-out-glow");
        }, 2500);
      }
    }

    requestAnimationFrame(gameLoop);
  };

  requestAnimationFrame(gameLoop);

  document.addEventListener("keydown", handleJump);
  document.addEventListener("touchstart", handleJump, { passive: false });
}
});