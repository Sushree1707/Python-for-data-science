


class Employee:
    language="Py" #This is a class attribute
    salary=120000
    language="Py" 
    
    def __init__(self,name,salary,language): #dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")
        
        
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
        
        
    @staticmethod
    def greet():
        print("Good Morning!!")
    
harry=Employee("Suraj",1300000,"Javascript")
# harry.name="Harry"
print(harry.name,harry.salary,harry.language)

