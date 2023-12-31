from random import randint
from datetime import datetime as dt


# changes for new branch

def get_random_array(length, int_range):
    arr = []
    for k in range(0, length - 1):
        arr.append(randint(0, int_range))
    return arr


def bubble_sort(array):
    """Функция сортировки пузырьковым методом."""
    start_time = dt.now()
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
    print('Сортировка пузырьковым алгоритмом заняла\t', dt.now() - start_time)
    return array


def select_sort(array):
    """Функция сортировки выбором."""
    sorted_array = []
    start_time = dt.now()

    while len(array) > 0:
        min_value = array[0]
        min_value_index = 0
        for j in range(0, len(array)):
            if array[j] < min_value:
                min_value = array[j]
                min_value_index = j
        sorted_array.append(array.pop(min_value_index))
    print('Сортировка выбором заняла\t\t\t\t\t', dt.now() - start_time)
    return sorted_array


def python_sort(array):
    """Функция сортировки sort(), встроенная в Python"""

    start_time = dt.now()
    array.sort()
    print('Сортировка встроенным методом sort() заняла\t', dt.now() - start_time)
    return array


def quick_sort(array):
    """Функция быстрой сортировки с рекурсией"""



    if len(array) <= 1:
        return array
    else:
        base_item = array[0]
        arr_less = [i for i in array[1:] if i <= base_item]
        arr_more = [i for i in array[1:] if i > base_item]
    return quick_sort(arr_less) + [base_item] + quick_sort(arr_more)



random_array_length = 200000
random_array_range = 1000000000000
print(F'Cоздается массив из {random_array_length} случайных чисел в диапазоне '
      F'от 0 до {random_array_range}')

# Создание списка с произвольными значениями int
random_array = get_random_array(random_array_length, random_array_range)

if random_array_length <= 10000:
    bubble_sort(random_array.copy())
else:
    print('Пузырьковым даже не буду заморачиаться сортировать')

if random_array_length <= 20000:
    select_sort(random_array.copy())
else:
    print('Сортровка выбором тоже очень долго')

sorted_arr = python_sort(random_array.copy())

start_time = dt.now()
sorted_arr = quick_sort(random_array.copy())
print('Сортировка quicksort заняла \t\t\t\t', dt.now() - start_time)

print(sorted_arr[:10], '.....', sorted_arr[-10:])
