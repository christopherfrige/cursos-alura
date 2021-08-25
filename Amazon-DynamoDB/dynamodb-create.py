import boto3

# Inicializa o cliente
dynamodb = boto3.client("dynamodb")

response = dynamodb.create_table(
    # Nome da tabela no AWS DynamoDB
    TableName="TesteDynamo2",
    
    # Definições dos atributos de identificação
    AttributeDefinitions=[
        {
            # Nome do atributo
            "AttributeName": "marketplace",
            # Pode ser S (string), N (numero) ou B (binario).
            "AttributeType": "S"
        },
    ],
    # Aqui definirá o tipo da chave dos atributos
    KeySchema=[
        {
            "AttributeName": "marketplace",
            # HASH (obrigatorio) ou RANGE (opcional)
            # Se for criar uma RANGE, é interessante já ter uma HASH para melhor utilização
            "KeyType": "HASH"
        }
    ],
    # Geralmente deixar dessa forma (pequena escala), relaciona-se aos limites de leitura/escrita de dados 
    ProvisionedThroughput={
        "ReadCapacityUnits": 1,
        "WriteCapacityUnits": 1
  }
)
print(response)