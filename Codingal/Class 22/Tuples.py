#List can be changed later(mutability - can be modified)
#Tuples cannot be changed later(immutability - cannot be modified)
#Index Value startes from 0,1,2,3,4,5
#

#Tuples
t = (1,2,3,4,5,6)
print(t)
l =[2]
t =(1,)
print(type(l))
print(type(t))
list1 = [12,45,21,67,89,34,56,78,90,100,11,123,134,145,156,167,178]
for i in list1:
    print(i)
t = ("aarush",2,3,8,True,5,False,7,8,9,10)
for i in t:
    print(t)

t = (1,2,3)
x,y,z = t
print(x)
print(y)
print(z)

#Tuple Unpacking
t = ("My name is Aarush,","I am 14 years old,","I live in Coimbatore.")
name,age,city = t
print
#Index - Starts from 0,1,2,3,4. Eg:10,20,30 = 0,1,2
numbers = (10,20,30,40,50)
print("index of 30:",numbers.index(30))
print("index of 50:",numbers.index(50))

#Finding Repetition
colors=("red","blue","red","green","red","blue")
print("red has ocuured:",colors.count("red"))
print("blue has occured",colors.count("blue"))