class MyClass:
    def getString(self):
        self.name = input()
    def printString(self):
        print(self.name.upper())
m = MyClass()
m.getString()
m.printString()

