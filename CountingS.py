def counting_sort(arr):
    minimum, maximum = min(arr), max(arr)
    size = maximum - minimum + 1
    b = [0] * size
    for i in range(len(arr)):
        b[arr[i] - minimum] += 1
    k = 0
    for i in range(size):
        while b[i] > 0:
            arr[k] = i + minimum
            k += 1
            b[i] -= 1
