'''
#Siddhi
class Fooditem:

    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        print(self.name)
        print(self.price)
        print(self.category)


class Customer:

    ord_details = ""

    def __init__(self,name,id,hist):
        self.name = name
        self.id = id
        self.hist = hist

    def place_order(self,item,quantity):
        self.item = item
        self.quantity = quantity




class Rcustomer(Customer):
    def __init__(self,discount):
        super.__init__()
        self.discount = 5/100

    def place_order(self,item,quantity):
        total =



class Restaurant:
    '''


class FoodItem:
    def __init__(self,name,price,category):
        self.name= name
        self.price = price
        self.category = category

    def display_info(self):
        print(self.name)
        print(self.price)
        print(self.category)

class Customer:
    order_history = []
    def __init__(self, name, customer_id ):
        self.name= name
        self.customer_id = customer_id
        self.order_history = []

    def place_order(self,food_item,quantity):
        order_details  = {'food_item': food_item.name,
                          'quantity': quantity,
                          'total_price':food_item.price * quantity
                          }
        Customer.order_history.append(order_details)
        print(f"Order Placed for {quantity} x {food_item.name}")

    def view_order_history(self):
       if not self.order_history:
           print("No order placed yet")
       else:
           print(f"Order history for {self.name}:")
           for index, order in enumerate(self.order_history,1):
             print(f"{index}.{order['quantity']} x{order['food-item']} - Total:  ${order['total_price']}")



pizza = FoodItem("Pizza", 10.99, "Main Course")
ice_cream = FoodItem("Ice Cream", 4.99, "Dessert")

pizza.display_info()
ice_cream. display_info()
customer1 = Customer("John", "A001")
customer1.place_order(pizza, 2)
customer1.place_order(ice_cream, 3)

customer1.view_order_history()

class Restaurant:
    def __init__(self, menu, customer):
        self.menu= menu
        self.customer = customer

    def add_food_item (self,food_item):
        self.menu.append(food_item)

    def add_customer(self,customer):
        self.customer.append(customer)

    def display_menu(self):
        print(self.menu)

    def display_customer(self):
        print(self.customer)










