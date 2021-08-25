import boto3
import json

dynamodb_client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

def upload():
    # Cria o objeto para enviar ao DynamoDB
    # "CHAVE": {"TIPO": "VALOR"}
    item = {
        "marketplace": {"S":"Magazine Luiza"},
        "texto": {"S":"Bananas de Pijamas"}
    }
    # Envia o objeto ao Dynamo (formato com dynamoDB client)
    # response = dynamodb_client.put_item(
    #    TableName = 'TesteDynamo2',
    #    Item=item
    #)

    # Envia o objeto ao Dynamo (formato com dynamoDB resource)
    table = dynamodb.Table("TesteDynamo2")
    response = table.put_item(
        Item=item
    )

    print("FAZENDO UPLOAD")
    print(response)

upload()