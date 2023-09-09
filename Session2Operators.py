print("Hello World")
x = input ("Enter a number: ")
y = input ("Enter another number: ")
z = int(x) + int(y)
print ("The sum of the two numbers is: ", z)

x = int (input ("Enter a number: "))
print(x>100)

x= input()
print(x<4)

x= float(input("Enter a number: "))
y= int(input("Enter another number: "))
print("The sum of the two numbers is: ", x+y)
print(type(x+y))
print("\n")


print("Splitting a number into two parts by Space")
print("Enter two numbers: ")
a,b = input().split(" ")
print("A is",a)
print("B is",b)
print("Splitting a number into two parts by Dot")
c,d = input().split(".")
print("C is",c)
print("D is",d)
print("Sum A+B is",int(a)+int(b))
print("Diffrence A-B is",int(a)-int(b))
print("Product A*B is",int(a)*int(b))
print("Divison A/B is",int(a)/int(b))
print("Mod A%B is",int(a)%int(b))
print("Power A**B is",int(a)**int(b))
print(type(c))
print(type(d))
print("Sum C+D is",float(c)+float(d))
print("Diffrence C-D is",float(c)-float(d))
print("Product C*D is",float(c)*float(d))
print("Divison C/D is",float(c)/float(d))
print("Mod C%D is",float(c)%float(d))
print("Power C**D is",float(c)**float(d))
print("\n")


print("Splitting a number into two parts by Dot")
print("Enter two numbers: ")
a,b=map(int,input().split('.'))
print(a)
print(b)
print(type(a))
print(type(b))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print("\n")


print("Splitting a number into two parts by Comma")
print("Enter two numbers: ")
c,d = map(float,input().split(','))
print(c)
print(d)
print(type(c))
print(type(d))
print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c%d)
print(c**d)
print("\n")



# PYTHON OPERATORS

# Arithmetic Operators
print("Arithmetic Operators")
print("Enter two numbers: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum of the two numbers is: ", num1+num2)
print("Difference of the two numbers is: ", num1-num2)
print("Product of the two numbers is: ", num1*num2)
print("Division of the two numbers is: ", num1/num2)
print("Modulus of the two numbers is: ", num1%num2)
print("Exponent of the two numbers is: ", num1**num2)
print("Floor Division of the two numbers is: ", num1//num2)
print("\n")


# Assignment Operators
print("Assignment Operators")
num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))
num3 += num4
print("Sum of the two numbers is: ", num3)
num3 -= num4
print("Difference of the two numbers is: ", num3)
num3 *= num4
print("Product of the two numbers is: ", num3)
num3 /= num4
print("Division of the two numbers is: ", num3)
num3 %= num4
print("Modulus of the two numbers is: ", num3)
num3 **= num4
print("Exponent of the two numbers is: ", num3)
num3 //= num4
print("Floor Division of the two numbers is: ", num3)
print("\n")


# Comparison Operators
print("Comparison Operators")
num5 = int(input("Enter first number: "))
num6 = int(input("Enter second number: "))
print("Is the first number greater than the second number? ", num5>num6)
print("Is the first number less than the second number? ", num5<num6)
print("Is the first number greater than or equal to the second number? ", num5>=num6)
print("Is the first number less than or equal to the second number? ", num5<=num6)
print("Is the first number equal to the second number? ", num5==num6)
print("Is the first number not equal to the second number? ", num5!=num6)
print("\n")


# Logical Operators
print("Logical Operators")
num7 = int(input("Enter first number: "))
num8 = int(input("Enter second number: "))
print("Is num7 greater than 5 and num8 less than 10? ", num7>5 and num8<10)
print("Is num7 greater than 5 or num8 less than 10? ", num7>5 or num8<10)
print("Is num7 greater than 5? ", not num7>5)
print("\n")


# Identity Operators
print("Identity Operators")
num9 = int(input("Enter first number: "))
num10 = int(input("Enter second number: "))
print("Is num9 the same as num10? ", num9 is num10)
print("Is num9 not the same as num10? ", num9 is not num10)
print("\n")


# Membership Operators
print("Membership Operators")
num11 = int(input("Enter first number: "))
num12 = int(input("Enter second number: "))
list = [1,2,3,4,5]
print(" List = [1,2,3,4,5] ")
print("Is num11 in list? ", num11 in list)
print("Is num12 not in list? ", num12 not in list)
print("\n")


# Bitwise Operators
print("Bitwise Operators")
num13 = int(input("Enter first number: "))
num14 = int(input("Enter second number: "))
print("Bitwise AND of the two numbers is: ", num13 & num14)
print("Bitwise OR of the two numbers is: ", num13 | num14)
print("Bitwise XOR of the two numbers is: ", num13 ^ num14)
print("Bitwise NOT of the two numbers is: ", ~num13)
print("Bitwise Left Shift of the two numbers is: ", num13 << num14)
print("Bitwise Right Shift of the two numbers is: ", num13 >> num14)
print("\n")


# Python Program to find the area of a triangle
print("Python Program to find the area of a triangle")
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is: ", area)
print("\n")


#python program to find area and perimeter of a circle
print("Python Program to find area and perimeter of a circle")
r = float(input("Enter radius of the circle: "))
pi = 3.14
area = pi*r*r
perimeter = 2*pi*r
print("Area of the circle is: ", area)
print("Perimeter of the circle is: ", perimeter)
print("\n")


# Python Program to swap two variables  
print("Python Program to swap two variables")
x = input("Enter first variable: ")
y = input("Enter second variable: ")
# temp = x
# x = y
# y = temp
# x= x+y
# y= x-y
# x= x-y
x,y = y,x
print("The value of x after swapping: ", x)
print("The value of y after swapping: ", y)
print


# Python Program to check if a number is positive, negative or zero
print("Python Program to check if a number is positive, negative or zero")
num = float(input("Enter a number: "))
if num>0:
    print("Positive number")
elif num==0:
    print("Zero")
else:
    print("Negative number")

print("\n")

# Python Program to check if a number is odd or even
print("Python Program to check if a number is odd or even")
num = int(input("Enter a number: "))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

print("\n")

# Python Program to check leap year
print("Python Program to check leap year")
year = int(input("Enter a year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")

else:
    print("Not a leap year")

print("\n")

# python program to take marks of 5 subjects as input out of 100 and calculate average and print percentage (total= 500)

print("Python Program to take marks of 5 subjects as input out of 100 and calculate average and print percentage (total= 500)")
print("Enter marks of 5 subjects: ")
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))
total = sub1+sub2+sub3+sub4+sub5
avg = total/5
percentage = (total/500)*100
print("Total marks is: ", total)
print("Average marks is: ", avg)
print("Percentage is: ", percentage)
print("\n")





