package br.com.fiap.main;

import javax.swing.JOptionPane;

import br.com.fiap.beans.Cliente;

public class testeCliente {

	public static void main(String[] args) {
		
		// Instanciar objetos
		
		Cliente objetoCliente = new Cliente();
		
		
		// Entrada (input)
		objetoCliente.setNome
		(JOptionPane.showInputDialog
				("Digite o nome do cliente: ")
		);
		
		objetoCliente.setEmail
			(JOptionPane.showInputDialog
				("Digite o email do cliente: ")
		);
		
		objetoCliente.setIdade(Integer.parseInt
			(JOptionPane.showInputDialog
				("Digite a idade do cliente:")
		));
		
		objetoCliente.setValorConsulta
			(Double.parseDouble
				(JOptionPane.showInputDialog
						("Digite o valor da consulta: ")
		));
		
		
		// Saída (output)
		System.out.println("Nome: " + objetoCliente.getNome() + 
				"\nEmail: " + objetoCliente.getEmail() +
				"\nIdade: " + objetoCliente.getIdade() +
				"\nValor da Consulta: " + objetoCliente.getValorConsulta());
		
	}

}
