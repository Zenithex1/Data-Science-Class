"""
Practice Question: Online Food Delivery Order System (Level 2.5/5)

Create a class named Pathao.

Attributes

Each order should store:

customerName (string)
restaurantName (string)
totalAmount (float)
status (string) — "Preparing", "Out for Delivery", "Delivered"
deliveryFee (float)
Constructor

Create a constructor that initializes all attributes when a FoodOrder object is created.

Methods
updateStatus(newStatus)
Update the order status.
Only allow valid statuses.
addItem(price)
Increase totalAmount by the item's price.
applyDiscount(percent)
Reduce the total amount by the given percentage.
calculateFinalBill()
Return the total amount including the delivery fee.
displayOrderInfo()
Display all order details in a readable format.
Testing Requirements

In the main program:

Create at least two FoodOrder objects.
Add items to both orders.
Apply a discount to one order.
Update order statuses multiple times.
Calculate and display the final bill for each order.
Display all order information.
"""

class Pathao():
    def __init__(self,customerName,restaurantName,totalAmount,status,deliveryFee):
        self.customerName = customerName
        self.restaurantName = restaurantName
        self.totalAmount = totalAmount
        self.status = status
        self.deliveryFee = deliveryFee
    
    def updateStatus(self,newStatus):
        valid_status = ["Preparing", "Out for Delivery", "Delivered"]
        if  newStatus in valid_status:
            self.status = newStatus
            print("Status updated to:", self.status)
        else:
            print("Invalid status!")


    def addItem(self,price):
        self.totalAmount = self.totalAmount +price 
        print(self.displayOrderInfo())

        return f"The total amount after adding item is  {self.totalAmount}"

    def applyDiscount(self,percent):
        self.totalAmount = self.totalAmount - (percent/100)* self.totalAmount
        print(self.displayOrderInfo())
        return f"The total amount after discount is {self.totalAmount}"

    def calculateFinalBill(self):
        print(self.displayOrderInfo())
        return f"The toal Amount after delivery is {self.totalAmount+self.deliveryFee}"
        

    def displayOrderInfo(self):
        return(
            f"customerName:{self.customerName}",
            f"restaurantName:{self.restaurantName}",
            f"totalAmount:{self.totalAmount}",
            f"status:{self.status}",
            f"delivery_fee :{self.deliveryFee}"
        )

    def isFree(self):
        if self.totalAmount > 50:
            return True
        else:
            return False
obj = Pathao("Jenish","Zoom",1000.0,"Out for Delivery",50.0)

print(obj.updateStatus("Preparing"))
print(obj.addItem(200))
print(obj.applyDiscount(20))
print(obj.calculateFinalBill())
print(obj.addItem(200))
print(obj.isFree())