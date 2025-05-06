# To convert temperature measures between celcius and fahrenheit scale

# Function to convert celcius to fahrenheit
def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

# Function to convert fahrenheit to celcius
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

# Take input from user
def temperature_converter():
    print("Welcome to the Temperature Converter!")
    choice = input("Convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F): ").strip().upper()

    if choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F")
    elif choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit)}°C")
    else:
        print("Invalid choice! Please choose either 'C' or 'F'.")

# Test
if __name__ == "__main__":
    temperature_converter()
