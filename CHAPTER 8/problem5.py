#Write a program to find the sum of first n natural numbers using while loop.
#1+2+3+4...+n
n=int(input("Enter the number : "))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)