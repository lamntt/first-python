# import shutil
# shutil.move('practices.txt','E:\backgound')
\


from collections import Counter
mylist = [1,5,4,7,1,2,2,2,4,7,'a','a']
print(list(Counter('aaaaaaaaaggggggggggggeeeeeeeeeeeeeehhhhhhhhhhhhhhttttttt')))
print(Counter(mylist))
c = Counter(mylist)
print(c.most_common(2))





from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])

sam = Dog(age=2,breed='Lab',name='Sammy')

frank = Dog(age=2,breed='Shepard',name="Frankie")

print(sam.age)
