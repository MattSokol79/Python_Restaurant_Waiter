# Waiter Helper Class
# Importing the Menu class to be used in the Waiter program
from menu import Menu

class Waiter(Menu):
    def __init__(self):
        super().__init__() # Inherits the menu from the menu class
        self.order_list = []

    # This is the ordering method, every time a person is asked
    # what they want ordered, they can input an item on the meny
    # if the item does not exist on the menu, they will be told thats the case

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

    # This __str__ allows us to display what was ordered once the program
    # Has run its course
    def __str__(self):
        return "You ordered {}".format(self.order_list)

def main():
    customer = Waiter()

    print("Welcome to the restaurant.")
    customer.order()
    print(f"You have ordered: {customer}")

# Checks if the code is running from the current file
if __name__ == "__main__":
    main()