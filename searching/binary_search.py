arr = [1, 3, 5, 6, 7, 9, 11, 13, 14, 17, 20,
       22, 30, 34, 56, 61, 62, 63, 64, 66, 80, 90]


def binarysearch(arr, val):
    low = 0
    high = len(arr)-1
    mid = (len(arr)-1)//2

    while low <= high:
        mid = (low + high)//2

        if arr[mid] < val:
            low = mid+1
        elif arr[mid] > val:
            high = mid-1

        else:
            return "found "
    return "not found"


print(binarysearch(arr, 26))
print(binarysearch(arr, 56))
print(binarysearch(arr, 80))
