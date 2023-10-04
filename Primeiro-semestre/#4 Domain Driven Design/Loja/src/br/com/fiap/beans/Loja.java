package br.com.fiap.beans;

public class Loja {
	
	//Visibilidade, tipo de dado e variável
	private String cnpj;
	private String razaoSocial;
	private int unidade;
	private Produto produto; // << Primeiro é MAIÚSCULO
	
	public String getCnpj() {
		return cnpj;
	}
	public void setCnpj(String cnpj) {
		this.cnpj = cnpj;
	}
	public String getRazaoSocial() {
		return razaoSocial;
	}
	public void setRazaoSocial(String razaoSocial) {
		this.razaoSocial = razaoSocial;
	}
	public int getUnidade() {
		return unidade;
	}
	public void setUnidade(int unidade) {
		this.unidade = unidade;
	}
	public Produto getProduto() {
		return produto;
	}
	public void setProduto(Produto produto) {
		this.produto = produto;
	}
	
	
	// Setters (entrada) e Getters (exibição)

}
