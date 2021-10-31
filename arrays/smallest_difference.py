# Smallest Difference
# #### Problem Statement
# Write a function that takes in two non-empty arrays of integers. The function should nd the pair of numbers(one from the rst array, one from the second array)
# whose absolute difference is closest to zero. The function should return an array containing these two numbers, with the number from the rst array in the rst
# position. Assume that there will only be one pair of numbers with the smallest difference.
# Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
# Sample output: [28, 26]
# #### Explanation
# To traverse in array use left and right pointer to traverse
# We can use a Stack here
# '''


def smallestDifference(arrayOne, arrayTwo):
    minsofar = float("inf")
    solarray = []
    arrayOne.sort()
    arrayTwo.sort()
    l1 = len(arrayOne)
    l2 = len(arrayTwo)
    p1, p2 = 0, 0
    while p1 < l1 and p2 < l2:
        firstarrayelement = arrayOne[p1]
        secondarrayelement = arrayTwo[p2]
        if abs(firstarrayelement - secondarrayelement) < minsofar:
            minsofar = abs(firstarrayelement - secondarrayelement)
            solarray = [firstarrayelement, secondarrayelement]
        if firstarrayelement < secondarrayelement:
            p1 += 1
        else:
            p2 += 1
    return solarray


array_one = [-1, 5, 10, 20, 24, 31, 54, 45,
             6, 43, 44, 245, 67, 88, 43, 56, 28, 3]
array_two = [26, 134, 135, 15, 17]
print(smallestDifference(array_one, array_two))
