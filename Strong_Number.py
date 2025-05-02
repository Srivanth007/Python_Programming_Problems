num = int(input("enter number to find its strong number or not: "))
temp = num
sum_of_factorial = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1,digit+1):
        fact = fact * i
    sum_of_factorial += fact
    temp = temp//10

if sum_of_factorial == num:
    print("strong number")
else:
    print("not strong number")

