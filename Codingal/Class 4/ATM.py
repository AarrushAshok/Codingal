#ATM = Automatic Teller Machine
print("Welcome to the ATM")
Amount = int(input("Enter Amount:"))

#Notes available are 1000,500,100

#1000 Notes
NumberOf1000Notes = Amount//1000
#Remaining after 1000 Notes
RemainingAmount = Amount - (NumberOf1000Notes*1000)

#500 Notes
NumberOf500Notes = RemainingAmount//500
#Remaining after 500 Notes
RemainingAmount = RemainingAmount  - (NumberOf500Notes*500)

#100 Notes
NumberOf100Notes = RemainingAmount//100

print("Number of 1000 notes:",NumberOf1000Notes)
print("Number of 500 notes:",NumberOf500Notes)
print("Number of 100 notes:",NumberOf100Notes) 