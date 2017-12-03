from graphics import *

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

def printStock(output):
    textOut = ""
    textOut += "\n"
    textOut += "Available Products\n"
    textOut += "------------------\n"
    for i in range(0,len(products)):
        if products[i].quantity > 0:
            textOut += str(i)+")" + " " + str(products[i].name) + " " + "$" + str(products[i].price) + " " + str(products[i].quantity)
            textOut += "\n"
    output.setText(textOut)

def showIntro(app):
    global entry, prompt, output
    # simple greeting
    output = Text(Point(2.5, 7), "Welcome to the Robot Shop!")
    output.draw(app)
    # instructions
    prompt = Text(Point(2, 3), "How much money do you have? $")
    prompt.draw(app)
    # text entry box
    entry = Entry(Point(4, 3), 6) # box holds six characters
    entry.setText("0.00")
    entry.draw(app)
    # wait for user to input something... how do I know when to stop waiting?
    while(app.getKey() != 'Return'): pass # so long as the user has not typed return, do nothing
    return float(entry.getText())

def main():
    app = GraphWin("Robot Shop", 400, 100)
    app.setCoords(0, 0, 5, 10)

    cash = showIntro(app)
    
    app.close()

    # create a new graphical window
    app = GraphWin("Robot Shop", 480, 400)
    app.setCoords(0, 0, 10, 10)

    # remove old prompt and draw a new one
    prompt.undraw()
    prompt.setText("Enter the product ID and Quantity you wish to purchase: ")
    prompt.draw(app)
    prompt.move(2.25, -1)
    # remove old entry box and draw a new one
    entry.undraw()
    entry.setText("ID QTY")
    entry.draw(app)
    entry.move(4.5, -1)

    Rectangle(Point(4, 0.5), Point(6, 1.5)).draw(app)
    button = Text(Point(5, 1), "Purchase")
    button.draw(app)

    output.undraw()
    output.draw(app)
    output.move(2.5, 0)

    message = Text(Point(5, 4), "")
    message.draw(app)
    message1 = Text(Point(5, 5), "")
    message1.draw(app)
    while cash > 0:
        printStock(output)
        # save click coords in a variable for later
        clickPoint = app.getMouse()

        vals = entry.getText().split(" ")
        entry.setText("")
        if vals[0] == "quit": 
            break
        prodId = int(vals[0])
        count = int(vals[1])
        if products[prodId].quantity >= count:
            if cash >= products[prodId].price:
                # products[prodId].modifyStock(count)
                cash -= products[prodId].price * count
                message.setText("You purchased " + str(count) + " " +  products[prodId].name+"s." + "\n")
                message1.setText("You have $" + "{0:.2f}".format(cash) + " remaining.")
                message.setTextColor('blue')
                message1.setTextColor('blue')
            else:
                message.setText("Sorry, you cannot afford that product.")
                message.setTextColor('red')
        else:
            message.setText("Sorry, we are sold out of " + products[prodId].name)
main()