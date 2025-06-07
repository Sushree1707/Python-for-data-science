#Write a program to find out whether a given post is talking about “Harry” or not

post=input("Enter a post : ")

if("harry".lower() in post.lower()):
    print("This post is talking about harry")
else:
    print("This post isn't talking about harry")