a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>=b)and(a>=c):
    print("largest of three numbers is ",a)
elif(b>=a)and(b>=c):
    print("largest of three numbers is",b)
else:
    print("largest is",c)