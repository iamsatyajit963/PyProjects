class Example:
    num=10
    @staticmethod
    def add(num1,num2):
        result=(num1+num2)*Example.num
        return result
print(Example.add(100, 200))