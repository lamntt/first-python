# # 1
# import math


# class Line:
#     def __init__(self, coord1, coord2):
#         self.coord1 = coord1
#         self.coord2 = coord2

#     def distance(self):
#         return math.dist(self.coord1, self.coord2)

#     def slope(self):
#         x1, y1 = self.coord1
#         x2, y2 = self.coord2
#         return (y2 - y1) / (x2 - x1)


# coordinate1 = (3, 2)
# coordinate2 = (8, 10)
# li = Line(coordinate1, coordinate2)
# print(li.slope())


# #2
# pi = 3.141592653589793


# class Cylinder:
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume(self):
#         return pi * (self.radius ** 2) * self.height

#     def surface_area(self):
#         return 2 * pi * (self.radius ** 2) + 2 * pi * self.radius * self.height


# cy = Cylinder(2, 3)
# print(cy.surface_area())


# 3 Gain product
# class Account:
#     product = []

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.isLogin = False

#     def login(self, username, password):
#         if self.username == username and self.password == password:
#             print("Login successfully")
#             self.isLogin = True
#         else:
#             self.isLogin = False
#             print("Login failed")

#     def add_to_cart(self, product):
#         self.product.append(product)

#     def get_cart(self):
#         print(self.product)


# ac1 = Account("giang", 123)
# ac1.login("giang", 123)
# if ac1.isLogin:
#     ac1.add_to_cart("skin product")
#     ac1.get_cart()


# Challenge
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner : {self.owner} has {self.balance} in account"

    def deposit(self, money):
        self.balance += money
        print(f"Deposit accepted. Your currently balance is {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print("Your balance is not enough")
        if money <= self.balance:
            self.balance -= money
            print(f"Withdraw accepted. Your currently balance is {self.balance}")


ac = Account("Jennie", 100)
print(ac)
ac.deposit(50)
ac.withdraw(150)
