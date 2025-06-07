#Write a program to find whether a given username contains less than 10 characters or not

username=input("Enter a name : ")
l=len(username)

if(l<10):
    print("Your username contains less than 10 characters.")
else:
    print("All is well!!")