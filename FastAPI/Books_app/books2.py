from fastapi import FastAPI, Body, Path, Query,HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
# starlete is already installed when we install fastapi
from starlette import status

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
                "rating":5,
                "published_date":2000
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

# Here HTTP_200_OK means we are explicitly defining that on sucessful request we will send a status code of 200
@app.get("/books",status_code=status.HTTP_200_OK)
async def read_All_books():
    return BOOKS



@app.get("/books/{book_id}",status_code=status.HTTP_200_OK)
#Data Validation for a path parameter using Path module
async def read_book(book_id: int= Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404,detail='Item not found')


@app.get("/books/publish/")
async def read_book(published_date: int= Query(gt=1999,lt=2031)):
    for book in BOOKS:
        if book.published_date == published_date:
            return book
        

@app.get("/books/",status_code=status.HTTP_200_OK)
# Data validation for the query parameters as same as the Book model
async def read_book_by_rating(book_rating:int= Query(gt=0,lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating ==book_rating:
            books_to_return.append(book)
    return books_to_return

# 201 status code for creation of reocrds 
@app.post("/create-book",status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.dict())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))


# 200 OR 204 
@app.put("/books/update_book",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book:BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404,detail='Item not found')


@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id : int=Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404,detail='Item not found')



