# jndict = {'thuyen':65,'khanh':72,'an':92,'giang':99}
# print(jndict['khanh'])
# jndict['lam'] = ['2k2','uel','hard work']
# jndict['an'] = 93
# jndict[2]='loc'
# print(jndict.keys())
# print(jndict.values())
# print(jndict['lam'][1])
# jnset = set()
# jnset.add(4)
# jnlist = [2,2,4,4,1,1,5,5]
# print(set(jnlist))

# file1 = open('myfile.txt', 'w')
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# s = "Hello\n"
# file1.write(s)
# file1.writelines(L)
# file1.close()
 

# file1 = open('myfile.txt', 'r')
# print(file1.read())
# file1.close()





# jnfile = open('becuto/myfam.txt','w')
# mem = 'My family has 5 peple \n'
# detail = ['This is my father \n','This is my mother \n','This is my brother \n','This is my baby']
# jnfile.write(mem)
# jnfile.writelines(detail)
# jnfile.close()
# jnfile = open('becuto/myfam.txt','r')

# print(jnfile.read())
# jnfile.close()



# jnlist = [1,3,2,5,2,3,4,5,6]
# jnlist[2] = 7
# for num in jnlist:
#   if num % 2 ==0:
#     print(f'This is not odd num: {num}')
#   else:
#     print(f'this is odd num: {num}')

# jnlistsum = 0
# for num in jnlist:
#   jnlistsum = jnlistsum + num
# print(f'This is the sum of list: {jnlistsum}')

# i = 0
# for num in jnlist:
#   i = 
# print(i)




# jnlist.sort()
# print(set(jnlist))
# jntuple = (2,3,4,5)
# # jntuple[0] = 1
# jndict = {'k1':'thuyen','k2':['khanh','an','giang','lam']}
# jnsub = jndict['k2'][3]
# print(jnsub)


# name = 'Bam'
# if name == 'jennie':
#   print('This is jennie')
# elif name == 'rose':
#   print('This is Rose')
# elif name == 'lisa':
#   print('This is Lisa')
# else:
#   print('This is Jisoo')


# jndict = {'mem1':'JN','mem2':'JS','mem3':'LS','mem4':'RS'}
# for it in jndict.values():
#   print(f'This is {it}')

# jn = 9
# while jn > 0:
#   if jn== 5:
#     continue
#   print(jn)
#   jn = jn - 1


# jnlist = [1,2,3,4,5,6,7,8,9,10,11,12]
# for num in jnlist:
#   if num == 5:
#     continue
#   print(num)
# index = 1
# for num in range(2,12,2):
#   print('The number {} is {}'.format(index,num))
#   index += 1


# fn = 'Nguyen'
# for index,letter in enumerate(fn):
#   print(index)
#   print(letter)
#   print('\n')


# id_count = 0
# fn = 'Nguyen'
# for letter in fn:
#   print(fn[id_count])
#   id_count += 1


# jnl1 = [1,2,3,4]
# jnl2 = ['jn','js','ls','rs']
# for it in zip(jnl1, jnl2):
#   print(it)
# print(list(zip(jnl1, jnl2)))


# from random import randint
# print(f'Chuc mung ban co so may man la: {randint(0,100)}')


# result = (input('Than tuong cua ban la: '))
# print(float(result))
# print(type(result))


# jnlist = []
# for num in range(0,11):
#   if num % 2 ==0:
#     jnlist.append(num)
# print(jnlist)

# jnlist = [num**2 for num in range(0,11) if num % 2 ==0]
# print(jnlist)


# 

# jnlist_tuple =[('thuyen',100),('Khanh',80),('giang',5)]
# def jn_check_salary(jnlist_tuple):
#   def_salary = 0
#   high_salary = ''
#   for name,salary in jnlist_tuple:
#     if salary > def_salary:
#       def_salary = salary
#       high_salary = name
#     else:
#       pass
#   return (high_salary,def_salary)
# print(jn_check_salary(jnlist_tuple))






# jn_list = [' ','O',' ']
# from random import shuffle

# def shuffle_list(jn_listAgr):
#   shuffle(jn_listAgr)
#   return jn_listAgr

