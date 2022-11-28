#oop 
#polymorphism

#1)overloading-->method/constructor
#2)overriding--> method/constructor
#3) overloading --> operator

# class A:
#     # def __init__(self):
#     #     print('parameter less constructor')
#     def __init__(self, param1=None):
#         print("Default parameter constructor")
#     def __init__(self, *param1):
#         print("Arbitrary parameter constructor")

#     def display(self):
#         print("Display method")
#     def display(self, offset=None):
#         print("Display method")

# a1=A(1,2,3,4,5)
# print(a1.display())
# a2=A(10)
# print(a2)

#method overriding-->
# class A:
#     def __init__(self):
#         print("From class A init.")
#     def show(self):
#         print("Show from class A.")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("From class B init.")
#     def show(self):
#         print("Show from class B.")
# b1=B()
# print(b1.show())


#operator overloading-->

class Student:
    def __init__(self, m1, m2):
        self.m1= m1
        self.m2= m2
    def __gt__(self,other):
        return s1.m1 + s1.m2 > s2.m1+s2.m2
    def __lt__(self, other):
        return s1.m1+s1.m2 < s2.m1+s2.m2
    def __add__(self, other):
        return (s1.m1+s1.m2) + (s2.m1+s2.m2)
s1= Student(85, 75)
s2= Student(80, 90)
print(s1 > s2)
print(s1 + s2)
# print(s1>s2)
# print(169 > 170)

