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
		objetoCliente.setEmail(JOptionPane.showInputDialog("Digite o email: "));
		objetoCliente.setIdade(Integer.parseInt
				(JOptionPane.showInputDialog("Digite a Idade: ")));
		
		objetoCliente.setValorConsulta(Double.parseDouble
				(JOptionPane.showInputDialog("Digite o valor da consulta: ")));
		
		
		//Saídas:
		System.out.println("Nome: " + objetoCliente.getNome() + "\n" +
				"Email: " + objetoCliente.getEmail() + "\n" +
				"Idade: " + objetoCliente.getIdade() + "\n" +
				"Valor da consulta: " + objetoCliente.getvalorConsulta());
	}

}
