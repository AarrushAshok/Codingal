#List Comprehension
list1 = [13,45,21,78,87,35,65,78,98,23,45,67,89]
print("Original list:",list1)

listOfSquare = [x**2 for x in list1]
evenNumber = list=({x for x in list1 if x%2 == 0})

print("List of squares:",listOfSquare)
print("Even Numbers:",list(evenNumber))