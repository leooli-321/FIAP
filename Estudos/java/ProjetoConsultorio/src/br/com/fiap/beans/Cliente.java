package br.com.fiap.beans;

public class Cliente {
	
	// Visibilidade, Tipo de Dado e Variável:
	private String nome;
	private String email;
	private int idade; //int > valores reais/inteiros
	private double valorConsulta; //double > números quebrados
	
	
	// Setters
	public void setNome (String nome) {
		this.nome = nome;
	}
	
	public void setEmail (String email) {
		this.email = email;
	}
	
	public void setIdade (int idade) {
		this.idade = idade;
	}
	
	public void setValorConsulta (double valorConsulta) {
		this.valorConsulta = valorConsulta;
	}
	
	// Getters (Exibir as variáveis)
	public String getNome () {
		return nome;
	}
	
	public String getEmail () {
		return email;
	}
	
	public int getIdade () {
		return idade;
	}
	
	public double getvalorConsulta () {
		return valorConsulta;
	}
	
}
