def arr_min(arr):
    min = arr[0]
    for i in range (len(arr)):
        if (arr[i]>min):
            min = min
        else:
            min = arr[i]
    print(min)
    return min

n = int(input())     #determine the length of the array

arr=[]
for i in range(n):
    arr.append(int(input()))

arr_min(arr)