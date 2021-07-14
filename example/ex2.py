# # ex1 of Warm up
# def lesser_of_two_evens(a,b):
#   if a % 2 == 0 and b % 2 == 0 and a > b:
#     print(a)
#   elif  a % 2 == 0 and b % 2 == 0 and a < b:
#      print(b)
#   elif a % 2 != 0 or b % 2 != 0 and a > b:
#     print(b)
#   elif a % 2 != 0 or b % 2 != 0 and a < b:
#     print(a)
# lesser_of_two_evens(2,8)


# #fix ex1
# def lesser_of_two_evens(a,b):
#   if a % 2 == 0 and b % 2 == 0:
#     return min(a,b)
#   else:
#     return max(a,b)
# print(lesser_of_two_evens(45,56))





# def lesser_of_two_evens(a,b):
#   max_num = 0
#   min_num = 1000
#   for num in lesser_of_two_evens(a,b):
#     if num > max_num:
#       max_num = num
#     elif num < min_num:
#       min_num = num
#     if a % 2 ==0 and b % 2 ==0:
#       print(max_num)
#     elif a % 2 != 0 or b % 2 != 0:
#       print(min_num)
# lesser_of_two_evens(19,50)






# ex2 of warm up and

# def animal_crackers(text):
#   text_list =text.split()
#   if text_list[0][0] == text_list[1][0]:
#     return True
#   else:
#     return False
# text = 'Jennie Lisoo'
# print(animal_crackers(text)

# # fix ex2
# def animal_crackers(text):
#   text_list =text.split()
#   return text_list[0][0] == text_list[1][0]
# print(animal_crackers('Jen Fi'))




# #ex3 of warm up 
# def makes_twenty(a,b):
#   if a + b == 20 or a == 20 or b == 20:
#     return True
#   else:
#     return False
# print(makes_twenty(15,10))


#   ex1 of level 1
# def old_macdonald(word):
#   sepr_list = list(word)
#   sepr_list[0] = sepr_list[0].upper()
#   sepr_list[3] = sepr_list[3].upper()
#   return "".join(sepr_list)
# print(old_macdonald('macdonald'))


# # fix ex1
# def old_macdonald(name):
#     if len(name) > 3:
#         return name[:3].capitalize() + name[3:].capitalize()
#     else:
#         return 'Name is too short!'
# print(old_macdonald('macdonald'))



# #ex2 of level 1
# def master_yoda(text):
#   text_list = text.split()
#   text_reverse = text_list[::-1]
#   return ' '.join(text_reverse)
# print(master_yoda('Hello world She look so beautiful'))

# ## fix ex2
# def master_yoda(text):
#   return ' '.join(text.split()[::-1])
# print(master_yoda('Hello world She look so beautiful'))




# #ex3 of level 1
# def almost_there(n):
#   return abs(100-n) <=10 or abs(200-n) <= 10
# print(almost_there(200))


# # ex1 of  level 2

# def has_33(nums):
#     for i in range(len(nums)):
      
#         # nicer looking alternative in commented code
#         if nums[i] == 3 and nums[i+1] == 3:
    
#         # if nums[i:i+2] == [3,3]:
#             return True  
    
#     return False
# print(has_33([3,8,4,5,7,3,3]))



# a = ["foo","bar","baz",'bar','any','much']

# indexes = [index for index in range(len(a)) if a[index] == 'bar']
# print(indexes)




# ex2 of level 2

# def paper_doll(text):
#   text_list = list(text)
#   letterx3 = []
#   for letter in text_list:
#     letterx3.append(letter*3)
#   return ''.join(letterx3)
  
# print(paper_doll('Missing Emma'))

# #fix ex2

# def paper_doll(text):
#   result =''
#   for letter in text:
#     result += letter*3
#   return result
# print(paper_doll('Missing Emma'))  



# ex3 of level 2

# def blackjack(a,b,c):
#   # for i in range(len(a,b,c)):
#   if a+b+c <= 21:
#     return a+b+c
#   elif (a+b+c > 21) and (a==11 or b==11 or c==11):
#     return (a+b+c) - 10
#   else:
#     return 'bust'
# print(blackjack(9,11,8))

# #fix ex3
# def blackjack(a,b,c):
    
#     if sum((a,b,c)) <= 21:
#         return sum((a,b,c))
#     elif sum((a,b,c)) <=31 and 11 in (a,b,c):
#         return sum((a,b,c)) - 10
#     else:
#         return 'BUST'
# print(blackjack(10,10,11))

# #ex4 of level 2:

# def summer_69(arr):
#   temp=[]
#   flag=False
#   if 6 in arr :
#     for nums in arr:
#       if nums!=6 and flag==False:
#         temp.append(nums)
#         print(temp)
#       elif nums==6 or nums !=9:
#         flag=True
#       elif nums ==9:
#         flag=False
#   else:
#     temp=arr
#   return sum(temp)
# print(summer_69([6,2,3,1,2,9,2,6,1,9,3]))

# # num_list = [1,2,4,0,0,7,5]
# def spy_game(num_list):
#   temp =[]
#   flag = False
#   for nums in num_list:
#     if nums ==0 and flag ==False:
#       temp.append(nums)
#     elif nums != 0 and nums !=7:
#       flag = True
      
#     elif nums == 0 and flag ==True:
#       temp.append(nums)
#     elif nums != 0 and nums !=7:
#       flag = False
#     elif nums == 7 :
#       temp.append(nums)
#   # return temp
  
#   if temp == [0,0,7]:
#     return True
#   else:
#     return False
# # num_list = [1,2,4,0,0,7,5]
# print(spy_game([1,0,2,4,5,7,0,0,2,7]))








# def spy_game(num_list):
#   temp = []
#   for nums in num_list:
#     if nums == 0 or nums == 7:
#       temp.append(f'{nums}')
#   str="".join(temp)
#   if str.__contains__('007'):
#     return True
#   else:
#     return False
# print(spy_game([1,7,2,0,4,5,0,2]))




# def spy_game(nums):

#     code = [0,0,7,'x']
    
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)   # code.remove(num) also works
       
#     return len(code) == 1
# print(spy_game([1,2,0,4,5,7,0,1,7,0,0]))


# def count_primes(num):
  
#   arr = []
#   for nums in range(2,num):
#     flag=True
#     for i in range(2,nums):
#         if nums % i == 0:
#           flag=False
#           break
#     if flag == True:
#       arr.append(nums)
#   return len(arr)
# print(count_primes(100))

    


# def print_big(letter):
#     patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
#     alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
#     for pattern in alphabet[letter.upper()]:
#         print(patterns[pattern])
# print(print_big('d'))
