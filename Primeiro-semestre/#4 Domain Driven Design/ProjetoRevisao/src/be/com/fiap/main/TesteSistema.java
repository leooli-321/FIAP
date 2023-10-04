package be.com.fiap.main;

import javax.swing.JOptionPane;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Colaborador;
import br.com.fiap.beans.Endereco;

public class TesteSistema {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Cliente objCliente = new Cliente();
		Colaborador objColaborador = new Colaborador();
		Endereco objEndereco = new Endereco();
		
		//Entradas:
		objCliente.setNome(JOptionPane.showInputDialog("Digite o nome do Cliente: "));
		objCliente.setIdade(Integer.parseInt(JOptionPane.showInputDialog("Insira a idade do Cliente: ")));
		
		objEndereco.setLogradouro(JOptionPane.showInputDialog("Digite o Logradouro: "));
		objEndereco.setCep(JOptionPane.showInputDialog("Digite o CEP: "));
		objEndereco.setNumero(Integer.parseInt(JOptionPane.showInputDialog("Insira o número: ")));
		
		objCliente.setEndereco(objEndereco);
		
		//Colaborador:
		objColaborador.setNome(JOptionPane.showInputDialog("Digite o nome do colaborador: "));
		objColaborador.setCargo(JOptionPane.showInputDialog("Cargo do Colaborador: "));
		objColaborador.setSalario(Double.parseDouble(JOptionPane.showInputDialog("Salário do Colaborador: ")));
		
		System.out.println("INFORMAÇÕES DO CLIENTE" +
		"\nNOME: " + objCliente.getNome() +
		"\nIDADE: " + objCliente.getIdade() +
		"\n\n ENDEREÇO DO CLIENTE: " +
		"\nLOGRADOURO: " + objEndereco.getLogradouro() +
		"\nCEP: " + objEndereco.getCep() +
		"\nNUMERO: " + objEndereco.getNumero() +
		"\n\nINFORMAÇÕES DO COLABORADOR" +
		"\nNOME: " + objColaborador.getNome() +
		"\nCARGO: " + objColaborador.getCargo());
		
		
	}

}
