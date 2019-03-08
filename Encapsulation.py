#Encapsulation in Python.
class Laptop:

    def __init__(self):
    # __maxprice is a private variable
        self.__maxprice = 10000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

obj = Laptop()
obj.sell()

# change the price
obj.__maxprice = 12000
obj.sell()

# using setter function
obj.setMaxPrice(12000)
obj.sell()
