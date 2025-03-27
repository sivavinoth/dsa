
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):

            while arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# Test it
arr = [5, 3, 8, 4, 2]
print(bubble_sort(arr))  


v =1323
sv = str(v)
stv = "".join(sorted(sv))
c = int(stv)
print(c)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test it
arr = [5, 3, 8, 4, 2]
print(bubble_sort(arr))  # Output: [2, 3, 4, 5, 8]

