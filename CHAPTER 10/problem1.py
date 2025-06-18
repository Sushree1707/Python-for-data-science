# Create a class “Programmer” for storing information of few programmers working at Microsoft

class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode


p=Programmer("Harry", 130000,253771)
print(p.name,p.salary,p.pincode,p.company)
s=Programmer("Suraj", 250000,758291)
print(s.name,s.salary,s.pincode,s.company)