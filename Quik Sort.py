def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # if the current value we're looking at is larger than the pivot
        # it's in the right place(right side of pivot) and we have to move left

        while low <= high and array[high] >= pivot:
            high = high - 1

            # Opposite procces of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]

        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


# Implementing the quik sort function
def quickSort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quickSort(array, start, p - 1)
    quickSort(array, p + 1, end)


# driver code

array = [29, 99, 27, 41, 56, 89, 45, 9, 21, 2, 1, 98, 34, 59, 90]
quickSort(array, 0, len(array) - 1)
print(array)
