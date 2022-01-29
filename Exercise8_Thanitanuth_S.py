userID = input("Please enter your ID : ")
userPassword = input("Please enter your Password : ")
if userID == "admin" and userPassword == "1234":
    print("-----Welcome to YottaPetch Company-----")
    print("=======================================")
    print("Issue1 << Azure Lagacy Chapter 1 Price 5 Dolla")
    print("Issue2 << Hanli Chapter 2 Price 6 Dolla")
    addToCart = input("Please enter Login ID that you want to purchase : ")
    if addToCart == "Issue1" :
        quantity = int(input("How many pieces do you want ? : "))
        totaltransaction = 5*quanlity
        acceptissue1 = input ("No exchange or refund Confirm Yes or No ? : ")
        if acceptissue1 == "Yes" :
            print("Total :", totaltransaction, "Dolla")
        if acceptissue1 == "No" :
            print("order canceled, please try again")
    elif addToCart == "Issue2" :
        quantity = int(input("How many pieces do you want ? : "))
        totaltransaction = 6*quanlity
        acceptissue1 = input ("No exchange or refund Confirm Yes or No ? : ")
        if acceptissue1 == "Yes" :
            print("Total :", totaltransaction, "Dolla")
        if acceptissue1 == "No" :
            print("order canceled, please try again")
