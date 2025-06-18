


class Employee:
    language="Py" #This is a class attribute
    salary=120000
    language="Py" 
    
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good Morning!!")
    
harry=Employee()
harry.greet()
harry.getInfo() #is also read as Employee.getInfo(harry)


