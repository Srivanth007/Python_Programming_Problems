num = int(input())
factor = []
i = 2
while i<= num:
    if num % i == 0:
        factor.append(i)
        num //= i
    else:
        i = i + 1
print(factor)