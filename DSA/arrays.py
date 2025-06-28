



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

# def twosum(arr, target):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] + arr[j] == target:
#                 return[i, j]
#     return[]
# arr = [2, 4, 7, 9, 10]
# target = 19
# print(twosum(arr, target))











#question 4

def twosum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return[i, j]
    return[]
arr = [7, 9, 0, 7 ,6]
target = 16
print(twosum(arr, target))

arr = [1, 2, 3, 4, 5]
total = 0


for num in arr:
    total += num

print("The sum of the array elements is:", total)
