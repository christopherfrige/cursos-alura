import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "TesteClient"

# Criando o Client DynamoDB
dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")

# Criando o Recurso DynamoDB "Table"
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)