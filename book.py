
class Book:

    def __init__(self, book_title, author_name, maker):
        self.book_title = book_title
        self.author_name = author_name
        self.maker = maker

    def get_book_title(self):
        print(self.book_title)

    def set_book_title(self, title):
        self.book_title = title

    def get_author_name(self):
        print(self.author_name)

    def set_author_name(self, string):
        self.author_name = string

    def get_maker(self):
        print(self.maker)

    def set_maker(self, string):
        self.maker = string

    def __str__(self):
        return f'Title: {self.book_title}, Author: {self.author_name}, Publisher: {self.maker}'
    



def __str__(self):
    return f"Title: {self._title}, Author: {self._author}, Publisher: {self._publisher}"