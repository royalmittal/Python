#looping Statemnets

#while loop
#while condition:
#    statement
'''
i=0
print(type(i))
while(i<10):
    print(i)
    i+=1

a=10
add = 0
while(a>0):
    add = add+a
    print(a)
    a-=1
print(add)



for x in range(1,12,12):
    print("Python is easy")


print("Multiplication Table")
i = int(input("Enter the number: "))
for x in range(1,11,1):
    print(i,"*",x,"=",i*x)

#Nested Loop

for x in range(1,6,1):
    for y in range(1,6,1):
        print(x,y)
    print("")

'''
#factorial of a number
k = int(input("Enter the number: "))
fact = 1
for x in range(1,k+1,1):    
    fact = fact*x
print("FACTORIAL OF ",x," IS",fact)









