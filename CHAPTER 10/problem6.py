#Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

from random import randint

class Train:
    
    
    def __init__(slf,TrainNo):
        slf.TrainNo=TrainNo
        #nothing will change but for a good practice and readability we have to do this
        
        
    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.TrainNo} from {fro} to {to}")
        
    
    def get_status(self):
        print(f"Train no: {self.TrainNo} is running now.")
    
    def get_fare(self,fro,to):
        print(f"Ticket fare in train no:{self.TrainNo} from {fro} to {to} is {randint(222,5555)}")
    

t=Train(3334221)
t.book("Rampur","Delhi")
t.get_status()
t.get_fare("Rampur", "Delhi")