package br.com.fiap.main;

import javax.swing.JOptionPane;

import br.com.fiap.beans.Aluno;
import br.com.fiap.beans.Colaborador;
import br.com.fiap.beans.Endereco;

public class TesteSistema {
	
	static String texto(String j) {
		return JOptionPane.showInputDialog(j);
	}
	
	static int inteiro(int j) {
		return Integer.parseInt(JOptionPane.showInputDialog(j));
	}
	
	static double real (double j) {
		return Double.parseDouble(JOptionPane.showInputDialog(j));
	}

	public static void main(String[] args) {
		// Instanciar objetos
		
		//int rm, String nome, String turma, double nota
		Aluno objAluno = new Aluno(Integer.parseInt
				(JOptionPane.showInputDialog("Digite o RM:")),
				JOptionPane.showInputDialog("Digite o Nome do aluno:"),
				JOptionPane.showInputDialog("Digite a turma:"),
				Double.parseDouble(JOptionPane.showInputDialog
						("Digite a nota do aluno:")
						));
		
		
		//String logradouro, String cep
		Endereco objEndereco = new Endereco(texto("Digite o logradouro"),
				texto("Digite o CEP:"), Integer.parseInt
				(JOptionPane.showInputDialog("Digite o número: ")));
		
		//String nome, String cargo
		Colaborador objColaborador = new Colaborador(JOptionPane.showInputDialog("Digite o nome do colaborador:"),
				JOptionPane.showInputDialog("Digite o cargo do colaborador: "), Double.parseDouble
				(JOptionPane.showInputDialog("Digite o Salário: ")));
		
		
		//Saídas
		System.out.println("RM do aluno: " + objAluno.getRm() +
				"\nNome: " + objAluno.getNome() +
				"\nTurma: " + objAluno.getTurma() +
				"\nNota: " + objAluno.getNota());
		
		System.out.println("\nLogradouro: " + objEndereco.getLogradouro() +
				"\nCEP: " + objEndereco.getCep());
		System.out.println("\nNome do Colaborador: " + objColaborador.getNome() +
				"\nCargo: " + objColaborador.getCargo());
	}
}
