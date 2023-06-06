import boto3
import hashlib
from datetime import datetime

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="dummy",
                          aws_secret_access_key="dummy",
                          region_name="local",
                          endpoint_url='http://localhost:8000')

table_name = 'Users'
table = dynamodb.Table(table_name)

def hash_password(password, userid):
    password = password + userid + "zLp0aOqfM5psX909Oj4oshRSExDRMx0jPrWMRQyB"
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

def add_user(email, password):
    hashed_password = hash_password(password, email)
    create_date = datetime.now()

    item = {
        'user_id': email,
        'password': hashed_password,
        #'create_date': create_date
    }

    table.put_item(Item=item)
    print("User added successfully.")

add_user('example@example.com', 'password123')
add_user('test@test.com','password123')