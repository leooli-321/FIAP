package br.com.fiap.main;

import javax.swing.JOptionPane;
import br.com.fiap.beans.Carro;

public class VetorCarro {
	
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
		Carro[] vetorCarro = new Carro [2]; // [0]  [1]
		
		//Preparar indice
		int indice= 0;
		
		//Entrada
		do {
			vetorCarro[indice] = new Carro();
			vetorCarro[indice].setMarca(texto("Marca do Carro"));
			vetorCarro[indice].setModelo(texto("Modelo do Carro"));
			vetorCarro[indice].setAno(inteiro("Ano do Carro"));
			vetorCarro[indice].setValor(real("Valor do Carro"));
			
			indice ++;
			
		} while (JOptionPane.showConfirmDialog(null, "Adicionar mais Carros?",
				"CADASTRO DE CARROS", JOptionPane.YES_NO_OPTION,
				JOptionPane.QUESTION_MESSAGE) ==0);
		
		// Para Vetor, saidas utilizando for
		for (int contador = 0; contador < indice; contador ++) {
			System.out.println("\n\nMarca: " + vetorCarro[contador].getMarca()+
					           "\nModelo: " + vetorCarro[contador].getModelo()+
					           "\nAno: " + vetorCarro[contador].getAno() +
					           "\nValor: " + vetorCarro[contador].getValor());
		}

	}

}
