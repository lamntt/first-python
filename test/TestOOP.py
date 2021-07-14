# class BlackPink:
#     def __init__(self, name, national):
#         self.name = name
#         self.national = national


# my_girl = BlackPink(name="Jennie", national="New Zealand")
# print(my_girl.name)


# # method
# class Dog:
#     species = "mammal"

#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def bark(self, number):
#         print(
#             f"My dog have name is {self.name} and is {self.species} have number {number} "
#         )


# my_dog = Dog("Lucky", "White")
# print(my_dog.bark(10))
# print(my_dog.species)


# # inheritance
class BlackPink:
    def __init__(self, name, national):
        self.name = name
        self.national = national

    def song(self):
        print("How you like that")


class Bias(BlackPink):
    def __init__(self, name, national):
        BlackPink.__init__(self, name, national)

    def song(self):
        print("Lovesick girls")

    def company(self):
        print("YG entertainment")


my_love = Bias("Jennie", "New Zealand")
print(my_love.song())


# # polymornism


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(People):
    def classroom(self):
        return self.name + " is " + self.age + " years old. "


class Teacher(People):
    def room(self):
        return self.name + " is " + self.age + " years old. "


# st = Student("Jen", "twenty")
# tc = Teacher("Jisoo", "twenty two")
# print(tc.room())


# ## magic/ dunder


# class BP:
#     def __init__(self, name, prize):
#         self.name = name
#         self.prize = prize

#     def __str__(self):
#         return f"{self.name} has {self.prize} prize"

#     def __len__(self):
#         return self.prize


# jn = BP("Jennie", 15)

# print(len(jn))
