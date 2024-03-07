package br.com.fiap.main;

import java.util.ArrayList;
import java.util.List;
import javax.swing.JOptionPane;
import br.com.fiap.beans.Livro;

public class ArrayListLivro {
	
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
		// Preparar a Lista
		List<Livro> ListaLivros = new ArrayList<Livro>();
		
		// Preparar objLivro
		Livro objLivro;
		
		// Entrada
		do {
			objLivro = new Livro();
			objLivro.setCodigo(inteiro("Codigo do Livro"));
			objLivro.setNome(texto("Nome do Livro"));
			objLivro.setEditora(texto("Editora"));
			objLivro.setValor(real("Valor do Livro"));
			
			ListaLivros.add(objLivro);
			
			
		} while ( JOptionPane.showConfirmDialog(null, "Registrar mais Livros?",
				"CADASTRO DE LIVROS", JOptionPane.YES_NO_OPTION,
				JOptionPane.QUESTION_MESSAGE) ==0);
		
		//Para ArrayList, saida utilizando o foreach
		for (Livro livro : ListaLivros) {
			System.out.println("\n\nCodigo: " + livro.getCodigo() +
					          "\nNome: " + livro.getNome() + 
					          "\nEditora: " + livro.getEditora() + 
					          "\nValor " + livro.getValor());
		}

	}

}
