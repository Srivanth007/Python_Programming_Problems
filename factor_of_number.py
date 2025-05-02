num = int(input())
factor = []
for i in range(2, num):
    if num % i == 0:
        factor.append(i)
print(factor)