#Sets
#Sets does not allow duplicate value
set1 = {1,2,3,4,4,5,6,7,9,9,9}
set2 = {3,5,9,10,11,12,34,56,67,23}
print(f"set1:{set1}")
print(f"set2:{set2}")

#Union
print(f"union of set1 and set2:{set1.union(set2)}")
print(f"union of set1 and set2:{set1 | set2}")

#Intersection
print(f"intersection of set1 and set2:{set1 & set2}")
print(f"intersection of set1 and set2:{set1.intersection(set2)}")

#Difference
print(f"difference of set1 and set2:{set1.difference(set2)}")
print(f"difference of set1 and set2:{set1 - set2}")
print(f"difference of set2 and set1:{set2.difference(set1)}")
print(f"difference of set2 and set1:{set2 - set1}")

#Symmetric Difference
print(f"symmetric difference of set1 and set2: {set1.symmetric_difference(set2)}")
print(f"symmetric difference of set1 and set2: {set1^set2}")