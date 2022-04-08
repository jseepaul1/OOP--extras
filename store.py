import re
from product import Product

# Create a Store class with 2 attributes


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):  # Add the add_product method to the Store class
        self.products.append(new_product)
        return self

    def sell_product(self, id):  # Add the sell_product method to the Store class
        for index, product in enumerate(self.products):
            if product.id == id:
                del self.products[index]
        return self

    # NINJA BONUS: Add the inflation method to the Store class
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    # NINJA BONUS: Add the set_clearance method to the Store class
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self

    def print_all_products(self):
        for product in self.products:
            product.print_info()
        return self


deli = Store("Argo's Deli")

product_1 = Product('peanuts', 5, 'legumes')
product_2 = Product('milk', 10, 'dairy')
product_3 = Product('chicken', 15, 'protein')
product_4 = Product('beef', 20, 'protein')

deli.add_product(product_1).add_product(product_2).add_product(product_3).add_product(product_4).set_clearance(
    "protein", 5).print_all_products().sell_product(product_4.id).inflation(10).print_all_products()
