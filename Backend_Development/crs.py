# Create a class Account that must have these two instance 
# Attributes: ID (a string of a 5 digit number that identifies a specific individual), and name (a string).
class Account:
    def __init__(self, ID:str, name:str):
        self.id = ID
        self.name = name

# StudentAccount must inherit from Account, have 3 additional instance attributes named classes, 
# is_enlistment_locked and is_enlisted, and 2 methods named add_class() and lock_enlistment(). 
class StudentAccount(Account):
    def __init__(self, ID:str, name:str):
        super().__init__(ID, name)
        self.classes = []
        self.is_enlistment_locked = False
        self.is_enlisted = False
        
    def add_class(self, subject:str):
        self.classes += [subject]
    
    def lock_enlistment(self):
        self.is_enlisted = True
        print(f"{self.name} has locked enlistment")

# AdviserAccount must inherit from Account too, and have 2 additional instance attributes 
# named advisees and enlisted advisees, and have 3 methods named add_advisee(), print_advisees(), and lock_enlistment_for().  
class AdviserAccount(Account):
    def __init__(self, ID: str, name: str):
        super().__init__(ID, name)
        self.advisees = []
        self.enlisted_advisees = []
    
    def add_advisee(self, advisee:StudentAccount):
        self.advisees += [advisee]
        print(f"{self.name} has added {advisee.name} as an advisee")
    def print_advisees(self):
        print(f"{self.name}'s students: {', '.join([x.name for x in self.advisees])}")

    def lock_enlistment_for(self, advisee:StudentAccount):
        if advisee not in self.advisees:
            print(f"Error: {advisee.name} is not an advisee of {self.name}")
            return
        if advisee.is_enlisted == False:
            print(f"Error: {advisee.name}'s enlistment is not locked yet")
            return
        advisee.is_enlistment_locked = True
        print(f"{advisee.name} is now enlisted")
        



#Test Code
student1 = StudentAccount("05524", "Ross")
student1.add_class("Class 1")
student1.add_class("Class 2")
student1.add_class("Class 4")
student1.lock_enlistment()


adviser = AdviserAccount("01341", "Rachel")
adviser.add_advisee(student1)
adviser.lock_enlistment_for(student1)


student2 = StudentAccount("12345", "Chandler")
student2.add_class("Class 1")
student2.add_class("Class 3")


adviser.add_advisee(student2)
adviser.lock_enlistment_for(student2)


student3 = StudentAccount("01353", "Joey")
student3.add_class("Class 5")
student3.add_class("Class 9")


adviser.lock_enlistment_for(student3)
