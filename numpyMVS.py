import numpy as np
r,c = map(int,input().split())
matrix = []

for i in range(r):
    matrix_ele = list(map(int,input().split()))
    matrix.append(matrix_ele)
    
matrix = np.array(matrix)

print(np.mean(matrix,axis=1))
print(np.var(matrix,axis=0))
print(np.round(matrix.std(),decimals=11))
