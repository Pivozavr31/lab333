n = int(input("введи кол-во чисел N: "))
arr = []
print("Введи элементы массива: ")
for i in range(n):
    arr.append(float(input(f"Элемент {i+1}: ")))
d = float(input("Введи число d: "))
found_count = 0
for i in range(n):
    sum_left = sum(arr[:i])
    sum_right = sum(arr[i + 1 :])
    if abs(sum_left - sum_right)<=d:
        found_count += 1
print(f"Кол-во элементов в массиве: {found_count}")
