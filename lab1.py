'''
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

# Example usage:
num =int(input("enter a number to calculate its factorial: "))
result = calculate_factorial(num)
print(f"The factorial of {num} is: {result}")
'''
class FactorialO:
    def __init__(self, n):
        self.n = n

    def calculateFactorial(self):
        if self.n < 0:
            return "Input should be a non-negative integer."
        elif self.n == 0 or self.n == 1:
            return 1
        else:
            result = 1
            for i in range(2, self.n + 1):
                result *= i
            return result

    def __str__(self):
        return f"The factorial of number {self.n} is {self.calculateFactorial()}"

n = int(input("Enter a number: "))
fact = FactorialO(n)
print(fact)
