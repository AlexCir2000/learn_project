from random import randint
from datetime import datetime as dt


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
    print('Сортировка пузырьковым алгоритмом заняла', dt.now() - start_time)
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
    print('Сортировка выбором заняла', dt.now() - start_time)
    return sorted_array


random_array_length = 1000
random_array_range = 1000
print(F'Cоздается массив из {random_array_length} случайных чисел в диапазоне '
      F'от 0 до {random_array_range}')
random_array = get_random_array(random_array_length, random_array_range)
sorted_arr = bubble_sort(random_array)
print(sorted_arr[:10], '.....', sorted_arr[-10:])
random_array = get_random_array(random_array_length, random_array_range)
sorted_arr = select_sort(random_array)
print(sorted_arr[:10], '.....', sorted_arr[-10:])
