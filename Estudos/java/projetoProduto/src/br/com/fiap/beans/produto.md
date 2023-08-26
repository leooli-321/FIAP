# Classe `Produto` 📦

O código Java a seguir define a classe "Produto" no pacote "br.com.fiap.beans", representando um conceito de produto com o atributo "nome". Vamos analisá-lo em detalhes:

## Declaração da Classe 📝

A linha `public class Produto {` inicia a declaração da classe chamada "Produto".

## Atributo "nome" 🏷️

O atributo `private String nome;` é declarado como "private", indicando que seu acesso se limita à própria classe. Ele é do tipo `String` e representa o nome do produto.

## Método Setter 📥

O método `setNome(String nome)` é um setter, utilizado para definir (ou "setar") o valor do atributo "nome". Ele recebe uma String denominada "nome" como parâmetro e atribui esse valor ao atributo da classe utilizando o operador `this.nome = nome;`.

## Método Getter 📤

O método `getNome()` é um getter, usado para obter (ou "pegar") o valor do atributo "nome". Ele simplesmente retorna o valor atual do atributo.

Em resumo, a classe "Produto" possui um atributo "nome" que pode ser acessado e modificado por meio dos métodos setter e getter. Isso exemplifica o encapsulamento, princípio da programação orientada a objetos que visa proteger os atributos da classe, permitindo acesso e modificação apenas por métodos controlados. Essa prática ajuda a manter a integridade dos dados e facilita a manutenção do código. 🛡️💻
