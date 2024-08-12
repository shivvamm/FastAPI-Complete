from fastapi import  Body, FastAPI



app = FastAPI()


BOOKS = [
{'title':'Title One','author':'Author One','category':'Science'},
{'title':'Title Two','author':'Author Two','category':'Maths'},
{'title':'Title Three','author':'Author Three','category':'Science'},
{'title':'Title Four','author':'Author Four','category':'Science'},
{'title':'Title Five','author':'Author One','category':'English'},
{'title':'Title Six','author':'Author One','category':'Science'},
{'title':'Title Seven','author':'Author One','category':'Science'},
]

# FastAPI sequentially mathces for the endpoint to execute the function
# A chronological order is followed

#GET REQUEST METHOD
#Request with get method cannot have a body
@app.get("/books")
async def read_all_books():
    return BOOKS

# PATH PARAMETERS
#%20 means space in the paramerter of the url
@app.get("/books/{book_title}")
async def read_books_by_author(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        

@app.get("/books/author/{book_author}")
async def read_books(book_author: str):
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            return book


# QUERY PARAMETERS 
# The query parameter is passed in the url as a key value pair
# Can be used to filter data as the url provided
@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# THE URL path must be clearly defined with / on start and one before the end
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author:str,category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


#POST REQUEST METHOD 
# post have body that have additional information that get does not have

@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)


#PUT REQUEST METHOD
# used to update data
# can have  body and additional information like post 

@app.put("/booka/update_books")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book


#DELETE REQUEST METHOD
# used to delete a record 
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

