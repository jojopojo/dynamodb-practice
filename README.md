# dynamodb-practice
Practicing dynamodb and Python boto3 locally

#1
docker-compose.yml 
-> for starting local DynamoDB with docker (runs localhost:8080)

books_data.json 
-> some sample data

#2
create-books.py - create the Books table

#3
add-books-from-json.py - uses the books_data.json and adds some books to Books table

#4
flask-get-books.py - starts server localhost:8181, try endpoint http://localhost:8181/api/books/random
