#Write a program to print multiplication table of a given number using while loop.
n=int(input("Enter a number you want multiplication table of : "))

i=1
while i in range(1,11):
    print(f"{n} x {i} = {n * i}")
    i+=1