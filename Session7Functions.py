'''
# function in python

1. a function can share variable among them using arguments
2. a function can contain doc string which can be used to generate documentation automatically, gives basic details about the function
3.we can access this  doc string using __doc__ attribute
4. now apply the __doc__ attribute to the function
5. a function can return a value using return statement
6. a function can return multiple values using return statement
7. a function can return a function
8. a function can be passed as an argument to another function
9. a variable defined inside a function is local to that function and cannot be accessed outside the function. the scope of the variable is limited to the function it has two types of scope global and local
10. a variable defined outside a function is global to the program and can be accessed anywhere in the program
11. a function can access a global variable but cannot change it but modify

# lambda function

1. a lamda function is a small anonymous function
2. a lambda function can take any number of arguments but can only have one expression
3. lambda arguments : expression
4. lambda functions can be used wherever function objects are required
5. lambda functions are syntactically restricted to a single expression

'''
'''
# def add_square():
#     a = int(input("Enter a number "))
#     b = int(input("Enter another number "))
#     print("Addition Of Square Of Given Numbers")
#     return(print(((a*a)+(b*b))))

# n = int(input("Enter the number of times you want to run the function "))
# for i in range(n):
#     add_square()

# function with arguments
def add_square(a,b):
    print("Addition Of Square Of Given Numbers")
    return(print(((pow(a,2))+(pow(b,2)))))

n = int(input("Enter the number of times you want to run the function "))
for i in range(n):
    a = int(input("Enter a number "))
    b = int(input("Enter another number "))
    add_square(a,b)

# function with doc string
def add_square(a,b):
    #This function adds the square of two numbers
    print("Addition Of Square Of Given Numbers")
    return(print(((pow(a,2))+(pow(b,2)))))
print(add_square.__doc__)

'''

import math
from math import sqrt
global pi 
pi = math.pi
def circle_area(r):
    #This function calculates the area of a circle
    return(pi*r*r)

def CircleArea(r):
    #This function calculates the area of a circle
    return(3.14*r*r)

def CirclePerimeter(r):
    #This function calculates the perimeter of a circle
    return(2*3.14*r)

def SquareArea(s):
    #This function calculates the area of a square
    return(s*s)

def SquarePerimeter(s):
    #This function calculates the perimeter of a square
    return(4*s)

def RectangleArea(l,b):
    #This function calculates the area of a rectangle
    return(l*b)

def RectanglePerimeter(l,b):
    #This function calculates the perimeter of a rectangle
    return(2*(l+b))

def TriangleArea(b,h):
    #This function calculates the area of a triangle
    return(0.5*b*h)

def TrianglePerimeter(a,b,c):
    #This function calculates the perimeter of a triangle
    return(a+b+c)

def SphereArea(r):
    #This function calculates the area of a sphere
    return(4*3.14*r*r)

def SpherePerimeter(r):
    #This function calculates the perimeter of a sphere
    return(2*3.14*r)

def CubeArea(s):
    #This function calculates the area of a cube
    return(6*s*s)

def CubePerimeter(s):
    #This function calculates the perimeter of a cube
    return(12*s)

def CuboidArea(l,b,h):
    #This function calculates the area of a cuboid
    return(2*((l*b)+(b*h)+(h*l)))

def CuboidPerimeter(l,b,h):
    #This function calculates the perimeter of a cuboid
    return(4*(l+b+h))

def CylinderArea(r,h):
    #This function calculates the area of a cylinder
    return(2*3.14*r*(r+h))

def CylinderPerimeter(r,h):
    #This function calculates the perimeter of a cylinder
    return(2*3.14*r)

def ConeArea(r,h):
    #This function calculates the area of a cone
    return(3.14*r*(r+sqrt(h*h+r*r)))

def ConePerimeter(r,h):
    #This function calculates the perimeter of a cone
    return(3.14*r)

def TorusArea(r,R):
    #This function calculates the area of a torus
    return(4*3.14*r*R)

def TorusPerimeter(r,R):
    #This function calculates the perimeter of a torus
    return(2*3.14*R)

print("Welcome to the Area and Perimeter Calculator")
list = ["Circle","Square","Rectangle","Triangle","Sphere","Cube","Cuboid","Cylinder","Cone","Torus"]
print("The list of shapes available are",list)
shape = input("Enter the shape you want to calculate the area and perimeter of ")
if shape == "Circle":
    r = int(input("Enter the radius of the circle "))
    print("The area of the circle is",CircleArea(r))
    print("The perimeter of the circle is",CirclePerimeter(r))
elif shape == "Square":
    s = int(input("Enter the side of the square "))
    print("The area of the square is",SquareArea(s))
    print("The perimeter of the square is",SquarePerimeter(s))
elif shape == "Rectangle":
    l = int(input("Enter the length of the rectangle "))
    b = int(input("Enter the breadth of the rectangle "))
    print("The area of the rectangle is",RectangleArea(l,b))
    print("The perimeter of the rectangle is",RectanglePerimeter(l,b))
elif shape == "Triangle":
    a = int(input("Enter the first side of the triangle "))
    b = int(input("Enter the second side of the triangle "))
    h = int(input("Enter the third side of the triangle "))
    print("The area of the triangle is",TriangleArea(b,h))
    print("The perimeter of the triangle is",TrianglePerimeter(a,b,h))
elif shape == "Sphere":
    r = int(input("Enter the radius of the sphere "))
    print("The area of the sphere is",SphereArea(r))
    print("The perimeter of the sphere is",SpherePerimeter(r))
elif shape == "Cube":
    s = int(input("Enter the side of the cube "))
    print("The area of the cube is",CubeArea(s))
    print("The perimeter of the cube is",CubePerimeter(s))
elif shape == "Cuboid":
    l = int(input("Enter the length of the cuboid "))
    b = int(input("Enter the breadth of the cuboid "))
    h = int(input("Enter the height of the cuboid "))
    print("The area of the cuboid is",CuboidArea(l,b,h))
    print("The perimeter of the cuboid is",CuboidPerimeter(l,b,h))
elif shape == "Cylinder":
    r = int(input("Enter the radius of the cylinder "))
    h = int(input("Enter the height of the cylinder "))
    print("The area of the cylinder is",CylinderArea(r,h))
    print("The perimeter of the cylinder is",CylinderPerimeter(r,h))
elif shape == "Cone":
    r = int(input("Enter the radius of the cone "))
    h = int(input("Enter the height of the cone "))
    print("The area of the cone is",ConeArea(r,h))
    print("The perimeter of the cone is",ConePerimeter(r,h))
elif shape == "Torus":
    r = int(input("Enter the radius of the torus "))
    R = int(input("Enter the major radius of the torus "))
    print("The area of the torus is",TorusArea(r,R))
    print("The perimeter of the torus is",TorusPerimeter(r,R))
else:
    print("Invalid shape entered")

