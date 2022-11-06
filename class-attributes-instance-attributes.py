# -*- coding: utf-8 -*-
"""Python-OOP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11ick8Wl-hJt32Fumxy7tg3Jzjkdh2o8-
"""


class Item:
    # Class Attribute
    rate = 0.3

    def __init__(self, name: str, price: float, qty=0):
        # Run Validation to receive argument
        assert price >= 0, f"Price {price} is less than zero"
        assert qty >= 0, f"Quantity: {qty} is less than zero"

        # instance Attributes - self object
        self.name = name
        self.price = price
        self.qty = qty

    def total_price(self):
        return self.price * self.qty

    # accessing class attributes in a method at class level: Item.rate;
    # but if we access class attribute at instance level: self.rate; then -
    # we can easily change the value of the rate at instance level
    # therefore it is good practice to access class attribute at instance level if-
    # we have plan to change the value of the attribute.
    def apply_discount(self):
        self.price = self.price * self.rate
        return self.price


pc = Item('Laptop', 45000, 5)
print(f'{pc.qty} pc Total Price {pc.total_price()}')
pc.rate = .45
print(f'Discount: {pc.apply_discount()}')
'''
pc.__dict__ # Return attribute at the instance level
Item.__dict__ # return attributes of the Item class
pc.price
'''

print(pc.rate)  # Accessing class attribute from instance level
print(Item.rate)  # class attribute from class level