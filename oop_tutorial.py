class do_math:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        
    def subtract(self):
        return self.val1 - self.val2
    
    def divide(self):
        return self.val1 // self.val2
    
math_instance = do_math(10, 5)

print(math_instance.subtract())
print(math_instance.divide())