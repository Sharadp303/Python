# class Employee:
#     salary=50
#     name="Sharad"
#     def getsalary(self):
#         return self.salary

class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary= salary
    def getSalary(self):
        print(self.salary)
    
rohan= Employee("Rohan",5555)
print(rohan.salary)
print(rohan.name)
rohan.getSalary()

sharad= Employee("Sharad",150000000)
print(sharad.salary)
print(sharad.name)

