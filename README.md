
# Classmethods
this project is related to classes in python


## Explanation 

this is documentation

class Employee:

this line makes a new class

no_of_leaves = 9

this line makes a new varible of this class

def __init__(self, name, salary, role):
        self.name = name 
        self.salary = salary
        self.role = role

this line makes a constructer for the class

aditya = Employee("Aditya" , 675634 , "Programmer")    

this line makes a object of Employee class

print(aditya.no_of_leaves)

this function prints no_of_leaves of aditya if aditya object does
not have any varible of no_of_leaves it will search in the class 
that is there any varible like that 

print(aditya.__dict__)

this prints the properties of aditya object

Employee.no_of_leaves = 38

this function changes the no_of_leaves given by the Employee class
to 38

print(aditya.no_of_leaves)

this function will now print 38 because no_of_leaves have been changed
by the Employee class

print(aditya.__dict__)

this again will print properties of aditya object

aditya.no_of_leaves = 100

this function will make aditya object one personal varible
which is no_of_leaves

print(aditya.no_of_leaves) 

now this function will print the no_of_leaves value which only aditya object has

print(aditya.__dict__)

this again will print properties of aditya object but the changed
is it will show one more properties of aditya which is aditya's personal varible

print(Employee.no_of_leaves)

Employee no_of_leaves will be same only because only Employee can change it's varible
value objects can only use it