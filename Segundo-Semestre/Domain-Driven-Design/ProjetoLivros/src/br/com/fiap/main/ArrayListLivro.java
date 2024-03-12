package br.com.fiap.main;

import java.util.ArrayList;
import java.util.List;
import javax.swing.JOptionPane;
import br.com.fiap.beans.Carro;

public class ArrayListCarro {
	
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
		List<Carro> ListaCarros = new ArrayList<Carro>();
		
		// Preparar objCarro
		Carro objCarro;
		
		// Entrada
		do {
			objCarro = new Carro();
			objCarro.setMarca(texto("Marca do Carro"));
			objCarro.setModelo(texto("Modelo do Carro"));
			objCarro.setAno(inteiro("Ano do Carro"));
			objCarro.setValor(real("Valor do Carro"));
			
			ListaCarros.add(objCarro);
			
			
		} while ( JOptionPane.showConfirmDialog(null, "Registrar mais Carros?",
				"CADASTRO DE CARROS", JOptionPane.YES_NO_OPTION,
				JOptionPane.QUESTION_MESSAGE) ==0);
		
		//Para ArrayList, saida utilizando o foreach
		for (Carro carro : ListaCarros) {
			System.out.println("\n\nMarca: " + carro.getMarca() +
					          "\nModelo: " + carro.getModelo() + 
					          "\nAno: " + carro.getAno() + 
					          "\nValor: " + carro.getValor());
		}

	}

}
