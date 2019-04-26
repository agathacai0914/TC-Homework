def twosum(arr, a):
    for i in range(len(arr)):
        #print(i)
        for j in range(len(arr)):
            #print(j)
            if (arr[i]+arr[j] == a and i!=j):
                return (i,j)
                #print("test")
    return None

arr = [1,2,3]
a = 4
#print(len(arr))
print(twosum(arr, a))