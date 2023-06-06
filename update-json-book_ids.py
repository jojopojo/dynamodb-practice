import json
import time
import random

filename = "books_data.json"
# Define your chosen start value for book_id
start_value = 21

# Load the JSON dataset from the file
with open(filename, encoding='utf-8') as file:
    books_data = json.load(file)

# Update the book_id fields with auto-incrementing values
for i, book in enumerate(books_data):
    book['book_id'] = int( str(int(time.time() * 1_000_000)) + "" + str(random.randrange(100000,999999)))

# Convert the updated dataset back to JSON
updated_books_data = json.dumps(books_data, indent=4, ensure_ascii=False)

# Write the updated dataset to a new file
with open('updated_books_data.json', 'w', encoding='utf-8') as file:
    file.write(updated_books_data)

print("Book dataset updated and saved to 'updated_books_data.json'")