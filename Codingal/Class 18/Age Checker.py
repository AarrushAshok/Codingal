#Age Checker
try:
    age = int(input("Enter you age:"))
    if age < 0 :
        raise ValueError("Age Cannot be Negative")
    print(f"Age is:{age}")
except ValueError as ve:
    print(ve)