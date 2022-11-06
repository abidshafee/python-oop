import csv

class myItem:
    # Class Attribute
    discount_rate = 0.3
    all_items = [] # Adding all items (instances) to this list
    def __init__(self, item: str, price: int, qty = 0):
        self.item = item
        self.price = price
        self.qty = qty

        # Method that autometically populate All_list -
        # the instances of myItem type is created
        myItem.all_items.append(self) # self is the object itself
        # Now if any object of myItem type is created that object -
        # will be autometically added to all_items lit

    def total_price(self):
        return self.price * self.qty

    def discount(self):
        self.price = self.price * self.discount_rate
        return self.price

    # Object Representation - Magic Method -> Representing class objects
    # Using this __repr__ method we've control to represent our object as we want
    def __repr__(self):
        return f"Item('{self.item}', {self.price}, {self.qty})"

    # Now we need to create a method that doesn't need instanciation
    # so we'll create a classmethod that doesn't get instanciated -
    # as the objet ob the class is created
    # Here what cls indicates is when we call the class method -
    # the class itself is passed as the firt argument in the background
    @classmethod
    def read_from_csv(cls):
        with open('data.csv', 'r') as f:
            record = csv.reader(f)
            pass


phone = myItem("Phone", 35000, 10)
laptop = myItem("Laptop", 65000, 5)
cable = myItem("Cable", 1300, 5)
mouse = myItem("Mouse", 450, 18)
keyword = myItem("Keyboard", 800, 30)

# In "all_items" list our object is appended as they created
print(myItem.all_items)

# Accessing and representing objects without __repr__ method
# for object in myItem.all_items:
#     print(object.item)

# Instantiating Class Method
myItem.read_from_csv()
