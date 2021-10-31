
# # Move_Element_To_End

# ## Problem Statement

# You are given an array of integers and an integer.Write a function that moves all instances of the integer in the array to the end
# of the array and returns the array.
# The function should perform this in place(i.e it should mutate the input array ) and dosen't need to maintain the order of the other
# integers

# Sample Input : array[2,1,2,2,2,3,4,2]
# 			   toMove =2
# Sample Output : [1,3,4,2,2,2,2,2] # 1,3,4 can be ordered differently

# def moveElementToEnd(array, toMove):

#     while start <= end:
#         if array[start] == toMove :
#             array[start] , array[end] = array[end] , array[start]
#             end-=1
#     return array

def t(array, toMove):
    start, end = 0, len(array)-1
    while start <= end:
        if array[start] == toMove:
            array[start], array[end] = array[end], array[start]
            end -= 1
        else:
            start += 1
    return array


print(t([2, 1, 2, 2, 2, 3, 4, 2], 2))
