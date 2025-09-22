#Odd Numbers
num = int(input("Enter a number: "))
odd = [i for i in range(num) if i % 2 != 0]
even = [i for i in range(num) if i % 2 == 0]
print("Odd numbers:",odd)
print("Even numbers:",even)

#Capitalize first letter of each fruit
fruits = ['apple', 'banana', 'cherry', 'date', 'blueberry']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized Fruits:", capitalized_fruits)