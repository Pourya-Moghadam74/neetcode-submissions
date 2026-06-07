import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args):
        if len(args) == 1:
            radius = args[0]
            return round(math.pi * (radius ** 2), 2)
        else:
            return (args[0] * args[1])
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))