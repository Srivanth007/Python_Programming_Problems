start = 4
end = 20
for i in range(start, end+1):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
            
    
        