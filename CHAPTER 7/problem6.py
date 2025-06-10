#Write a program to calculate the factorial of a given number using for loop.

#using while loop
n=int(input("Enter a number : "))

fact=1
i=1
while(i<=n):
    fact*=i
    i+=1
print(fact)


#using for loop
n=int(input("Enter a number : "))
fact=1
for i in range(1,n+1):
    fact*=i
    i+=1

print(f"The factorial of {n} is {fact}")