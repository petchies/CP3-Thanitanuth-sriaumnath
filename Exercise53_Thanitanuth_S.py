TotalPrice = int(input("TotalPrice : "))
Vat = int(input("TaxRate : "))
def Vatcalculate(TotalPrice):
    result = TotalPrince*(100+Vat)/100
    return result
print(Vatcalculate(TotalPrice))