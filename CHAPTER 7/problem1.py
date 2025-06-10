#Write a program to print multiplication table of a given number using for loop.

n=int(input("Enter a number you want multiplication table of : "))

for i in range(1,11):
    print(f"{n} x {i} = {n * i}")