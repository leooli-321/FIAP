package br.com.fiap.beans;

public class Produto {
	
	// Visibilidade, tipo de dados e variáveis
	
	private String tipo;
	private String marca;
	private int quantidade;
	private double valor;
	
	// Setters (entrada) e Getters (saída)
	public String getTipo() {
		return tipo;
	}
	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	public String getMarca() {
		return marca;
	}
	public void setMarca(String marca) {
		this.marca = marca;
	}
	public int getQuantidade() {
		return quantidade;
	}
	public void setQuantidade(int quantidade) {
		this.quantidade = quantidade;
	}
	public double getValor() {
		return valor;
	}
	public void setValor(double valor) {
		this.valor = valor;
	}
	
	

}
