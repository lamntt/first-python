jn_list = [' ','O',' ']
from random import shuffle

def shuffle_list(jn_listAgr):
  shuffle(jn_listAgr)
  return jn_listAgr

def  your_guess():
  guess = ' '
  while guess not in ['0','1','2'] :
    guess = input('Please choose one of 0 or 1 or 2: ')
  return int(guess)

def check_guess(jn_listAgrLam,guessing):
  if jn_listAgrLam[guessing] == 'O':
    print('correctly')
    print(jn_listAgrLam)
  else:
    print('wrong')
    print(jn_listAgrLam)
 
mix_list = shuffle_list(jn_list)
# shuffle(jn_list)
print(mix_list)

guess = your_guess()
check_guess(jn_list,guess)