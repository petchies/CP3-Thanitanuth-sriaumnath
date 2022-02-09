menuList = []
menuPrice = []

def showBill():
    Count = 0
    print("----- Meng Compay -----")
    for number in range(len(menuList)):
        print(menuList[number], menuPrice[number])
        Count == menuPrice[number]
    print("Totall =", Count, "Dolla")

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit" ):
        break
    else:
        menuPrice = int(input("Please Enter Menu : "))
        menuList.append(menuName)
        menuPrice.append(menuPrice)

showBill()