

# Inheritance Example: 
class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")
        

# To add Inheritance, add the parent class in as a parameter
class Fish(Animal):

    def __init__(self):
        '''To get a hold of all Animal attributes, use super.__init__()'''
        super().__init__()
        
    def swim(self):
        print("moving in water.")

    '''MODIFY a parent class method - super().parent_method()'''
    ''' (Sec 21. V153 at (5:30) )'''
    def breathe(self):
        super().breathe()
        print("doing this underwater.")


nemo = Fish()
nemo.swim()

print(nemo.num_eyes)

nemo.breathe() #returns both parent statement and child statement (under water)

# ******** Resume Sec 21. V.154  