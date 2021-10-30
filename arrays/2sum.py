input_array = [3, 5, -4, 8, 11, 1, -1, 6]
sum = 10


def twosum(input_array, sum):
    for i in range(0, len(input_array)):
        for j in range(i+1, len(input_array)):
            if input_array[i] + input_array[j] == sum:
                return [input_array[i], input_array[j]]
    return -1


def twosumoptimized(input_array, sum):
    input_array.sort()
    lower = 0
    upper = len(input_array)-1
    while lower < upper:
        summ = input_array[lower] + input_array[upper]
        if summ == sum:
            return [input_array[upper]], input_array[lower]
        elif summ > sum:
            upper -= 1
        else:
            lower += 1
    return -1


print(twosum(input_array, sum))
print(twosumoptimized(input_array, sum))
