package br.com.fiap.main;

import br.com.fiap.beans.Colaborador;
import br.com.fiap.beans.Loja;
import br.com.fiap.beans.Produto;

public class TesteSistemaLoja {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Instanciar Objetos
		
		Loja objLoja = new Loja();
		Produto objProduto = new Produto();
		Colaborador objColaborador = new Colaborador();
		
		//Entrada 
		//Loja
		objLoja.setCnpj("cnpj");
		objLoja.setRazaoSocial("Zé da Manga");
		objLoja.setUnidade(6);
		
		//Produto
		objProduto.setMarca("Manguinha boa de qualidade");
		objProduto.setQuantidade(1);
		objProduto.setTipo("Manga");
		objProduto.setValor(3.59);

		//Colaborador
		objColaborador.setCargo("CEO");
		objColaborador.setIdade(37);
		objColaborador.setNome("José from Mangas");
		objColaborador.setSalario(12.90);
		
		//Saídas
		//Loja
		System.out.println("CNPJ: " + objLoja.getCnpj() +
				"\nRazão Social: " + objLoja.getRazaoSocial() +
				"\nUnidade: " + objLoja.getUnidade());
		
		//Produto
		System.out.println("Marca: " + objProduto.getMarca() +
				"\nQuantidade: " + objProduto.getQuantidade() +
				"\nTipo: " + objProduto.getTipo() +
				"\nValor: " + objProduto.getValor());
		
		//Colaborador
		System.out.println("Cargo: " + objColaborador.getCargo() +
				"\nIdade: " + objColaborador.getIdade() +
				"\nNome: " + objColaborador.getNome() +
				"\nSalario: " + objColaborador.getSalario() );
		
		
	}

}
