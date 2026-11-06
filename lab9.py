def max(arr):
    if not arr:
        return 0
    m = 0
    for x in arr:
        y = arr.count(x)
        if y > m:
            m = y
    return m
j = [3,-1,-1,-1,2,3,-1,3,-1,2,4,9,3]
print(max(j))
