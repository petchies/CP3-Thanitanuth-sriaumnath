class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ", self.name, self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Por"
customer1.lastName = "Mei"
customer1.addCart()

customer2 = Customer()
customer2.name = "Petch"
customer2.lastName = "Chin"
customer2.addCart()

customer3 = Customer()
customer3.name = "Wee"
customer3.lastName = "Feng"
customer3.addCart()

customer4 = Customer()
customer4.name = "Kong"
customer4.lastName = "Ruk"
customer4.addCart()