def iota(n):
    list_a = []
    for i in range (n+1):
        list_a = list(range(i))
    return list_a

n = int(input())
print(iota(n))