import boto3
# This doesnt work... look at create-books.py for working script
dynamodb = boto3.resource('dynamodb', 
                          aws_access_key_id="dummy",
                          aws_secret_access_key="dummy",
                          region_name="local",
                          endpoint_url='http://localhost:8000')

table_name = 'Users'

attribute_definitions = [
    {
        'AttributeName': 'user_id',
        'AttributeType': 'S'  # N represents a number
    },
    {
        'AttributeName': 'password',
        'AttributeType': 'S'
    }
]

# Define the key schema for the table
key_schema = [
    {
        'AttributeName': 'user_id',
        'KeyType': 'HASH'  # HASH represents the partition key
    },
    {
        'AttributeName': 'password',
        'KeyType': 'RANGE'
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