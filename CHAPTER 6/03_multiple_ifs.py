a=int(input("Enter your age : "))

#if statement no:1
if(a%2==0):
    print("a is even")
#end of if statement no:1

#if statement no:2 
if(a>=18):
    print("You are above the age of consent")
elif(a<0):
    print("You are entering a wrong age")
else:
    print("You are below the age of consent")
#end of if statement no:2

print("End of program")