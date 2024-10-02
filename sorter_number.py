'''
Sorter (сортировка):

1) bubble_sort
2) selection_sort
3.1) insertion_sort_1
3.2) insertion_sort_2
4) merge_sort
5) quick_sort
'''



''' [1. Creating an array of 9 unique digits in random order]: '''
# импорт модуля "random"
import random

def random_array():
    # пустой массив
    array = []
    
    # цикл работает пока длина массива меньше 9.
    while len(array) < 9:
        # генерируется случайной число от 1 до 9
        run = random.randint(1, 9)
        
        # если число не в массива, то:
        if run not in array:
            # оно добавляется в массив
            array.append(run)
    
    return array

# print(f'{random_array()}')  # вывод: массив из 9 уникальных цифр в случайном порядке



''' [2. Sorting]: '''

array = random_array()

''' (bubble): '''
def bubble_sort(arr):
    n = len(array)

    for run in range(n-1):
        for i in range(n-1-run):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return arr


''' (selection): '''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        index = i
        for j in range(i+1, n):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr


''' (insertion): '''
def insertion_sort_1(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def insertion_sort_2(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_element
    return arr


''' (merge): '''
def merge_sort(arr):
    def merge_sort_recursive(arr):
        if len(arr) >= 1:
            return arr
        
        mid = len(arr) // 2
        
        left = arr[:mid]
        right = arr[mid:]
        
        left = merge_sort_recursive(left)
        right = merge_sort_recursive(right)
        
        return merge(left, right)
    
    def merge(left, right):
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        while i < len(left):
            merged.append(left[i])
            i += 1
        
        while j < len(left):
            merged.append(right[j])
            j += 1
        
        return merged
    
    return merge_sort_recursive(arr)


''' (quick): '''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []

    for el in arr[1:]:
        if el < pivot:
            left.append(el)
        else:
            right.append(el)
    
    return quick_sort(left) + [pivot] + quick_sort(right)



# print(f'\narray: {random_array()}\n')
# print(f'bubble_sorter: {bubble_sort(arr=array)}')
# print(f'selection_sort: {selection_sort(array)}')
# print(f'insertion_sort_1: {insertion_sort_1(array)}')
# print(f'insertion_sort_2: {insertion_sort_2(array)}')
# print(f'merge_sort: {merge_sort(array)}')
# print(f'quick_sort: {quick_sort(array)}')





''' Мой первый сортировщик:
https://www.youtube.com/shorts/fGZktXucbNY
https://www.youtube.com/watch?v=WBaL7ANQbzQ
'''
# def bubble_sorter(arr):
#     n = len(array)
#     counter = 0

#     for run in range(n-1):  # ...
#         for i in range(n-1-run):  # дополнительно ставится "-run" для того, чтобы не сравнивать с числами которые уже встали на свои места
#             # print(f'comparison: if {array[i]} > {array[i+1]}')
#             if array[i] > array[i+1]:  # если левый элемент больше правого, то:  (можно поменять знак и будет обратная сортировка...)
#                 counter += 1  # счётчик +1
#                 # print(f'{array} {array[i]} <-> {array[i+1]}')  # ...
#                 array[i], array[i+1] = array[i+1], array[i]  # смена местами

#     print(f'{array} Было произведено ходов: {counter}')

# bubble_sorter(arr=array)