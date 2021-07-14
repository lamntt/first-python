from random import randint 
ranNum = randint(0,101)
print(f'The random number is: {ranNum}')
yourNum =0
numCount = 0
while  int(yourNum) != ranNum:
  yourNum = int(input('Your number: '))
  if yourNum == ranNum:
    print('correctly')
  elif numCount==0:
    if abs(yourNum -ranNum)<=10:
      print('WARM') 
    else:
      print('COLD')
  else:
    if abs(yourNum -ranNum)<=10:
      print('WARMER') 
    else:
      print('COLDER')
  numCount += 1
print(f'You took {numCount} of guessing')
# while int(yourNum) < 0 or int(yourNum) > 100:
#   print('OUT OF BOUNDS')
#   numCount += 1
#   yourNum = input('Your number: ')

    








