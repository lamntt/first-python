def count_primes(num):
  
  arr = []
  for nums in range(2,num):
    flag=True
    for i in range(2,nums):
        if nums % i == 0:
          flag=False
          break
    if flag == True:
      arr.append(nums)
  return len(arr)
print(count_primes(100))