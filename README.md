# API REST Simples com Flask

Este projeto implementa uma API REST simples utilizando o framework Flask em Python. Uma API REST (Representational State Transfer) é uma interface que permite a comunicação entre sistemas, normalmente utilizando o protocolo HTTP.

## Funcionalidades

### CRUD
O código implementa as operações CRUD (Create, Read, Update, Delete) para gerenciar uma lista de itens:

- **Create (Criar):** Adiciona novos itens à lista.
- **Read (Ler):** Recupera informações sobre os itens existentes.
- **Update (Atualizar):** Modifica os dados de um item existente.
- **Delete (Deletar):** Remove itens da lista.

### Rotas
Cada rota define uma URL e um método HTTP (GET, POST, PUT, DELETE) que o servidor pode processar.

- **GET `/items`:** Retorna todos os itens.
- **GET `/items/<id>`:** Retorna um item específico com base no ID.
- **POST `/items`:** Cria um novo item.
- **PUT `/items/<id>`:** Atualiza um item existente com base no ID.
- **DELETE `/items/<id>`:** Deleta um item com base no ID.

### JSON
Os dados são enviados e recebidos no formato JSON, que é amplamente utilizado em APIs web por sua simplicidade e fácil integração com diversas linguagens de programação.
