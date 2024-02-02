class InvalidEmployeeException(Exception):
    pass
class Project:
    def __init__(self,employee_list):
        self.__employee_list=employee_list

    def validate_employee(self,employee_id):
        flag=False
        for key in self.__employee_list:
            if(key==employee_id):
                flag=True
        if(flag==False):
            raise InvalidEmployeeException
            print("1")
        return True

project1=Project([1001,1002,1003])
try:
    print(project1.validate_employee(1005))
except Exception:
    print("2")
except InvalidEmployeeException:
    print("3")