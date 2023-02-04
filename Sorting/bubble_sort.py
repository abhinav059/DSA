
arr = list(map(int, input().split()))

n = len(arr)-1

for i in range(n):
    for j in range(n):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

