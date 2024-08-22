x = float(input("enter the first value: "))
y = float(input("enter the second value: "))

operator = input(" enter the operator: (+, - ,* /): ")

if operator == '+':
    print("ans = ", x+y)

elif operator == '-':
    print("ans = ", x-y)

elif operator == '*':
    print("ans = ", x*y)
elif operator == '/':
    print("ans = ", x/y )
else:
  print("Pleae, enter the correct operator and the value !!!!")  