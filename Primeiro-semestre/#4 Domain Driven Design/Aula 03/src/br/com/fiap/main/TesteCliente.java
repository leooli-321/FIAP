package br.com.fiap.main;

import br.com.fiap.beans.Cliente;

public class TesteCliente {

	public static void main(String[] args) {
			
		// Instanciar objeto 
		Cliente objetoCliente = new Cliente();

		// Entrada 
		objetoCliente.setNome("Leo Oli");
		objetoCliente.setIdade(27);
		objetoCliente.setValor(350);
		
		// Saídas
		System.out.println("Nome: " + objetoCliente.getNome() + 
				"\nIdade: " + objetoCliente.getIdade() +
				"\nValor da Consulta: " + objetoCliente.getValor() );
		
	}

}