#Temperature
def get_temperature():
    try:
        temp = float(input("Enter temperature in Celsius: "))
        if temp < -273.15:
            raise ValueError("Temperature cannot be below -273.15°C")
        print(f"Temperature entered: {temp}°C")
    except ValueError as ve:
        print("Error:", ve)

def check_string_length(s):
    if len(s) < 3:
        raise ValueError("String length must be at least 3 characters.")
    return "String length is acceptable."

# Using the functions
get_temperature()

try:
    user_input = input("Enter a string: ")
    result = check_string_length(user_input)
    print(result)
except ValueError as e:
    print("Error:", e)