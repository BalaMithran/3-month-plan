# '''
# Three Number Sum

#  Problem Statement


# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# The function should nd all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets.
# The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with
# respect to the numbers they hold. If no three numbers sum up to the target sum, the function should return an empty array.

# Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0

# Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# O(n^2) time | O(n) space


def three_number_sum(array, targetSum):
    array.sort()
    ans_list = []
    for i in range(0, len(array)):
        lower = 0
        upper = len(array)-1
        while lower < upper:
            sum = array[lower] + array[upper] + array[i]
            if sum == targetSum:
                ans_list.append([array[upper], array[lower]])
            elif sum > targetSum:
                upper -= 1
            else:
                lower += 1
    return ans_list


sample_input_array = [12, 3, 1, 2, -6, 5, -8, 6]
sample_sum = 0
result = three_number_sum(sample_input_array, sample_sum)
print(result)
