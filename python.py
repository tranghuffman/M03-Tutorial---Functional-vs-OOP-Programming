class do_math:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    
    def subtraction(self):
        return self.val1 - self.val2
    def division(self):
        return self.val1 // self.val2

math_instance = do_math(15, 5)
print(math_instance.subtraction()) 
print(math_instance.division())