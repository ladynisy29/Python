# # year =int(input("Enter a year: "))

# # if(year%4==0 and year%100!=0) or (year%400==0):
# #     print(f"{year} is a leap year")
# # else:
# #     print(f"{year} is not a leap year")

# # for i in range(1,11,2):
# #     print(i)

# # array= enumerate(["a","b","c"])
# # for i, value in array:
# #     print(i, value)

# # lis= [2,3,4,-5, -6,7]

# # for i in lis:
# #     if i<0:
# #         break
# #     print(i)

# # import random
# # number = random.randint(1,100)


# # while True:
# #     user = int(input("Guess a number: "))
# #     if user == number:
# #         print("You guessed right")
# #         break
# #     else:
# #         if user< number:
# #             print("Inavalid response. Try a higher number")
# #         elif user> number:
# #             print("Inavalid response. Try a smaller number")
# #         continue

# # text = "Text"

# # print(text[::3])

# # name = "Alexander"
# # name = list(name)
# # text =name.reverse()
# # name = ''.join(name)
# # print(name)

# # sen = "I love you so much"
# # sen = sen.split()
# # print(len(sen))

# # array= [x**x for x in range(10)]
# # print(array)

# # array= [x for x in range(10) if x%2==0]
# # array.extend([20,30])
# # print(array)

# # dict = {x:x**2 for x in range(10)}
# # dict.update({100:1000})

# # print(dict)

# # dic = {"name":"Alexander", "age":24}
# # dic= tuple(dic.items())
# # print(dic)

# # lo = dict(dic)
# # print(lo)

# # def name(name, message= "Hello"):
# #     print(f"{name}, {message}")

# # name("Alex")

# # def f(*args):
# #     print(args)

# # f("Love", "You")

# # def l(**args):
# #     print(args)

# # l(name= "Alex", age= 24)

# # def f():
# #     x=1
# #     print(x)

# # f()

# # f= lambda x: x**x
# # f= lambda x,y: x+y

# # n= f(2,3)
# # print(n)

# # numbers= [0, 1, 2]


# # fib = {}

# # a,b = 0,1

# # for i in range(10):
# #     fib[i]= a
# #     a, b =b, a+b 
# # print(fib)

# # re_fib= {values: key for key, values in fib.items()}
# # print(re_fib)

# # list = [2,3,1,5]

# # for i in range(len(list)):
# #     for j in range(i+1, len(list)):
# #         if list[i]> list[j]:
# #             print("It is strictly increasing")
# #         else:
# #             print("It is not strictly increasing")

# # lis = ["art", "stop", "ontinue", "break"]
# # vowels = ["a","e","i","o","u"]

# # fil_lis = [word for word in lis if word[0].lower() in vowels]
# # print(fil_lis)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transposed)

# sen = "I will love you forever, I will always love you"
# words = sen.split()
# word_c= {word: words05
#          .count(word) for word in words}
# print(word_c)



# x = [2, 3, 4]
# def  fun(x):
#   return x+1
# y= list(map(fun, x))
# print(y)

# class Person:
#     def __inti__(self, name, age):
#         self.name= name
#         self.age= age

# class Animal:
#     def __init__(self, voice):
#         self.voice= voice
  
# cat = Animal("Meow")
# print(cat.voice)

# dog = Animal("Woof")
# print(dog.voice)

# N1 =1
# D1= 2

# N2 = 2
# D2 = 3

# print(f"{(N1*D2+N2*D1)}/{(D1*D2)}")


# class Fraction:
#     def __init__(self,x=0,y=1):
#         self.x=x
#         self.y=y
#     def print(arg):
#         print(arg.x, '/', arg.y)

# f1 = Fraction(1)
# f2 = Fraction(2,3) 

# f1.print()


# class Fraction:
#     def __init__(self, N1, N2, D1, D2):
#         self.N1 = N1
#         self.N2 = N2
#         self.D1 = D1
#         self.D2 = D2
 
#     def print(self):
#         print(f"{(self.N1*self.D2+self.N2*self.D1)}/ {self.D1*self.D2}")

# f1= Fraction(1,2,2,3)
# f1.print()

# class Counter:
#     def __init__(self, start=0):
#         self.count = start
#     def increment():


# class Animal:
#     def _init__(self,name):
#         self.name = name
#     def speak(self):
#         pass
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
# dog=Dog()  
# if __name__ == "__main__":
#     animals = [dog]
#     for animal in animals:
#         print(f"{dog.speak()}")

from math import gcd

class Fraction:
    def __init__(self, x=0, y=1):
        self.__num=x
        self.__den=y
        self.simplify()

    def setNum(self, x):
        self.__num=x
        self.simplify() 

    def setDen(self,y):
        self.__den=y
        self.simplify()

    def __add__(self, other):
        num = self.__num*other.__den+self.__den*other.__num
        den = self.__den*other.__den
        return Fraction(num,den)
    

    def simplify(self):
        common_divisor = gcd(self.__num, self.__den)
        self.__num //= common_divisor
        self.__den //= common_divisor
        if self.__den < 0:  # Keep denominator positive
            self.__num = -self.__num
            self.__den = -self.__den

    def __str__(self):
        print(self.__num, '/', self.__den)

  
f1 = Fraction(1,2)
f2= Fraction(2,3)

f1.print()
f2.print()
