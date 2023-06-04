import boto3
import json
from decimal import Decimal

# Custom JSON encoder to handle Decimal values
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

# Create a connection to DynamoDB
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

# Convert the items to JSON
json_books = json.dumps(items, indent=4, cls=DecimalEncoder)

# Print the JSON representation of all books
print(json_books)