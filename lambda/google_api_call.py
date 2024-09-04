import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv('API_KEY')
query = input('Book?:')

base_url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'


book_response = requests.get(base_url)

#print(book_response)

if book_response.status_code == 200:
    #store the json repsonse
    book_data = book_response.json()

    #three closest books to book searched
    top_three_books = []

    for book_number in range(3):
        top_three_books.append(book_data['items'][book_number]['volumeInfo'])
        
    for book in top_three_books:
        print(book.get('description'), '\n')
    

