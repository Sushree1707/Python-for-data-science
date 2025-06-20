class Employee:
    company="ITC"
    name="Suraj"
    def show(self):
        print(f"The name of the employee is {self.name} and the company name is {self.company}")
        
class Coder:
    language="Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee,Coder):
    company="Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language}")
        
a=Employee()
b=Programmer()

b.show()
b.printLanguage()
b.showLanguage()