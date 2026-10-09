n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
count_rem_3 = 0
max_abs_rem_3 = None
sum_rem_5 = 0
for num in numbers:
    if num % 7 == 3:
        count_rem_3 += 1
        if max_abs_rem_3 is None or abs(num) > abs(max_abs_rem_3):
            max_abs_rem_3 = num
    elif num%7 ==5:
        sum_rem_5 += num
print(count-rem_3)
if max_abs_rem_3 is not None:
    print(max_abs_rem_3)
else:
    print(0)
print(sum_rem_5)
