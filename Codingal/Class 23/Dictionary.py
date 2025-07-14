#Dictionary
Dictionary ={
"Sky": "Akash",
"Aarush": "First ray of the sun",
"Aman": "Peace",
"Konnichiwa": "Hello",
}

print(Dictionary)
word = input("Enter a word:")
print(f"Meaning of {word} is",Dictionary[word])


studentDetail = {
    1:"akash",
    2:"aarush",
    3:"aman",
    4:"annika",
    5:"david"
}

print(studentDetail)
studentDetail[4] = "syda"
print(studentDetail[4])
studentDetail[6] = "rai"
print(studentDetail[6])
studentDetail["fullName"] = "kumar"
print(studentDetail["fullName"])

Detail = {
    1:"akash",
    2:"aarush",
    3:"aman",
    4:"annika",
    5:"david"
}
print(Detail.keys())
print(Detail.values())
print(Detail.items())
count = 1
for key in Detail.keys():
    print(f"on {count} place key is {key}")
    count = count +1
count = 1
for value in Detail.values():
    print(f"on {count} place value is {value}")
    count = count +1
for key,value in Detail.items():
    print(f"for key {key} value is {value}")