# Python program for bubble sort

def bubbleSort(arr):
    n = len(arr)

    # Traverse the array 1 by 1
    for i in range(n):
        for j in range(0, n - i - 1):

            # Swaping element from 0 to n-i-1 if the element found is greater
            # than the other
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)

print("Sorted array: ")
for i in range(len(arr)):
    print("%d" % arr[i])
