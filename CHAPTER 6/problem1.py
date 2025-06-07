#Write a program to find the greatest of four numbers entered by the user.

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))
d=int(input("Enter a number : "))

if(a>b and a>c and a>d):
    print("a is the greatest.")
elif(b>a and b>c and b>d):
    print("b is the greatest.")
elif(c>a and c>b and c>d):
    print("c is the greatest.")
else:
    print("d is the greatest")