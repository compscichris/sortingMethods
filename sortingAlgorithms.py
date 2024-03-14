# Author: compscichris
# Date: 2/20/2024
# sortingAlgorithms.py is a python file made to help review and refresh memory on sorting algorithm runtimes,
# and to help practice python.
import math
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

array = [-4, 29, 3, 45, 7, -34]

#Selection sort
'''
Selection sort is a sorting algorithm that repeatedly selects the smallest element from the unsorted portion of the 
list. 
TIME COMPLEXITY: o(N^2), theta(N^2), O(N^2)
SPACE COMPLEXITY: O(N)
The algorithm runs O(N), because its nature targets the first slot of the array, and proceeds with the next slot, until 
'''
def selectionSort(array):
    size = len(array)
    if size <= 1:
        print("Size too small for sorting.")
    else:
        for i in range(0, size):
            min = math.inf
            minInd = -1
            for j in range(i, size):
                if min > array[j]:
                    min = array[j]
                    minInd = j
            if minInd != i:
                array[minInd] = array[i]
                array[i] = min
print("SELECTION SORT:")
print("INPUT:",array)
selectionSort(array)
print("OUTPUT:",array)

array2 = [11, 12, 13, 5, 6]
#Insertion sort
def insertionSort(array):
    size = len(array)
    if size <= 1:
        print("Size too small for sorting.")
    else:
        for i in range(1,size):
            swap = True
            j = i - 1
            while (swap and j >= 0):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                    j -= 1
                else:
                    swap = False

print("INSERTION SORT:")
print("INPUT:",array2)
insertionSort(array2)
print("OUTPUT:",array2)

def insertionSortEfficient(array):
    size = len(array)
    if size <= 1:
        print("Size too small for sorting.")
    else:
        for i in range(1,size):
            swap = True
            target = array[i]
            j = i - 1
            while (j >= 0 and array[j] > target):
                array[j+1] = array[j]
                j -= 1
            array[j+1] = target

#insertionSortEfficient(array2)
#print(array2)

'''
Merge Sort is a sorting algorithm that uses divide and conquer to sort an array. 
RUNTIME: o(N*logN), theta(N*logN), O(N*logN)
Recurrence Relation proof: T(N) = 2T(N/2) + N 
For every run of the recursion we split and create 2 subproblems of N elements,
then merge N elements together. 
'''
def mergeSort(array, beg, end):
    eCount = end - beg
    copy = [0] * eCount
    midpoint = beg + eCount//2
    if eCount < 2:
        copy[0] = array[beg]
        return copy
    left = mergeSort(array, beg, midpoint)
    right = mergeSort(array, midpoint, end)
    i = 0;
    j = 0;
    k = 0;

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            copy[k] = left[i]
            i += 1
        else:
            copy[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        copy[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        copy[k] = right[j]
        j += 1
        k += 1
    return copy


array3 = [12, 11, 13, 5, 6, 7, -1, 29, 40, -20]
print("MERGE SORT:")
print("INPUT:",array3)
end = len(array3)
list = mergeSort(array3, 0, end)
print("OUTPUT:",list)




array4 = [6,3,0,5,-12,500,90]
def bubbleSort(array):
    size = len(array)
    for i in range(size, 0, -1):
        for j in range(1, i):
            if array[j-1] > array[j]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                #STEP BY STEP
                #print(array)

print("BUBBLE SORT:")
print("INPUT:",array4)
bubbleSort(array4)
print("OUTPUT:",array4)

#Optimized verion from https://www.geeksforgeeks.org/bubble-sort/
def bubbleSortOptimized(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if (swapped == False):
            break


'''# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")'''
