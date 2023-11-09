package br.com.fiap.main;

import javax.swing.JOptionPane;

import br.com.fiap.beans.Debito;

public class TesteSistema {

	// String
	static String texto(String j) {
		return JOptionPane.showInputDialog(j);
	}

	// Int
	static int inteiro(String j) {
		return Integer.parseInt(JOptionPane.showInputDialog(j));
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Debito objD = new Debito(texto("Nome"), texto("Bandeira"), inteiro("Numero"), inteira("CVV"), real("Saldo"));

	}

}
