'''
#conditional statment in pythomn
#if satement

n= int (input("Enter a number: "))
if(n>3):
    print("Number is greater than 3")

# if statement
# if condition:
#     statement
# else:
#     statement
num = int(input("Enter a number: "))
if(num>0):
    print("Positive number")
else:
    print("Negative number")


ch= input("Enter a character: ")
if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("Vowel")
else:
    print("Consonant")

cha = input("Enter a character: ")
if(cha>='a' and cha<='z'):
    print("Lower case")
else:
    print("Upper case")

b= int(input("Enter a number: "))
c= int(input("Enter a number: "))
d= int(input("Enter a number: "))
if(b>c and b>d):
    print("b is greater")
elif(c>b and c>d):
    print("c is greater")
else:
    print("d is greater")

    

# if else statement
# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

a = int(input("Enter a number: "))
if(a>0):
    print("Positive number")
elif(a<0):
    print("Negative number")
else:
    print("Zero")


# if elif else statement
# if condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

# nested if statement
# if condition:
#     if condition:
#         statement
#     else:
#         statement
# else:
#     statement


year = int(input("Enter a year: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

'''

number = int(input("Enter a number: "))
if(number>0):
    if(number%2==0):
        print("Even number")
    else:
        print("Odd number")
else:
    print("Invalid/Negative number")
    print("Enter a positive number")

