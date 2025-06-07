#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

maths=int(input("Enter the marks of maths : "))
science=int(input("Enter the marks of science : "))
english=int(input("Enter the marks of english : "))

#check the percentage
total_percentage=(100*(maths+science+english))/300

if(total_percentage>=40 and maths>=33 and science>=33 and english>=33):
    print("You are pass",total_percentage)
else:
    print("You are fail",total_percentage)