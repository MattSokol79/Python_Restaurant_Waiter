# Waiter Helper Class
# Importing the Menu class to be used in the Waiter program
from menu import Menu

class Waiter(Menu):
    def __init__(self):
        super().__init__() # Inherits the menu from the menu class
        self.order_list = [] # Creates an empty order list

    # This is the ordering method, order number starts at 0, and increments up to 3
    def order(self):
        order_number = 0
        # A diner is greeted with the menu
        print("This is the current menu, due to company policy, "
              "diners may only order maximum 3 items", self.menu)
        print("What would you like to order?")
        while order_number < 3: # We only want the diner to order 3 items
            diner_order = input("--> ").title()
            # If the specified item is present in the menu, we can add it to the order_list
            if diner_order in self.menu:
                self.order_list.append(diner_order)
                order_number += 1
            else:
                print("Sorry, we are currently not serving this item")
        # If we have reached more than 3 items, we return the order to the diner
        else:
            return self.order_list

    # This __str__ allows us to display what was ordered once the program
    # Has run its course
    def __str__(self):
        return "{}".format(self.order_list)

# Main allows us to run the code from this file, so no need to import
# the classes into another .py file
def main():
    customer = Waiter()

    print("Welcome to the restaurant.")
    customer.order()
    print(f"You have ordered:\n {customer}")

# Checks if the code is running from the current file
if __name__ == "__main__":
    main()