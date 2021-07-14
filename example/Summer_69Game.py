def summer_69(arr):
  total = 0
  add = False
  for nums in arr:
    if nums != 6 and add == False:
      total += nums
    elif nums == 6 :
      add = True
      total = total
    elif nums == 9 :
      add = False
      total = total
    
      
  return total

print(summer_69([1,1,6,2,9,2,6,1,2,9,9,1]))