import boto3
from botocore.exceptions import NoCredentialsError

# Create a connection to DynamoDB Local
dynamodb = boto3.resource('dynamodb', 
                          aws_access_key_id="dummy",
                          aws_secret_access_key="dummy",
                          region_name="local",
                          endpoint_url='http://localhost:8000')

# Define table name and attribute definitions
table_name = 'Books'
attribute_definitions = [
    {
        'AttributeName': 'book_id',
        'AttributeType': 'N'  # N represents a number
    }
]

# Define the key schema for the table
key_schema = [
    {
        'AttributeName': 'book_id',
        'KeyType': 'HASH'  # HASH represents the partition key
    }
]

# Define the provisioned throughput for the table (adjust according to your needs)
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Create the table
try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput
    )

    # Wait for the table to be created
    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

    # Print the status
    print(f"Table '{table_name}' created successfully!")
except NoCredentialsError:
    print("Local DynamoDB credentials not found. Make sure you have started DynamoDB Local.")