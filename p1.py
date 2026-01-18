import math_utils as mu
try:
  num = int(input("Enter number to check:"))
  if num < 0:
    raise ValueError
  print("Is the number prime?:", mu.is_prime(num))
  print("Factorial of number is:", mu.factorial(num))
  print("Binary of number:",mu.convert_binary(num))
except ValueError:
  print("Only Positive integers can be entered")
