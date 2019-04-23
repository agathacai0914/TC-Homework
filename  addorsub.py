def add_or_sub(op, a, b):
    sum = 0
    if(op == '+'):
        sum = a+b
    elif(op == '-'):
        sum = a-b
    return sum

op = input()
a = int(input())
b = int(input())

print(add_or_sub(op, a, b))