# 🚗 API de Gerenciamento de Carros (Flask)

Uma API simples desenvolvida com **Flask** para gerenciar uma lista de carros — permitindo **consultar, adicionar, atualizar e excluir** registros.  
Ideal para fins de estudo ou como base para projetos RESTful em Python.

---

## 📋 Funcionalidades

| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| **GET** | `/carros` | Retorna todos os carros cadastrados |
| **GET** | `/carros/<id>` | Retorna um carro específico pelo ID |
| **POST** | `/carros` | Adiciona um novo carro |
| **PUT** | `/carros/<id>` | Atualiza um carro existente |
| **DELETE** | `/carros/<id>` | Remove um carro do sistema |

---

## 🧱 Estrutura de Dados

Cada carro é representado por um dicionário com os seguintes campos:

```json
{
  "id": 1,
  "montadora": "Fiat",
  "modelo": "Mobi",
  "ano": 2026
}

<h2>📄 Licença</h2>
<p>Este projeto está licenciado sob a <a href="LICENSE">MIT License</a>.</p>
    
<h2>🤝 Contribuição</h2>

<p>Fique à vontade para abrir issues e enviar pull requests para melhorias no projeto!</p>
    
<h2>📞 Contato</h2>
<p>Caso tenha dúvidas ou sugestões, entre em contato:</p>
<ul>
    <li>📧 Email: <a href="mailto:santossilvahenrygabriel58@gmail.com">Meu email de contato</a></li>
    <li>🔗 LinkedIn: <a href="www.linkedin.com/in/henry-gabriel-santos-silva-6ba776209">Meu Perfil linkedin</a></li>
</ul>
    
<hr>
    
<p>⭐ Se gostou do projeto, deixe um star no repositório!</p>