# Waiter Helper Class
# Importing the Menu class to be used in the Waiter program
from menu import Menu

class Waiter(Menu):
    def __init__(self):
        super().__init__() # Inherits the menu from the menu class
        self.order_list = []

    def order(self):

