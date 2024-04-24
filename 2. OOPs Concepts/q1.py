# @author: 22000214 - Abhiraj Chaudhuri
# @description: Program No. 1. Write a OOP in python to input empid, name, basic salary, no. of experience in yrs.
# Calculate hra(35% of basic), da (58% of basic) and pf (9.5% of basic).
# Also calculate bonus based on experience in years.
# If experience in years is >= 30, bonus must be 59% of basic,
# If experience in years is >=23, bonus must be 51% of basic,
# If experience in years is >=15, bonus must be 45% of basic,
# If experience in years is >=7, bonus must be 33% of basic,
# If experience in years is <7, bonus must be 16% of basic
# Calculate netsalary as basic+da+hra-pf+bonus.
# Create a class, constructor to create instance variables, getter-setter for each variable,
# calculative functions for operative variables. A class methods/function should not contain

class Employee:
    def __init__(self, empID, name, salary, experience):
        self.empID = empID
        self.name = name
        self.salary = salary
        self.experience = experience

    def getDetails(self):
        return self.empID, self.name, self.salary, self.experience

    def setDetails(self, empID, name, salary, experience):
        self.empID = empID
        self.name = name
        self.salary = salary
        self.experience = experience

    def hra(self):
        return self.salary * 0.35

    def da(self):
        return self.salary * 0.58

    def pf(self):
        return self.salary * 0.095

    def bonus(self):
        if self.experience >= 30:
            return self.salary * 0.59
        elif self.experience >= 23:
            return self.salary * 0.51
        elif self.experience >= 15:
            return self.salary * 0.45
        elif self.experience >= 7:
            return self.salary * 0.33
        else:
            return self.salary * 0.16

    def netSalary(self):
        hra = self.hra()
        da = self.da()
        pf = self.pf()
        bonus = self.bonus()
        return self.salary + hra + da - pf + bonus

empID = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
salary = float(input("Enter Employee Salary: "))
experience = int(input("Enter Employee Experience in Years: "))

employee = Employee(empID, name, salary, experience)

print("HRA: ", employee.hra())
print("DA: ", employee.da())
print("PF: ", employee.pf())
print("Bonus: ", employee.bonus())
print("Net Salary: ", employee.netSalary())

#output:
# Enter Employee ID: 214
# Enter Employee Name: Abhie
# Enter Employee Salary: 125000
# Enter Employee Experience in Years: 8
# HRA:  43750.0
# DA:  72500.0
# PF:  11875.0
# Bonus:  41250.0
# Net Salary:  294375.0