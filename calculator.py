def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print ("Menu Driven Program")
print ("1.Addition")
print ("2.Subtraction")
print ("3.Multiplication")
print ("4.Division")

while True:
    choice = input("Enter Choice : 1/2/3/4")
    num1 = float(input("Enter First Number "))
    num2 = float(input("Enter Second Number "))
    if choice == '1':
        print (num1,"+",num2,"=",add(num1,num2))
    elif choice == '2':
        print (num1,"-",num2,"=",sub(num1,num2))
    elif choice == '3':
        print (num1,"*",num2,"=",mul(num1,num2))
    elif choice == '4':
        print (num1,"/",num2,"=",div(num1,num2))
    else: 
        print("BYE")