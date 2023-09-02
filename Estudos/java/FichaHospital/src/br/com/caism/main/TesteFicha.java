package br.com.caism.main;

import javax.swing.JOptionPane;

import br.com.caism.beans.FichaPaciente;

public class TesteFicha {

	public static void main(String[] args) {
		
		// Instânciar objetos:
		FichaPaciente objetoPaciente = new FichaPaciente();
		
		//Entrada:
		objetoPaciente.setNomePaciente(JOptionPane.showInputDialog
				("Nome do Paciente: "));
		objetoPaciente.setReligiao(JOptionPane.showInputDialog
				("Religião do Paciente: "));
		objetoPaciente.setEstadoCivil(JOptionPane.showInputDialog
				("Estado Civil: "));
		objetoPaciente.setEmail(JOptionPane.showInputDialog
				("Email: "));
		
		objetoPaciente.setTelefone(Double.parseDouble
				(JOptionPane.showInputDialog
						("Telefone: ")));
		
		objetoPaciente.setIdade(Integer.parseInt
				(JOptionPane.showInputDialog
						("Idade: ")));
		
		objetoPaciente.cpf(Double.parseDouble
				(JOptionPane.showInputDialog
						("CPF: ")));
		
		
		// Saídas:
		System.out.println(
				"Nome: " + objetoPaciente.getNomePaciente() +
				"\nReligião do Paciente: " + objetoPaciente.getReligiao() +
				"\nEstado Civil: " + objetoPaciente.getEstadoCivil() +
				"\nEmail: " + objetoPaciente.getEmail() +
				
				"\nTelefone: " + objetoPaciente.getTelefone() +
				"\nIdade: " + objetoPaciente.getIdade() +
				"\nCPF: " + objetoPaciente.getCpf());
	}

}
