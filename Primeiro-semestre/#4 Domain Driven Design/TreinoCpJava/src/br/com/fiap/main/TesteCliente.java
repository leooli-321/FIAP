package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Colaborador;
import br.com.fiap.beans.Endereco;

public class TesteCliente {

	public static void main(String[] args) {
		
		// Instanciar objetos
		Cliente objetoCliente = new Cliente();
		Endereco objetoEndereco = new Endereco();
		Colaborador objetoColaborador = new Colaborador();
		
		// Entradas:
		
		//Cliente
		objetoCliente.setNome("Zé da manga");
		objetoCliente.setIdade(24);
		objetoCliente.setEmail("zé@manga.com");
		
		//Endereco
		objetoEndereco.setBairro("luul");
		objetoEndereco.setCep("00000000");
		objetoEndereco.setLogradouro("Não há");
		objetoEndereco.setNumero(69);

		//Colaborador
		objetoColaborador.setCargo("Agiota");
		objetoColaborador.setNome("Zé neto");
		objetoColaborador.setRg("4587894564");
		objetoColaborador.setSalario(269.500);
		
		//Saídas
		System.out.println("Nome do Cliente: " + objetoCliente.getNome());
		System.out.println("Idade do Cliente: " + objetoCliente.getIdade());
		System.out.println("Email do Cliente: " + objetoCliente.getEmail());
		
		System.out.println("Endereço: " + objetoEndereco.getBairro());
		System.out.println("Endereço: " + objetoEndereco.getCep());
		System.out.println("Endereço: " + objetoEndereco.getLogradouro());
		System.out.println("Endereço: " + objetoEndereco.getNumero());
		
		System.out.println("Cargo do colaborador: " + objetoColaborador.getCargo());
		System.out.println("Nome do Colaborador: " + objetoColaborador.getNome());
		System.out.println("RG do Colaborador: " + objetoColaborador.getRg());
		System.out.println("Salário do Colaborador: " + objetoColaborador.getSalario());
	}

}
