#Class
#A class is like a blueprint or map. Just like a blueprint of a building.
#An object is a real thing created from a class. 
# #From one blueprint, you can create many buildings
class human:
    def __init__(self,a,b,c,d,e):
        self.name = a
        self.age = b
        self.gender = c
        self.height = d
        self.weight = e
        print("Constructor Called")

aarush = human("aarush",23,"male",5.6,60)
john = human("john",33,"male",5.9,65)
sam = human("sam",31,"male",5.8,63)
rena = human("rena",26,"female",5.0,70)