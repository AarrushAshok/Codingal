#Profit and Loss
SellingPrice = int(input("Enter selling price per kilogram:"))
BuyingPrice = int(input("Enter a buying price per kilogram:"))
Kilogram = int(input("Enter the quantity in kilogram:"))
TotalSellingPrice = SellingPrice*Kilogram
TotalBuyingPrice = BuyingPrice*Kilogram

print("TotalSellingPrice:",TotalSellingPrice)
print("TotalBuyingPrice:",TotalBuyingPrice)

if TotalSellingPrice > TotalBuyingPrice:
    ProfitAmount = TotalSellingPrice - TotalBuyingPrice
    PercentageProfit = (TotalBuyingPrice/TotalSellingPrice)*100
    print("Yay!It's an Profit")
    print("ProfitAmount:",ProfitAmount)
    print("PercentageProfit:",PercentageProfit)
else:
    LossAmount = TotalBuyingPrice - TotalSellingPrice
    PercentageLoss = (TotalSellingPrice/TotalBuyingPrice)*100
    print("Oops!It's an Loss")
    print("Loss Amount:",LossAmount)
    print("PercentageLoss:",PercentageLoss)