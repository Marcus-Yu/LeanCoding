num = int(input("Pick A Number."))

def factorial(num):
  print(num)
  if num == 1:
    return 1
  else:
    return factorial(num-1) * num

print(factorial(num))