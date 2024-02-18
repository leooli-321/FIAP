package br.com.fiap.main;

import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;

import br.com.fiap.beans.Produto;

public class TesteCarrinho {
	
	// String
	static String texto(String j) {
		return JOptionPane.showInputDialog(j);
	}
	
	//int
	static int inteiro(String j) {
		return Integer.parseInt
				(JOptionPane.showInputDialog(j));
	}
	
	//Double
	static double real(String j) {
		return Double.parseDouble
				(JOptionPane.showInputDialog(j));
	}

	public static void main(String[] args) {
		//Prepara a Lista
		List<Produto> listaProdutos = new ArrayList<Produto>();
		
		Produto objProduto;
		
		//Entradas
		do {
			
			objProduto = new Produto();
			objProduto.setCodigo(inteiro("Informe o código do produto"));
			objProduto.setTipo(texto("Informe o tipo de produto"));
			objProduto.setMarca(texto("Informe a marca do Produto"));
			objProduto.setQuantidade(inteiro("Informe a quantidade"));
			objProduto.setPreco(real("Informe o valor do produto"));
			
			listaProdutos.add(objProduto);
			
		} while (JOptionPane.showConfirmDialog
				(null, "Deseja adicionar mais produtos no carrinho?",
						"CARRINHO DE COMPRAS", JOptionPane.YES_NO_OPTION, 
						JOptionPane.QUESTION_MESSAGE) ==0);
		
		// SAIDAS COM FOREACH (for)
		
	}

}
