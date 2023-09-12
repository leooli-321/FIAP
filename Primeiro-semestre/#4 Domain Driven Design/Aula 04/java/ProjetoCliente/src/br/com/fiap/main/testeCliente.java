package br.com.fiap.main;

import javax.swing.JOptionPane;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Endereco;

public class testeCliente {

	public static void main(String[] args) {
		
		// Instanciar objetos
		
		Cliente objetoCliente = new Cliente();
		Endereco objetoEndereco = new Endereco();
		
		
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
		
		objetoEndereco.setLogradouro(JOptionPane.showInputDialog
				("Digite o logradouro do cliente: ")
		);
		
		
		
		// Saída (output)
		System.out.println("Nome: " + objetoCliente.getNome() + 
				"\nEmail: " + objetoCliente.getEmail() +
				"\nIdade: " + objetoCliente.getIdade() +
				"\nValor da Consulta: " + objetoCliente.getValorConsulta() +
				"\nLogradouro: " + objetoEndereco.getLogradouro());
		
	}

}
