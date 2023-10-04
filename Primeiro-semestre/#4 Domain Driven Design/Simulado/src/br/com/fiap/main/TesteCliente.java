package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Documento;

public class TesteCliente {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Cliente objCliente = new Cliente();
		Documento objDocumento = new Documento();
		
		objCliente.setNome("Braufas");
		objCliente.setIdade(28);
		objCliente.setPagamento(19.90);
		
		objDocumento.setCpf("12312312323");
		objDocumento.setRg("121231231");
		
		System.out.println("Nome: " + objCliente.getNome() +
				"\nIdade: " + objCliente.getIdade() +
				"\nPagamento: " + objCliente.getPagamento() +
				"\nCPF: " + objDocumento.getCpf() +
				"\nRG: " + objDocumento.getRg()
				);
		
	}

}
