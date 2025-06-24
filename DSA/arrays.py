



# def twoSum(arr, target):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == target:
#                 return [i, j]
#     return []
# arr = [2 ,9, 7, 5]
# target = 12
# print(twoSum(arr, target))


#question 2



# def twosum(arr, target):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] + arr[j] == target:
#                 return[i, j]
#     return[]
# arr = [1,3,4,7,8]
# target = 7
# print(twosum(arr, target))


#question 3

def twosum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return[i, j]
    return[]
arr = [2, 4, 7, 9, 10]
target = 19
print(twosum(arr, target))