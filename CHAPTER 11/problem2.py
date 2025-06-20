#Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    print("There are different types of animals.")

class Pets(Animals):
    print("Among different types of animals there are some pets.")

class Dogs(Pets):
    @staticmethod
    def bark():
        print("Among the pets some are dogs.")

d=Dogs()
d.bark()