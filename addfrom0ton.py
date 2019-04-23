def sum_n(n):
    sum = 0
    for a in range (n+1):
        sum += a
    return sum

n = int(input())
print(sum_n(n))