def fibonacci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(13))
