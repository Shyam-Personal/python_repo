class Person:
    adhaar_no = 1
    def __init__(self,name,dob,gender):
        self.__adhaar_no = Person.adhaar_no # Private variable
        Person.adhaar_no += 1
        self.__name = name
        self.__dob = dob
        self.__gender = gender
        
    def setName(self,name):
        self.__name = name
        
    def changeDOB(self,dob):
        self.__dob = dob
    
    def getDOB(self):
        return self.__dob
        
class Employee(Person):
    employee_id = 1
    def __init__(self, name, dob, gender, company_name, salary, years_of_exp): # Parent class __init__ i.e. constructor method needs to call explicitly 
        Person.__init__(self, name, dob, gender)
        self.__company_name = company_name
        self.__salary = salary
        self.__years_of_exp = years_of_exp
        self.emp_id = Employee.employee_id 
        Employee.employee_id += 1
        
    def setCompanyName(self,company_name):
        self.__company_name = company_name
        
    def getYearsOfExperience(self):
        return self.__years_of_exp
    
    def getCompanyName(self):
        return self.__company_name
    
    def updateSalary(self,update_percentage):
        self.__salary = self.__salary + (self.__salary * update_percentage)/100
        
        
def main():
    vitthal = Employee("Vitthal", "29-12-1988", "Male", "Stellus", 100000, 3)
    print(vitthal.getCompanyName())
    print(vitthal.getDOB())
    print(vitthal.changeDOB("12-12-1989"))
    print(vitthal.getDOB())
    
    print(vitthal.adhaar_no)

if __name__ == "__main__":
    main()