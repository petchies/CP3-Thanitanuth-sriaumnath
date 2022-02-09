systemMenu = {"ข้าวเหนียวทุเรียน":70, "ข้าวคลุกกะปิ":50, "ข้าวกิมจิ":79, "พิซซ่า":199}
menuList = []

def showBill():
    Total = 0
    print("----- Meng Company -----")
    for i in range(len(menuList)) :
        print(menuList[i][0], menuList[i][1])
        Total += input(menuList[i][1])
    print("Total :", Total)
while True:
    menuName = input("Please Enter Menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()