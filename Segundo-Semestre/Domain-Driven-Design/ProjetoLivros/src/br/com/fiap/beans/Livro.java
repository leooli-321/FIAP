package br.com.fiap.beans;

public class Livro {
	
	private int codigo;
	private String nome;
	private String editora;
	private double valor;
	public Livro() {
		super();
	}
	public Livro(int codigo, String nome, String editora, double valor) {
		super();
		this.codigo = codigo;
		this.nome = nome;
		this.editora = editora;
		this.valor = valor;
	}
	public int getCodigo() {
		return codigo;
	}
	public void setCodigo(int codigo) {
		this.codigo = codigo;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getEditora() {
		return editora;
	}
	public void setEditora(String editora) {
		this.editora = editora;
	}
	public double getValor() {
		return valor;
	}
	public void setValor(double valor) {
		this.valor = valor;
	}
	

}
