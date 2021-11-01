
# Monotonic_Array

# #### Problem Statement

# Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
# An array is said to be monotonic if its elements,from left to right, are entirely non-increasing or entirely non-decreasing.

# Sample Input : [-1,-5,-10,-1100,-1100,-1101,-1102,-9001] # if prevN <= currN <= nextN or prevN >= currN >= nextN

# Sample Output : true

def isMonotonic(array):
    state = array[0] <= array[1]
    for i in range(0, len(array)-2):
        if state == (array[i] <= array[i+1]):
            # print(array[i], array[i+1])
            # print("same")
            pass
        else:
            return False
    return True


print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
print(isMonotonic([1, 3, 5, 7, 9, 9, 11, 14, 17, 33]))
