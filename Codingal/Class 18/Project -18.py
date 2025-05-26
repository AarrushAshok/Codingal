#Temperature
def get_temperature():
    try:
        temp = float(input("Enter temperature in Celsius: "))
        if temp < -273.15:
            raise ValueError("Temperature cannot be below -273.15°C")
        print(f"Temperature entered: {temp}°C")
    except ValueError as ve:
        print("Error:", ve)