from random import randint
from datetime import datetime


def bubble_sort(spisok):
    """Function Функция сортировки
    пузырьковым методом."""
    for i in range(0, len(spisok)-1):
        for j in range(0, len(spisok)-1):
            if spisok[j] > spisok[j+1]:
                temp = spisok[j+1]
                spisok[j+1] = spisok[j]
                spisok[j] = temp
    return spisok


N = 10
spis = []
for k in range(0, N-1):
    spis.append(randint(0, 100))

print(spis)
T1 = datetime.now()
sorted_spis = bubble_sort(spis)
print(datetime.now() - T1)