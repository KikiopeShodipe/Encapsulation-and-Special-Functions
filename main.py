class MyClass:
    def __init__(self, value):
        self.__privateVar = value

    def __privMeth(self):
        print("This is a private method.")

    def hello(self):
        print(f"The value of privateVar is: {self.__privateVar}")

    def callPrivateMethod(self):
        self.__privMeth()

value = int(input("Enter an integer value: "))
obj = MyClass(value)
obj.hello()
obj.callPrivateMethod()
