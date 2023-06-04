from flask import Flask, jsonify, Response
import json
import random
import boto3
from decimal import Decimal

app = Flask(__name__)

# Custom JSON encoder to handle Decimal values
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

@app.route('/api/books')
def get_books():
    dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="dummy",
                          aws_secret_access_key="dummy",
                          region_name="local",
                          endpoint_url='http://localhost:8000')
    table_name = 'Books'
    table = dynamodb.Table(table_name)
    response = table.scan()
    items = response['Items']
    
    json_books = json.dumps(items, ensure_ascii=False, cls=DecimalEncoder).encode('utf-8')
    
    return Response(json_books, content_type='application/json; charset=utf-8')

@app.route('/api/books/random')
def get_random_book():
    dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="dummy",
                          aws_secret_access_key="dummy",
                          region_name="local",
                          endpoint_url='http://localhost:8000')
    table_name = 'Books'
    table = dynamodb.Table(table_name)
    response = table.scan()
    items = response['Items']
    
    random_book = random.choice(items)
    
    return jsonify(random_book)

@app.route('/api/books/<name>')
def get_book_by_name(name):
    dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="dummy",
                          aws_secret_access_key="dummy",
                          region_name="local",
                          endpoint_url='http://localhost:8000')
    table_name = 'Books'
    table = dynamodb.Table(table_name)
    
    response = table.scan(FilterExpression='book_name = :name', ExpressionAttributeValues={':name': name})
    items = response['Items']
    
    if len(items) > 0:
        return jsonify(items[0])
    else:
        return jsonify({'error': 'Book not found'})

if __name__ == '__main__':
    app.run(port=8181)