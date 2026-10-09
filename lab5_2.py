n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
count=0
total_sum=0
seen=set()
for num in numbers:
    if -num in seen:
        count +=1
        total_sum += num
    seen.add(num)
print(count)
print(total_sum)
