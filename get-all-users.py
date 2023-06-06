import boto3

dynamodb = boto3.resource('dynamodb',                    
                          aws_access_key_id="dummy",
                          aws_secret_access_key="dummy",
                          region_name="local",
                          endpoint_url='http://localhost:8000')
table_name = 'Users'
table = dynamodb.Table(table_name)


def list_users():
    response = table.scan()
    users = response.get('Items', [])
        
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        users.extend(response.get('Items', []))
    
    return users


# Usage example
all_users = list_users()
for user in all_users:
    print(user)