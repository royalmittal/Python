# Modules in Python
'''
#import operator
import operator

print("Operator Module: ")
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
op = input("Enter an operator: ")
#print(operator.add(x, y))
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
print(ops[op](x, y))



#import random
import random
print("Random Module: ")
print("Random number between 0 and 1: ")
print(random.random())
print("Random number between 1 and 10: ")
print(random.randrange(1, 10))
print("Random number between 1 and 10: ")
print(random.randint(1, 10))
print("Random Choice: ")
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Random Choice: ")
print(random.choice("Hello World!"))
print("Random Choice: ")
print(random.choice(["Hello", "World", "!"]))
print("Random Shuffle: ")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list)
print(list)



# import string 
import string
print("String Module: ")
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)



#import math
import math
print("Math Module: ")
print("PI",math.pi)
print("Exponent",math.e)
print("Tau",math.tau)
print("Infinity",math.inf)
print("NaN",math.nan)
print("Positive Infinity",math.inf)
print("Negative Infinity",math.inf)
#ceil = prints the next highest integer
print("Ceil library",math.ceil(10.1))
print(math.ceil(10.9))
#floor = prints the next lowest integer
print("Floor Library",math.floor(10.1))
print(math.floor(10.9))
print(math.pow(2, 3))
#sqrt = square root
print("Square Root",math.sqrt(100))
#log = logarithm
print("Logarithm",math.log(100, 10))
#sin = sine
print("Sine",math.sin(10))
#cos = cosine
print("Cosine",math.cos(10))
#tan = tangent
print("Tangent",math.tan(10))
#factorial 
print("Factorial",math.factorial(5))
#degrees
print("Degrees",math.degrees(10))
#radians
print("Radians",math.radians(10))
#modf
print("Modf",math.modf(10.5))
#gcd
print("GCD",math.gcd(10, 5))
#lcm
print("LCM",math.lcm(10, 5))



# import time
# import datetime
# import calendar

import time
print("Time Module: ")
curr = time.time()
print("Current Time -",curr)
print("Current System Time -",time.ctime(curr))

import calendar
print("Calendar Module: ")
print("May'23 Calendar -",calendar.month(2023,5))
#print(calendar.calendar(2020))

import datetime
print("Datetime Module: ")
print("Current Date -",datetime.date.today())
print("Current Date -",datetime.date.today().strftime("%d/%m/%Y"))


# import os
print("OS Module: ")
import os
print("Current Working Directory -",os.getcwd())
print("List of Files -",os.listdir())
print("List of Files -",os.listdir("C:\\Users\\Saurabh\\Desktop\\Python\\Session5"))



# import sys    
print("Sys Module: ")
import sys
print("System Path -",sys.path)
print("System Version -",sys.version)
print("System Platform -",sys.platform)
print("System Modules -",sys.modules)
print("System Executable -",sys.executable)
print("System Byte Order -",sys.byteorder)
print("System Maxsize -",sys.maxsize)



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
a = int(input("Enter a number: "))
print("Factorial of",a,"is",factorial(a))

'''
import operator
def factorial():
    x = int(input("Enter a Number for Factorial: "))
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    print("Factorial of",x,"is",fact)

def Calculator():
    x = int(input("Enter a Number: "))
    y = int(input("Enter another Number: "))
    op = input("Enter an Operator: ")
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    print(ops[op](x, y))

def square_root():
    a = int(input("Enter a Number for Square Root"))
    ans = pow(a, 0.5)
    print("Square Root of",a,"is",ans)


factorial()
square_root()
Calculator()
