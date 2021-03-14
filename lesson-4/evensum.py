num = int ( input ("Pick a number."))

def addup(num):
  print(num)
  if num == 0:
    return 0
  else:
    return addup(num-2) + num



def addup1(num):
  print(num)
  if num == 0:
    return 0
  else:
    if num/2 == int(num/2):
      return addup(num-1) + num
    else:
      return addup(num-1)

print(addup1(num))

#if (num/2)==int(num/2):
  #print(addup(num))
#else:
  #(num-1)
  #print(addup(num-1))