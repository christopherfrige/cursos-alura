# Estudo do Amazon DynamoDB

Diferentemente de algumas das outras pastas, essa foi um estudo individual, e não um curso em si.

## Anotações importantes: 

**Diferença entre DynamoDB Client e Resource**
-  Com o client as APIs do DynamoDB são acessados de uma maneira mais baixo nível (tendo que específicar varias coisas)
- O resource permite um acesso mais voltado a orientação a objetos.
- IMPORTANTE: se for usar o Resource, importar:
 
        from boto3.dynamodb.conditions import Key

**Maior explicação acerca da Hash e Range keys**
- HASH -> Partition Key
- Range -> Sort Key
- Compõem a chave primária
- Explicação completa [aqui](https://stackoverflow.com/questions/27329461/what-is-hash-and-range-primary-key).

**Criando tabelas**
- O código do arquivo criar_tabela_DynamoDB.py está comentado e explica os passos de criação.

**Enviando dados para a tabela**
- É possivel enviar tanto por client como por resource
- Client necessita especificar a tabela e o AttributeType de cada atributo.
- Resource não necessita especificar a tabela na hora de requisitar, mas é necessário criar um objeto Table.