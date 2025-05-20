class Computer:
    def __init__(self):
        self.__max_price = 50000
    def sell(self):
        print(f"\nCurrent Selling Price: {self.__max_price}")
    def setMaxPrice(self, price):
        self.__max_price = price
print("Welcome to the Computer Shop!")
comp = Computer()
print("\nInitial price of the computer:")
comp.sell()
direct_price = int(input("\nTry setting a new price directly (this won't work as expected): "))
comp.__max_price = direct_price
print("After attempting to change the price directly:")
comp.sell()
setter_price = int(input("\nNow enter a new price using the proper setter method: "))
comp.setMaxPrice(setter_price)
print("After changing the price using setter:")
comp.sell()