class Employee:
    no_of_leaves = 9

    def __init__(self, name, salary, role):
        self.name = name 
        self.salary = salary
        self.role = role
    @classmethod
    def from_str(cls, string):
    #params = string.split("-")
    #print(params)
    #return cls(params[0], params[1], params[2])
     return cls(*string.split("-"))

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves 

aditya = Employee.from_str("Aditya-675634-Programmer")

print(aditya.no_of_leaves)
aditya.change_leaves(34)
print(aditya.no_of_leaves)
