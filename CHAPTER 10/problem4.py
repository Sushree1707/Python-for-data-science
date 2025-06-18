#Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,n):
        self.n=n
        
        
    def square(self):
        print(f"The square is {self.n*self.n}")
        
        
    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")
        
        
    def squareroot(self):
        print(f"The square is {self.n**1/2}")
    
    @staticmethod
    def greet():
        print("Hey!! Good Morning.")
        
a=Calculator(4)
a.greet()
a.square()
a.cube()
a.squareroot()