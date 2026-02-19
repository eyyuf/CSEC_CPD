matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row , col = i+1 , j+1
            break
m = abs(row-3) + abs(col-3)
print(m)
        
