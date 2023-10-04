package br.com.fiap.beans;

public class Colaborador {
	
	// Visibilidade, tipo de dado e variável
	private String nome;
	private String cargo;
	private double salario;

	
	// Método construtor vazio
	public Colaborador() {
		super();
	}
	
	// Método construtor cheio
	public Colaborador(String nome, String cargo, double salario) {
		super();
		this.nome = nome;
		this.cargo = cargo;
		this.salario = salario;
	}

	// Setters and Getters
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCargo() {
		return cargo;
	}

	public void setCargo(String cargo) {
		this.cargo = cargo;
	}
		

}
