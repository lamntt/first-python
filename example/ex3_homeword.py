# #ex1
# def vol(rad):
#   pi=3.14
#   return 4/3*pi*rad**3
# print(vol(2))

# #ex2
# def ran_check(num,low,high):
#   if low <num and high > num:
#     print(f'{num} is in the range between {low} and {high}')
#   else:
#     print('ooops')
# print(ran_check(3,1,2))


#ex3


# def up_low(s):
#   up = 0
#   low = 0
  
#   for letter in s:
#     if letter.isupper():
#       up += 1
#     elif letter.islower():
#       low += 1
    
#   print('Original String : ' + s)
#   print(f'No. of Upper case characters : {up}')
#   print('No. of Lower case Characters : ',low)

# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# print(up_low(s))

# ##ex4
# def unique_list(lst):
#   unique = []
#   for num in lst:
#     if num not in unique:
#       unique.append(num)
#   return unique
# lst = [1,2,3,4,1,2,3,8,6,10,5,6,7,8,9]
# print(unique_list(lst))
############ use set() to choose unique_list


# unique_list = (list(filter(lambda num: num not in unique,lst))
# ##5

# def multiply(numbers): 
#   mul = 1
#   for num in numbers:
#     mul = mul * num
#   return mul
# numlist= [1, 2, 3, -4]
# print(multiply(numlist))


# #ex6 

# def palindrome(s):
#   s=s.replace(' ','')
#   if s == s[::-1]:
#     return True
#   else:
#     return False
# print(palindrome('lamal'))

#ex7
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
  str2 = str1.lower()
  uniq = []
  st = str2.replace(' ','')
  
  for letter in st:
    if letter not in uniq:
      uniq.append(letter)
  
  sort_uniq = sorted(uniq)
  join_uniq = ''.join(sort_uniq)
  
  if join_uniq != alphabet:
    return False
  else: 
    return True
  
print(ispangram('quick brown fox jumps over tlazy dogg'))



# string = 'The quick brown fox jumps over the lazy dog'
# print(string.ascii_lowercase)




