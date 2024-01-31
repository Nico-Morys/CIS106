class Student:
    def __init__(self, first, last, dcode, credits):
        self.first = first
        self.last = last
        self.dcode = dcode
        self.credits = credits
        

    def tuition(self, dcode):
        if dcode == "I":
            cost = 250
        else: cost = 500
        
        tuitionowed = float(self.credits) * float(cost)
        return tuitionowed
    

student1 = Student('Nico', 'Morys', 'I', 12)

print("Student First Name: ", student1.first)
print("Student Last Name: ", student1.last)
print("Student District Code: ", student1.dcode)
print("Students Amount of Credits: ", student1.credits)
print("Students Tuition: $", student1.tuition("I"))





