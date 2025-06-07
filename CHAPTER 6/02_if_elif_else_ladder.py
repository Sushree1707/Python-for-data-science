a=int(input("Enter your age : "))

if(a>=18):
    print("You are above the age of consent")
elif(a<0):
    print("You are entering a wrong age")
elif(a==0):
    print("You are entering 0 which is not valid") 
else:
    print("You are below the age of consent")

print("End of program")