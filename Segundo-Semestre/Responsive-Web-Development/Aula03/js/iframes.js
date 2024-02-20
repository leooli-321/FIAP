let isInvulnerable = false;

if (!gameStarted) {
    gameStarted = true;
    isInvulnerable = true;
    setTimeout(() => {
      isInvulnerable = false;
    }, 3000); // Mario será invulnerável por 3 segundos
    // ...
  }
  
  if (!isInvulnerable && pipePosition <= 100 && pipePosition > 0 && marioPosition < 60) {
    // ...
  }
  