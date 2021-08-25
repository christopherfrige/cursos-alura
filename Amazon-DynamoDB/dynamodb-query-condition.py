import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "TesteDynamo2"

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)

response = table.query(
  # Usado geralmente para retornar mais de um item com Keys iguais
  # Se possui só o Hash, o query normal já basta
  # Condições funcionam melhor quando há Hash + Range key
  KeyConditionExpression=Key('marketplace').eq('magazineluiza')
)
print(response['Items'])
