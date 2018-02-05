#!/usr/bin/python
# -*- coding: utf-8 -*-
"""A simple class"""

class Book(object):
    """creating the book class"""

    author = ''
    title = ''

    def __init__(self, author, title):
        """defining the init function"""

        self.author = author
        self.title = title

    def show(self):
        """creates the print statement"""

        print "{}, written by {}".format(self.title, self.author)

book1 = Book('John Steinbeck', 'Of Mice and Men')
book2 = Book('Harper Lee', 'To Kill a Mockingbird')

book1.show()
book2.show()
