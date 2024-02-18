package br.com.fiap.conections;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConexaoFactory {
	
	// Método de conexão com o Banco de Dados
	public Connection conexao() throws ClassNotFoundException, SQLException {
		
		// Driver
		Class.forName("oracle.jdbc.driver.OracleDriver");
		
		//Retornar a Conexão
		return DriverManager.getConnection("jbdc:oracle:thin:@oracle.fiap.com.br:1521:orcl", 
				"rm554024", "fiap23");
	}

}
