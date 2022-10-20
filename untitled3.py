# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:19:50 2022

@author: pulle
"""

from tkinter import*

root= Tk()
root.title("Class")
root.geometry("600x600")

class Bookshelf:
    def __init__(self, name, age, dob, id_number):
        self.bookshelf_name = name
        self.bookshelf_age = age
        self.bookshelf_dob = dob
        self.bookshelf_id = id_number
        
    def add_bookshelf(self):
        print("Book Name: "+self.bookshelf_name)
        print("Book Author: "+self.bookshelf_age)
        print("Book Price: "+str(self.bookshelf_dob))
        print("Book was Published in: "+str(self.bookshelf_id))
        print("Book Added")
        
        
        
bookshelf1 = Bookshelf("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 13.49, 1997)
bookshelf1.add_bookshelf()

bookshelf2 = Bookshelf("Diary of a Wimpy Kid", "Jeff Kinney", 6.70, 2017)                                                                                                                     )
bookshelf2.add_bookshelf()