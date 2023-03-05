#python program using functions/methods utilizing both OOP and finctional paradigms for a subtraction and division function.

class do_math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def subtraction(self):
        return self.num1 - self.num2
    def division(self):
        return self.num1 // self.num2

math_instance = do_math(15, 5)
print(math_instance.subtraction()) 
print(math_instance.division())