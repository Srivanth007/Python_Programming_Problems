num1 = 20 
num2 = 40
if num1 > num2:
    print("num1 is greater than num2") 
else:
    print("num2 is greater than num1")

num3 = 10
if num1 > num2 and num1 > num3:
    print("num1 is greater")
elif num2 > num1 and num2 > num3:
    print("num2 is greater")
else:
    print("num3 is greater")