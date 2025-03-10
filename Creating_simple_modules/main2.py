class Employee:
    __organization = 'Skillsoft'

    def __init__(self,name,department,salary):
        self.__name = name 
        self.__department = department
        self.__salary = salary 

    def display_details(self):
        print(f"Name:-{self.__name}")
        print(f"Department:-{self.__department}")
        print(f"Salary:-{self.__salary}")
        print(f"Organization:-{Employee.__organization}")

#employee_denver = Employee('Denver','HR',67000)
#employee_denver.display_details()

def create_employee(name,department,salary):
    employee = Employee(name,department,salary)
    return employee 

if __name__ == "__main__":                #check whats happening?
    print("*********************",__name__)
    employee_denver = create_employee('Denver','HR',67000)
    employee_denver.display_details()