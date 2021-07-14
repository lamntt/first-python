from random import randint
ranNum = randint(0,100)
print(f'The random number is: {ranNum}')
numCount = 0
yourNum = -1
prevNum =-1
while yourNum != ranNum:
  yourNum = int(input('Your number: '))
  # print(f'Your previous number: {prevNum}')
  if yourNum == ranNum:
    print('Correctly')
    print(f'You took {numCount} of guessing')
  elif yourNum < 0 or yourNum > 100:
    print('OUT OF BOUNDS')
  elif abs(yourNum - ranNum) < 10 and numCount == 0:
    print('WARM')
  elif abs(yourNum - ranNum) > 10 and numCount == 0:
    print('COLD')
  elif abs(yourNum - ranNum) < abs(prevNum - ranNum):
    print('WARMER')
  elif abs(yourNum - ranNum) > abs(prevNum - ranNum):
    print('COLDER')
  prevNum=yourNum
  numCount += 1

