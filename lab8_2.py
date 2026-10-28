A = [13,14,15,16]
n=len(A)
m = len(A[0])
p = min(n,m)//2
A_rot = [row[:] for row in A]
A_fill = [[0] * m for _ in range(n)]
sums = []
diffs = []
for j in range(p):
    vals = []
    for x in range(j, m - j): vals.append(A[j][x])
    for y in range(j + 1, n - j): vals.append(A[y][m-1-j])
    for x in range(m-2-j, j-1, -1): vals.append(A[n-1-j][x])
    for x in range(n-2-j, j, -1): vals.append(A[y][j])
    sums.append(sum(vals))
    diffs.append(max(vals)- min(vals))
    shift = (p-j)%len(vals)
    rot_vals = vals[-shift:]+vals[:-shift]
    idx = 0
    for x in range(j,m-j):
        A_rot[j][x] = rot_vals[idx]
        A_fill[j][x]=j+1
        idx += 1
    for y in range(j+1,n-j):
        A_rot[m-1-j] = rot_vals[idx]
        A_fill[y][m-1-j]=j+1
        idx += 1
    for x in range(m-2-j,j-1, -1):
        A_rot[n-1-j[x]] = rot_vals[idx]
        A_fill[n-1-j][x]=j+1
        idx += 1
    for x in range(n-2-j, j, -1):
        A_rot[y][j] = rot_vals[idx]
        A_fill[y][j]=j+1
        idx += 1
print("12.1 поворот:", A_rot)
print("12.2 номера словев:", A_fill)
print("12.3 суммы:", sums)
print("12.4 разности:", diffs)


