package br.com.fiap.beans;

public class Debito extends Cartao {

	private double consignado;

	// Construtor
	public Debito() {
		super();
	}

	// Construtor cheio com Heranca
	public Debito(String nome, String bandeira, int numero, int cvv, double saldo, double consignado) {
		super(nome, bandeira, numero, cvv, saldo);
		this.consignado = consignado;
	}

	public Debito(double consignado) {
		super();
		this.consignado = consignado;
	}

	public double getConsignado() {
		return consignado;
	}

	public void setConsignado(double consignado) {
		this.consignado = consignado;
	}
	
	public double limite() {
		return saldo - consignado;
	}

}
