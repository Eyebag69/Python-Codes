def is_prime(n):
  for i in range(2,n):
    if n %i == 0:
      return False
  else:
    return True
def factorial(n):
  if n <= 1:  
    return 1
  else:
    return n*factorial(n-1)
def convert_binary(n):
  binary =" "
  while n > 0:
    binary = binary + str (n % 2)
    n= n//2
  return binary[::-1] or "0"

