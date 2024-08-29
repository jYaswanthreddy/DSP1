n = int(input("enter the length of the array: "))
arr =[]
for i in range(0,n):
  arr.append(input())
sum1 = (n*(n+1)/2)
sum2 = 0
for i in range(0,n):
  sum2 = sum2 + int(arr[i])

missing_value = sum1 - sum2
print("The missing value is : ", missing_value)