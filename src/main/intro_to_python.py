import numpy as np
import pandas as pd

# 1
a = np.zeros((3, 3))

for i in range(3):
  for j in range(3):
    if i == j:
      a[i,j] = 1
      
print(f"{a}\n\n")

#2
for i in range(3):
  for j in range(3):
    if i != j:
      a[i,j] += 3
      
      
print(f"{a}\n\n")

#3
a = np.delete(a, 1, 1)

print(f"{a}")
