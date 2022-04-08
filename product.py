# Create a Product class with 3 attributes
import random
from math import ceil


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = ceil(10000000 * random.uniform(0, 1))

    # Add the update_price method to the Product class
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price + ((percent_change / 100) * self.price)
        elif is_increased == False:
            self.price = self.price - ((percent_change / 100) * self.price)
        return self

    def print_info(self):  # Add the print_info method to the Product class
        print(
            f"Name of product is: {self.name}, Category is: {self.category}, Price is: {self.price}")
        return self
