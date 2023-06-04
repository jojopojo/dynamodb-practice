from flask import Flask, Response
import json
import boto3

app = Flask(__name__)

@app.route('/api/books')
def get_books():
    dynamodb = boto3.resource('dynamodb')
    table_name = 'Books'
    table = dynamodb.Table(table_name)
    response = table.scan()
    items = response['Items']
    
    json_books = json.dumps(items, ensure_ascii=False).encode('utf-8')
    
    return Response(json_books, content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run(port=8181)