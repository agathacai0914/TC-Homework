def cummulative_sum(arr):
    arr2 = []
    sum = 0
    for i in range(len(arr)):
        sum = sum+arr[i]
        arr2.append(sum)
    return arr2

n = int(input())

arr=[]  #determine the input array
for i in range(n):
    arr.append(int(input()))

print(cummulative_sum(arr))
