from employee import Employee ,create_employee

#And also check why __pycache file is created in the directory
#What is __name__ ? 
if __name__ == "__main__":                #check whats happening?
    print("In main*********************",__name__)
    employee_denver = create_employee('Denver','HR',67000)
    employee_denver.display_details()
    employee_jessica = Employee('Jessica','sales',69000)
    employee_jessica.display_details()