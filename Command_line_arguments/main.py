import sys
from employee import create_employee
#The below line will be true only if below line is true
#if __name__ == '__main__':

#    print('Number of command line arguments: ', len(sys.argv))
#    print('Script name: ',sys.argv[0])    #sys.argv is a list with the command-line arguments
#   print('All arguments: ', sys.argv)

    #if we use below the program willl be messy so we use argparse module

#    print('All arguments: ',sys.argv)

#   name = sys.argv[1]
#    department = sys.argv[2]
#    salary = int(sys.argv[3])

#    emp = create_employee(name,department,salary)
#    emp.display_details()

#sys module is little messy because if any user uses he dont know the order that has to be given .
#every argument in argv list is str sometimes we need to convert other data types so we use argparse

import argparse 

parser = argparse.ArgumentParser(description = 'parsing employee details')

parser.add_argument('--name', help='Please specify employee name',type = str)

parser.add_argument('--department',help = 'Please specify employee department')

parser.add_argument('--salary',help = 'Please specify employee salary',type=int)

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    emp = create_employee(args.name,args.department,args.salary)
    emp.display_details()

#if we add extra argument in cli it throws unrecognized error