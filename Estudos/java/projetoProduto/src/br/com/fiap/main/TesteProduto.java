package br.com.fiap.main;

import br.com.fiap.beans.Produto;

public class TesteProduto {

	public static void main(String[] args) {
		// Instânciar objeto
		// Input / Output
		Produto objetoProduto = new Produto(); // Para exibir o que foi escrito

		// Entrada
		objetoProduto.setNome("Leo Oli");

		// Saída
		System.out.println("Nome: " + objetoProduto.getNome());

	}

}
