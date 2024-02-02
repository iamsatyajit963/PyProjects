# An Organization has decided to provide salary hike to its empolyee based on their job. 
# Employees can be in job levels 3, 4, or 5. Hike percentage based on the job levels are given below
# Job Level	    Hike Percentage (Applicable on current salary)
# 	3			    15
# 	4			    7
# 	5			    5
# In case of invalid job level, consider hike percentage to be 0
# Given the current salary and the job level, write a python program to find and display the new salary of an employee.

sal = int(input("Enter the salary: "))
jl = int(input("Enter the job level(3,4,5): "))

if (jl == 3):
    sal+=sal*0.15
    print("New Salary= " + str(sal))
elif (jl == 4):
    sal+=sal*0.07
    print("New Salary= " + str(sal))
elif (jl == 5):
    sal+=sal*0.05
    print("New Salary= " + str(sal))
else:
    print("New Salary= " + str(sal))