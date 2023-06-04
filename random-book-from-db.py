import boto3
import random
import json
from decimal import Decimal

# Custom JSON encoder to handle Decimal values
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

# Create a connection to DynamoDB Local
dynamodb = boto3.resource('dynamodb', 
                          aws_access_key_id="dummy",
                          aws_secret_access_key="dummy",
                          region_name="local",
                          endpoint_url='http://localhost:8000')

# Specify the table name
table_name = 'Books'

# Get a reference to the table
table = dynamodb.Table(table_name)

# Scan the table to get all items
response = table.scan()
items = response['Items']

# Select a random book
random_book = random.choice(items)

# Convert the book to JSON
json_book = json.dumps(random_book, cls=DecimalEncoder)

# Print the JSON representation of the random book
print(json_book)