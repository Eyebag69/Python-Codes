#temperature coversion

temp = float(input("Enter Temperature:"))
unit = input("Is this Temperature In Celsius or Fahrenheit (C or F):").upper()

if unit == "C":
    temp = round((temp * 9/5) + 32 , 1)
    unit = "Fahrenheit"
    print(f"Converted Temperature is: (temp,2) {unit}")
elif unit == "F":
    temp = round((temp - 32) * 5/9 , 1)
    unit = "Celsius"
    print(f"Converted Temperature is: (temp,2) {unit}")
else:
    print(f"{unit} is an invalid unit")
