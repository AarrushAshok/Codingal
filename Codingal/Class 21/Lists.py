#Lists
ages = [12,13,14,15]
print(ages)
print(ages[0])
print(ages[1])
print(ages[2])
print(ages[3])

#Adding Age
newAge = int(input("Enter new age:"))
ages.append(newAge)
print(ages)

#Deleting Age
ages.pop()
ages.pop()
print(ages)