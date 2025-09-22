#Frequency Checking in a Dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test Dictionary:", test_dict)

user_input = int(input("Enter a number to check its frequency in the dictionary: "))

if user_input in test_dict.values():
    frequency = list(test_dict.values()).count(user_input)
    print(f"The frequency of {user_input} in the dictionary is: {frequency}")
else:
    print(f"The value {user_input} is not present in the dictionary.")