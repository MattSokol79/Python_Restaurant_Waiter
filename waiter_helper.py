# Waiter Helper Class
# Importing the Menu class to be used in the Waiter program
from menu import Menu

class Waiter(Menu):
    def __init__(self):
        super().__init__() # Inherits the menu from the menu class
        self.order_list = []

    def order(self):
        ordering = True

        while ordering:
            choice = input("What would you like to order? ")

            if choice in self.menu:
                self.order_list.append(choice)
            else:
                print("I'm sorry, we do not serve that here")

            if choice.lower() == "no":
                ordering = False

        return self.order_list

    def __str__(self):
        return "You ordered {}".format(self.order_list)

