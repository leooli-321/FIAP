package br.com.caism.beans;

public class FichaPaciente {
	
	// Visibilidade, Tipo de Dado e Variável:
	private String nomePaciente;
	private String religiao;
	private String estadoCivil;
	private String email;
	private double telefone;
	private int idade;
	private double cpf;
	
	
	// Setters
	public void setNomePaciente (String nomePaciente) {
		this.nomePaciente = nomePaciente;	
	}
	
	public void setReligiao (String religiao) {
		this.religiao = religiao;
	}
	
	public void setEstadoCivil (String estadoCivil) {
		this.estadoCivil = estadoCivil;
	}
	
	public void setEmail (String email) {
		this.email = email;
	}
	
	public void setTelefone (double telefone) {
		this.telefone = telefone;
	}
	
	public void setIdade (int idade) {
		this.idade = idade;
	}
	
	public void setCpf (double cpf) {
		this.cpf = cpf;
	}


	// Getters
	public String getNomePaciente () {
		return nomePaciente;
	}
	
	public String getReligiao () {
		return religiao;
	}
	
	public String getEstadoCivil () {
		return estadoCivil;
	}
	
	public String getEmail () {
		return email;
	}
	
	public double getTelefone () {
		return telefone;
	}
	
	public int getIdade () {
		return idade;
	}
	
	public double getCpf () {
		return cpf;
	}

	public void cpf(double d) {
		// TODO Auto-generated method stub
		
	}
	
}
