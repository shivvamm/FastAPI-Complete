from fastapi import FastAPI, Body, Path, Query
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description:str
    rating:int
    published_date: int

    def __init__(self,id,title,author,description,rating,published_date):
        self.id  = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date =  published_date

# Adding  validation using pydantic for single fields
class BookRequest(BaseModel):
    id:Optional[int] = Field(description="Id is not needed as it is assigned automatically by the server",default=None)
    title:str= Field(min_length=3)
    author: str = Field(min_length=1)
    description:str  = Field(min_length=1,max_length=100)
    rating:int = Field(gt=-1, lt=6 )
    published_date:int = Field(gt=1999,lt=2031)

# For providing the exmple for the given schema 
    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"A new Book",
                "author":"shivam",
                "description":"A new book",
                "rating":5
            }
        }
    }


BOOKS = [
    Book(1,'computer science','code','A very nice book',5,2001),
    Book(2,'computer science','code','A very nice book',5,2005),
    Book(3,'computer science','code','A very nice book',4,2003),
    Book(4,'computer science','code','A very nice book',2,2000),
    Book(5,'computer science','code','A very nice book',3,2014),
    Book(6,'computer science','code','A very nice book',1,2012)
]

#Overwriting the id for proper order 
def find_book_id(book:Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    # Same as above
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id +1
    # else:
    #     book.id = 1
    return book

@app.get("/books")
async def read_All_books():
    return BOOKS

@app.get("/books/{book_id}")
#Data Validation for a path parameter using Path module
async def read_book(book_id: int= Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
        
@app.get("/books/publish/")
async def read_book(published_date: int= Query(gt=1999,lt=2031)):
    for book in BOOKS:
        if book.published_date == published_date:
            return book
        
@app.get("/books/")
# Data validation for the query parameters as same as the Book model
async def read_book_by_rating(book_rating:int= Query(gt=0,lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating ==book_rating:
            books_to_return.append(book)
    return books_to_return

@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.dict())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))


@app.put("/books/update_book")
async def update_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete("/books/{book_id}")
async def delete_book(book_id : int=Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break


