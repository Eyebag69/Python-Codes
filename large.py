def largest(a,b,c):
  if a>= b and a >= c:
    return a 
  elif b >=a and b >=c:
    return b
  else:
    return c
def sum_of_digits(num):
  t = 0
  while num >0:
    last = num % 10
    total += last 
    num = num//10
  return t 
def num_rev(num):
  rev = 0
  while num > 0:
     last = num % 10
     rev = rev * 10 + last
     num = num//10
  return rev 

print("Menu")
print("1.For largest of Digits")
print("2.for sum of digits")
print("3.for reverse of digits")
print("4. exit") 
while True:
  choice = int(input("Enter choice:"))
  match choice:
    case 1:
      a = int(input("Enter first number:"))
      b = int(input("Enter second number:"))
      c = int(input("Enter third number:")) 
      print("Largest:",largest(a,b,c))  
    case 2:
      num = int(input("Enter number for sum:"))
      print("sum of digits:",sum_of_digits(num))
    case 3:
      num = int(input("Enter number for reverse:"))
      print("reverse of number is:", num_rev(num))

    case 4:
      print("Exiting")
      break
    case _:
      print("Invalid input") 