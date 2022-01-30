def login():
    usernameInput = input("username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "ascha" :
        print("login Success")
        return login()
    else :
        print("login Error, please check your username and password")
        return login()

def showMenu() :
    print("Welcome to Petch Cafe")
    print("1. Vat Calculate")
    print("2. Price Calculate")
    print("3. Exit")
    return MenuSelect()

def MenuSelect() :
    userSelect = int(input("choice :"))
    if userSelect == 1 :
        amount = int(input("please Enter ToTal Price :"))
        return vatcalculate(amount)
    elif userSelect == 2 :
        return priceCalculate()
    elif userSelect == 3 :
        return exit()
    else :
        return showMenu()

def vatcalculate(TotalPrice):
    vat = 7 / 100
    result = TotalPrice + (TotalPrice * vat)
    print("Total Price is :", result)

def priceCalculate():
    price_1 = int(input("First Product Price :"))
    price_2 = int(input("Second Product Price :"))
    return vatcalculate(price_1 + price_2)

print(login())