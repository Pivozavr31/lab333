num =  [100,85,60,42,42,15,3]
is_descending = all(num[i] >= num[i+1] for i in range(len(num) - 1))
is_strictly_descendind = all(num[i] > num[i+1] for i in range(len(num) - 1))
print(num)
print(is_descending)
print(is_strictly_descendind)
