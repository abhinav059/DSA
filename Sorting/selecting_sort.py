#Naive solution
# arr = list(map(int, input().split()))
# arr = [10,4,7,9,4,2,15]
# temp = []
# n = len(arr)

# for i in range(n):
#     x = min(arr)
#     temp.append(x)
#     arr[arr.index(x)] = float("inf")

# print(temp)

# Optimized solution

arr = [10,4,7,9,3,5,2,15]
n = len(arr)
k = 0

for i in range(n):
    ind = i
    for j in range(i+1,n):
        if arr[j]<arr[ind]:
            ind = j
    arr[i], arr[ind] = arr[ind], arr[i]

print(arr)