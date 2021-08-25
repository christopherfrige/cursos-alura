import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "TesteDynamo2"

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)

response = table.get_item(
    Key={
        "marketplace": "magazineluiza"
    }
)
print(response['Item']['texto'])