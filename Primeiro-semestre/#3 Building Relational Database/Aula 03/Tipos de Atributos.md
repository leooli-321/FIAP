# 🗃️ Modelagem de Dados em Bancos de Dados

O design de entidades e atributos em um banco de dados é uma parte fundamental da modelagem de dados. Vamos explorar esses conceitos, incluindo atributos compostos, atributos multivalorados, chaves primárias (primary keys) e chaves estrangeiras (foreign keys).


## 📦 Entidades

As entidades representam objetos, conceitos ou itens do mundo real que você deseja armazenar e gerenciar em um banco de dados. Exemplos de entidades podem incluir "Cliente", "Produto", "Pedido" e assim por diante.

## 📄 Atributos

Os atributos são características ou propriedades que descrevem uma entidade. Cada entidade possui vários atributos que definem suas características. Por exemplo, para a entidade "Cliente", os atributos podem incluir "Nome", "Endereço" e "Telefone".


## 🏠 Atributos Compostos

Atributos compostos são aqueles que podem ser divididos em partes menores, chamadas componentes, cada uma com seu próprio significado. Por exemplo, um atributo composto "Endereço" pode ser dividido em "Rua", "Cidade", "Estado" e "CEP".


## 🎨 Atributos Multivalorados

Atributos multivalorados são aqueles que podem ter múltiplos valores para uma única entidade. Por exemplo, a entidade "Produto" pode ter um atributo multivalorado "Cores Disponíveis", que inclui várias cores para um único produto.


## 🔑 Chaves Primárias (Primary Keys)

A chave primária é um atributo ou conjunto de atributos que identifica exclusivamente cada registro em uma tabela. Ela garante que não haja duplicatas de registros na tabela. A chave primária é fundamental para a integridade dos dados e a capacidade de vincular registros em tabelas relacionadas.


## 🔗 Chaves Estrangeiras (Foreign Keys)

Uma chave estrangeira é um atributo ou conjunto de atributos em uma tabela que estabelece uma relação com a chave primária de outra tabela. Ela é usada para criar relacionamentos entre as tabelas. As chaves estrangeiras permitem a implementação de integridade referencial, garantindo que os relacionamentos entre as entidades sejam mantidos.


### Exemplo: Sistema de Vendas Online 🛒

- A entidade "Produto" pode ter atributos como "ID do Produto", "Nome do Produto" e "Preço".
- A entidade "Pedido" pode ter atributos como "ID do Pedido", "Data do Pedido" e "Total do Pedido".
- A entidade "Item de Pedido" pode ser usada para representar produtos em um pedido e pode ter uma chave estrangeira que faz referência ao "ID do Produto" e ao "ID do Pedido".
- A chave primária da entidade "Produto" seria o "ID do Produto", enquanto a chave primária da entidade "Pedido" seria o "ID do Pedido".

O design adequado de entidades, atributos, chaves primárias e chaves estrangeiras é crucial para a construção de um banco de dados eficaz e bem-estruturado, que permita a representação precisa das informações e a execução de consultas eficientes.
