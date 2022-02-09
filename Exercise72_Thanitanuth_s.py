menuList = []

def showBill():
    TotalPrice = 0
    print("----- Meng Food -----")
    for number in range(len(menuList)) :
        print(menuList[number])
        TotalPrice += int(menuList[number][2])
    print("Total :" , TotalPrice)

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == 'exit'):
        break
    else:
        menuPrice = input("Please Enter Price :")
        menuList.append([menuName, menuPrice])

showBill()
