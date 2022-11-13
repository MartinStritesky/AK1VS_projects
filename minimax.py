# Minimax
from random import randint
import timeit
import sys

def Bubblesort(pole):
    t0 = timeit.default_timer()
    for j in range(len(pole) - 1):
        for i in range(len(pole) - j - 1):
             if pole[i] > pole[i + 1]:
                pole[i], pole[i + 1] = pole[i + 1], pole[i]
    print(pole)
    t1 = timeit.default_timer()
    print(f'The time needed to sort is {t1 - t0} seconds.')
    return pole


def InsertionSort(pole):
    t0 = timeit.default_timer()
    for i in range(1, len(pole)):
        key_item = pole[i]
        j = i - 1
        while j >= 0 and pole[j] > key_item:
            pole[j + 1] = pole[j]
            j -= 1
        pole[j + 1] = key_item
    print(pole)
    t1 = timeit.default_timer()
    print(f'The time needed to sort is {t1 - t0} seconds.')
    return pole


def QuickSort(pole):
    if len(pole) < 2:
        return pole
    low, same, high = [], [], []
    pivot = pole[randint(0, len(pole)-1)]
    for item in pole:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return QuickSort(low) + same + QuickSort(high)


vstup = sys.argv
vstup.remove('minimax.py')
pole = []

if vstup == []:
    for i in range(20):
        pole.append(randint(0, 100000))
elif vstup != [] and sys.argv[0].endswith(".txt"):
    with open(sys.argv[0]) as f:
        text = f.readline()
        pole = list(map(int, text.split(",")))
else:
    pole = list(map(int, vstup))

min = pole[0]
max = pole[0]
min_pos = 0
max_pos = 0

for i in range(len(pole)):
    if pole[i] > max:
        max = pole[i]
        max_pos = i
    if pole[i] < min:
        min = pole[i]
        min_pos = i

print(f'The maximum item is {max} at place number {max_pos} and the minimum item is {min} at place number {min_pos}.')

has_chosen = False
while has_chosen == False:
    method = input("Please choose your sorting method: (B)ubbleSort, (I)nsertionSort or (Q)uickSort? ")

    if method == 'I':
        InsertionSort(pole)
        has_chosen = True

    elif method == 'Q':
        t0 = timeit.default_timer()
        print(QuickSort(pole))
        has_chosen = True
        t1 = timeit.default_timer()
        print(f'The time needed to sort is {t1 - t0} seconds.')

    elif method == 'B':
        Bubblesort(pole)
        has_chosen = True

    else:
        method = input("Please choose correctly!")