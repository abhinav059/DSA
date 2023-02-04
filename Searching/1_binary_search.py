# def b_search(arr,n,x): #arr = list(array), n = len(arr), x = element to search.
#     low = 0, high = n-1
#     while (low<=high):
#         mid = (low+high)//2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             high = mid-1
#         else:
#             low = mid+1
#     return -1


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

start = 0
end = len(grid)

while start<end:
    mid = start - (end - start)//2
    if grid[mid]<0:
        end = mid
    else:
        s