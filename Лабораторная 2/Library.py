import typing

BOOKS_DB = [
    {"id": 1,"name": "test_1","pages": 20,},
    { "id": 2,"name": "test_2","pages": 800,}
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга \"{self.name}\""

    def __repr__(self):
        return f"Book(id_={self.id_}, name=\'{self.name}\', pages={self.pages})"

class Library:
    def __init__(self, books: list[Book] = None):
        self.books: list[Book] = books if books else []

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id: int):
        for i, book in enumerate(self.books):
            if book.id_ == book_id:
                return i
        else:
            raise ValueError("Книги не существует")

if __name__ == '__main__':
    empty_library = Library() 
    print(empty_library.get_next_book_id())  

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DB
    ]
    library_with_books = Library(books=list_books)  
    print(library_with_books.get_next_book_id())  

    print(library_with_books.get_index_by_book_id(1)) 
