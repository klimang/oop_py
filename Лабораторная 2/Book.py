BOOKS_DB = [
    {"id": 1,"name": "test_1","pages": 20,},
    {"id": 2,"name": "test_2","pages": 800,}
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


if __name__ == '__main__':
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DB
    ]
    for book in list_books:
        print(book)

    print(list_books)
