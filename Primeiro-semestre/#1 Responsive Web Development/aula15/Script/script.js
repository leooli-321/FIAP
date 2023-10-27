function validar() {
    nome = document.getElementById("txtUser");
    senha = document.getElementById("pwdPass");
    erroNome = document.getElementById("erroNome");

    if (nome.value == "") {
        nome.focus();
        erroNome.innerText = "DIGITE O USUÁRIO";
        return false;
    } else {
        erroNome.innerText = "";
    }

    if (senha.value == "") {
        senha.focus();
        erroSenha.innerText = "DIGITE SUA SENHA";
        return false;
    }
}
