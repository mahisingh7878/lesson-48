#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
class computer:
    def __init__(self):
        self.___maxprice=98788


    def sell(self):
        print("cost of the computer",self.___maxprice)

    def setmaxprice(self,price):
        self.___maxprice=price

c1=computer()
c1.sell()

c1.___maxprice=9090890
c1.sell()

c1.setmaxprice(9090890)
c1.sell()