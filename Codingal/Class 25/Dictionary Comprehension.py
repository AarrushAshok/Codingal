#Dictionary Comprehension
list1 = [13,45,21,78,87,35,65,78,98,23,45,67,89]

dictionaryOfSquare = {str(x):x**2 for x in list1}

for key,value in dictionaryOfSquare.items():
    print("square of",key,":",value)
