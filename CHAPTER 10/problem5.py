# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint

class Train:
    
    
    def __init__(self,TrainNo):
        self.TrainNo=TrainNo
        
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