#Write a program which finds out whether a given name is present in a list or not.
list1=["Suraj","Sushree","Sunil","Anuj"]

name=input("Enter the name : ")
if(name in list1):
    print("Name is present")
else:
    print("Name is not present")