# def  your_guess():
#   guess = ' '
#   while guess not in ['0','1','2'] :
#     guess = input('Please choose one of 0 or 1 or 2: ')
#   return int(guess)

# def check_guess(jn_listAgrLam,guessing):
#   if jn_listAgrLam[guessing] == 'O':
#     print('correctly')
#     print(jn_listAgrLam)
#   else:
#     print('wrong')
#     print(jn_listAgrLam)
 
# mix_list = shuffle_list(jn_list)
# # shuffle(jn_list)
# print(mix_list)

# guess = your_guess()
# check_guess(jn_list,guess)


# def spy_game(num_list):
#   temp =[]
#   flag = False
#   for nums in num_list:
#     if nums ==0 :
#       temp.append(nums)
    # elif nums != 0 and nums !=7:
    #   flag = True
      
    # elif nums == 0 and flag ==True:
    #   temp.append(nums)
    # elif nums != 0 and nums !=7:
    #   flag = False
#     elif nums == 7 :
#       temp.append(nums)
#   # return temp
  
#   if temp == [0,0,7]:
#     return True
#   else:
#     return False
# # num_list = [1,2,4,0,0,7,5]
# print(spy_game([1,0,2,0,4,5,7]))





# def myfunc(text):
#     myjoin = []
  
#     for index in range(len(text)):
#         if index%2==0:
#             myjoin.append(text[index].upper())
#         else:
#             myjoin.append(text[index].lower())
#     return ''.join(myjoin)
# print(myfunc('Thanhlam'))
        

# def summer_69(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total
# print(summer_69([1,1,6,2,9,2,6,1,2,9,9,1]))




# def spy_game(nums):
#     zero_counter = 0
#     for number in nums:
#         if number == 0:
#             zero_counter += 1
#         elif number == 7 and zero_counter >= 2:
#             return True
#     return False
# print(spy_game([1,7,2,0,4,7,5,0,2,7]))

# def jn_map(num):
#   return num % 2==0
# jn_arr = [1,2,3,4,5,6,7,8]
# print(list(filter(jn_map, jn_arr)))
# x=[1,2,3,4,5,6,7]
# square = list(map(lambda x: x**2,jn_arr))
# print(square)









# game_list = [0,1,2]
# def display_game(game_list):
#     print("Here is the current list")
#     print(game_list)
# display_game(game_list)
# def position_choice():
    
#     # This original choice value can be anything that isn't an integer
#     choice = 'wrong'
    
#     # While the choice is not a digit, keep asking for input.
#     while choice not in ['0','1','2']:
        
#         # we shouldn't convert here, otherwise we get an error on a wrong input
#         choice = input("Pick a position to replace (0,1,2): ")
        
#         if choice not in ['0','1','2']:
#             # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            
          
#             print("Sorry, but you did not choose a valid position (0,1,2)")
            
    
#     # Optionally you can clear everything after running the function
#     # clear_output()
    
#     # We can convert once the while loop above has confirmed we have a digit.
#     return int(choice)
# def replacement_choice(game_list,position):
    
#     user_placement = input("Type a string to place at the position")
    
#     game_list[position] = user_placement
    
#     return game_list
# def gameon_choice():
    
#     # This original choice value can be anything that isn't a Y or N
#     choice = 'wrong'
    
#     # While the choice is not a digit, keep asking for input.
#     while choice not in ['Y','N']:
        
#         # we shouldn't convert here, otherwise we get an error on a wrong input
#         choice = input("Would you like to keep playing? Y or N ")

        
#         if choice not in ['Y','N']:
#             # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
        
            
#             print("Sorry, I didn't understand. Please make sure to choose Y or N.")
            
    
#     # Optionally you can clear everything after running the function
#     # clear_output()
    
#     if choice == "Y":
#         # Game is still on
#         return True
#     else:
#         # Game is over
#         return False
# game_on = True

# # First Game List
# game_list = [0,1,2]



# while game_on:
    
#     # Clear any historical output and show the game list
    
#     display_game(game_list)
    
#     # Have player choose position
#     position = position_choice()
    
#     # Rewrite that position and update game_list
#     game_list = replacement_choice(game_list,position)
    
#     # Clear Screen and show the updated game list
    
#     display_game(game_list)
    
#     # Ask if you want to keep playing
#     game_on = gameon_choice()

















