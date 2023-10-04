package br.com.fiap.beans;

public class Endereco {

	// Visibilidade, tipo de dado e variável
	private String logradouro;
	private String cep;
	private int numero;
	

	// Método construtor vazio
	public Endereco() {
		super();
	}
	
	// Método construtor cheio
	public Endereco(String logradouro, String cep, int numero) {
		super();
		this.logradouro = logradouro;
		this.cep = cep;
		this.numero = numero;
	}

	// Setters (saída) e Getters (Exibir\ Retornar)
	public String getLogradouro() {
		return logradouro;
	}
	public void setLogradouro(String logradouro) {
		this.logradouro = logradouro;
	}
	public String getCep() {
		return cep;
	}
	public void setCep(String cep) {
		this.cep = cep;
	}
	public int getNumero() {
		return numero;
	}
	public void setNumero(int numero) {
		this.numero = numero;
	}
}
