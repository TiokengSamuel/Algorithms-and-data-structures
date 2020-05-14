# Binary search Algorithm
# where, arr and x is the array and the value searched for succesfully

def BinarySearch(arr, x, firstNum, lastNum):
    while firstNum <= lastNum:
        mid = firstNum + (lastNum - 1) // 2
        # check if x is present in the middle
        if arr[mid] == x:
            return mid
        # check if it is greater and ignore the left half
        elif arr[mid] < x:
            firstNum = mid + 1

        # check if it is smaller and ignore the right half
        else:
            lastNum = mid - 1

    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Driver code
result = BinarySearch(arr, x, 0, len(arr) - 1)

if result != -1:
    print("Element is present at index", result + 1)

else:
    print("Element is not in the array!")
