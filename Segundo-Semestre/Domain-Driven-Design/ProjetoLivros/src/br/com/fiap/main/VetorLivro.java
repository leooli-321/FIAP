package br.com.fiap.main;

import javax.swing.JOptionPane;
import br.com.fiap.beans.Livro;

public class VetorLivro {
	
	//String
	static String texto(String j) {
		return JOptionPane.showInputDialog(j);
	}
	
	//int
	static int inteiro(String j) {
		return Integer.parseInt(JOptionPane.showInputDialog(j));		
	}
	
	// double
	static double real(String j) {
		return Double.parseDouble(JOptionPane.showInputDialog(j));
	}

	public static void main(String[] args) {
		// Preparar vetor e definir o maximo de posições
		Livro[] vetorLivro = new Livro [2]; // [0]  [1]
		
		//Preparar indice
		int indice= 0;
		
		//Entrada
		do {
			vetorLivro[indice] = new Livro();
			vetorLivro[indice].setCodigo(inteiro("Codigo do Livro"));
			vetorLivro[indice].setNome(texto("Nome do livro"));
			vetorLivro[indice].setEditora(texto("Editora"));
			vetorLivro[indice].setValor(real("Valor do livro"));
			
			indice ++;
			
		} while (JOptionPane.showConfirmDialog(null, "Adicionar mais Livros?",
				"CADASTRO DE LIVROS", JOptionPane.YES_NO_OPTION,
				JOptionPane.QUESTION_MESSAGE) ==0);
		
		// Para Vetor, saidas utilizando for
		for (int contador = 0; contador < indice; contador ++) {
			System.out.println("\n\nCodigo: " + vetorLivro[contador].getCodigo()+
					           "\nNome: " + vetorLivro[contador].getNome()+
					           "\nEditora: " + vetorLivro[contador].getEditora() +
					           "\nValor: " + vetorLivro[contador].getValor());
		}

 		

	}

}
