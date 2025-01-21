import random
import timeit

print(" Програма для демонстрації часу роботи сортування різними методами" "\n" "Генеруємо випадковий список чисел" )
start = int(input("Ведіть початкове число для генерації: "))
end = int(input("Ведіть кінцеве число для генерації: "))
size = int(input("Ведіть кількість елементів у списку: "))

# Функція сортування вставками

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

# Функція сортування злиттям
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def generate_list (size, start, end):
     return random.choices(range(start, end), k=size)

test_list = generate_list(size, start, end)

time_taken = timeit.timeit(stmt=lambda: insertion_sort(test_list.copy()), number=1)
time_taken_merged = timeit.timeit(stmt=lambda: merge_sort(test_list.copy()), number=1)
timsort_time = timeit.timeit(lambda: sorted(test_list.copy()), number=1)

print(f"Сортування списку вставками із {size} елементів зайняло {time_taken:.4f} секунд.")
print(f"Сортування списку злиттям із {size} елементів зайняло {time_taken_merged:.4f} секунд.")
print(f"Сортування списку Timsort із {size} елементів зайняло {timsort_time:.4f} секунд.")
