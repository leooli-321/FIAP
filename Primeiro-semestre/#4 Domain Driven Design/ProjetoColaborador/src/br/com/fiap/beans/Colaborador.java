package br.com.fiap.beans;

public class Colaborador {
	
	//Visibilidade, tipo de dado e variável:
	private String nome;
	private double valorHora;
	private int idade;
	private double qtdadeHoras;
	private double percentual;
	private Endereco endereco;
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public double getValorHora() {
		return valorHora;
	}
	public void setValorHora(double valorHora) {
		this.valorHora = valorHora;
	}
	public int getIdade() {
		return idade;
	}
	public void setIdade(int idade) {
		this.idade = idade;
	}
	public double getQtdadeHoras() {
		return qtdadeHoras;
	}
	public void setQtdadeHoras(double qtdadeHoras) {
		this.qtdadeHoras = qtdadeHoras;
	}
	public double getPercentual() {
		return percentual;
	}
	public void setPercentual(double percentual) {
		this.percentual = percentual;
	}
	public Endereco getEndereco() {
		return endereco;
	}
	public void setEndereco(Endereco endereco) {
		this.endereco = endereco;
	}
	
	
	//Metodo get para nome e idade 
	public String getNomeIdade() {
		return "Nome: " + nome + "\nIdade: " + idade;
	}
	
	// Método worker
	public double calcularSalario() {
		return valorHora * qtdadeHoras;
	}

	//if e else
	public String pagarTaxa() {
		String informacao = null;
		if (calcularSalario() > 13600.55) {
			informacao = "Paga Taxa";
		} else {
			informacao = "Não Paga Taxa";
		}
		return informacao;
	}

}
