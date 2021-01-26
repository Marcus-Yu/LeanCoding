print("Welcome to my Fibonacci Sequence!")
a = 1
b = 1
c = 0
print(a)
print(b)
while c < 60:
  c = a + b
  a = b
  b = c
  print(c)