#Grading System
Mathematics = int(input("Enter Mathematics's marks: "))
Economics = int(input("Enter Economics's marks: "))
Chemistry = int(input("Enter Chemistry's marks: "))
Biology = int(input("Enter Biology's marks: "))
TotalMarks = Biology+Chemistry+Economics+Mathematics
OverallPercentage = (TotalMarks/400)*100

if OverallPercentage >= 90 and OverallPercentage <= 100:
    print("Grade-A,Excellent!")
elif OverallPercentage >= 80 and OverallPercentage <= 90:
    print("Grade-B,Very Good!")
elif OverallPercentage >= 70 and OverallPercentage <= 80:
    print("Grade-C,Good!")
elif OverallPercentage >= 60 and OverallPercentage <= 70:
    print("Grade-D,Need Improvement")
elif OverallPercentage >= 50 and OverallPercentage <= 60:
    print("Grade-E,Try harder next time")
else:
    print("Grade-F,Failed,Better luck next time!")

print("TotalMarks:",TotalMarks)
print("OverallPercentage:",OverallPercentage)