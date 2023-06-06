import boto3
#doesn't work
dynamodb = boto3.client('dynamodb', 
                          aws_access_key_id="dummy",
                          aws_secret_access_key="dummy",
                          region_name="local",
                          endpoint_url='http://localhost:8000')
table_name = 'Books'

response = dynamodb.delete_table(
    TableName=table_name
)

print(f"Table '{table_name}' deleted successfully.")