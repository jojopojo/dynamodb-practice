import boto3
import json

# Create a connection to DynamoDB Local
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="dummy",
                          aws_secret_access_key="dummy",
                          region_name="local",
                          endpoint_url='http://localhost:8000')

# Specify the table name
table_name = 'Books'

# Load data from the JSON file
with open('updated_books_data.json') as file:
    books_data = json.load(file)

# Get a reference to the table
table = dynamodb.Table(table_name)

# Insert items into the table
with table.batch_writer() as batch:
    for book in books_data:
        batch.put_item(Item=book)

print("Data inserted successfully!")
