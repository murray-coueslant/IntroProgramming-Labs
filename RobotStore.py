class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def getStock(self, count):
        if count > self.quantity:
            print('We do not have that many in stock.')
            print('Right now we have', self.quantity, 'in stock.')
        else:
            print('Right now we have', self.quantity, 'in stock.')
    
    def getCost(self, count):
        cost = count * self.price
        print(count, self.name + '\'s', 'would cost', '$' + str(cost))
    
    def modifyStock(self, count):
        self.quantity -= count
        print('You have removed', count, self.name + 's')

products = [Product("Ultrasonic range finder", 2.50, 4), Product("Servo motor", 14.99, 10),
            Product("Servo controller", 44.95, 5), Product("Microcontroller Board", 34.95, 7),
            Product("Laser range finder", 149.99, 2), Product("Lithium polymer battery", 8.99, 8)]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i].quantity > 0:
            print(str(i)+")", products[i].name , "$", products[i].price)
            print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": 
            break
        prodId = int(vals[0])
        count = int(vals[1])
        if products[prodId].quantity >= count:
            if cash >= products[prodId].price:
                products[prodId].modifyStock(count)
                cash -= products[prodId].price * count
                print("You purchased", count, products[prodId].name+"s.")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", products[prodId].name)
main()