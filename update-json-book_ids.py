import json

filename = "more_books_data_temp.json"
# Define your chosen start value for book_id
start_value = 21

# Load the JSON dataset from the file
with open(filename, encoding='utf-8') as file:
    books_data = json.load(file)

# Update the book_id fields with auto-incrementing values
for i, book in enumerate(books_data):
    book['book_id'] = start_value + i

# Convert the updated dataset back to JSON
updated_books_data = json.dumps(books_data, indent=4, ensure_ascii=False)

# Write the updated dataset to a new file
with open('updated_books_data.json', 'w') as file:
    file.write(updated_books_data)

print("Book dataset updated and saved to 'updated_books_data.json'")