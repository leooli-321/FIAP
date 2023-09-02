package br.com.fiap.main;

import javax.swing.JOptionPane;

import br.com.fiap.beans.Cliente;

public class TesteCliente {

	public static void main(String[] args) {
		
		// Instânciar objetos:
		Cliente objetoCliente = new Cliente();
		
		// Entrada:
		objetoCliente.setNome("Leo Oli");
		objetoCliente.setEmail("leo@oli.com");
		objetoCliente.setIdade(27);
		objetoCliente.setValorConsulta(349.70);
		
		
		// Instânciar objetos:
		Cliente objetoClienteDois = new Cliente();
		
		
		// Entrada:
		objetoCliente.setNome(JOptionPane.showInputDialog("Digite o nome: "));
		objetoCliente.setEmail("maira@kikuchi.com");
		objetoCliente.setIdade(20);
		objetoCliente.setValorConsulta(249.99);
		
		
		//Saídas:
		System.out.println("Nome: " + objetoCliente.getNome() + "\n" +
				"Email: " + objetoCliente.getEmail() + "\n" +
				"Idade: " + objetoCliente.getIdade() + "\n" +
				"Valor da consulta: " + objetoCliente.getvalorConsulta());
	}

}
