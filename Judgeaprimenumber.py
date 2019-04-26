def is_prime(n):
    if (n == 1):
        print("False")
    elif (n == 2):
        print("True")
    else:
        for i in range(2, n):
            if (n % i == 0):
                print('False')
                return()
            else:
                i = i + 1
        print('True')


n = int(input())

is_prime(n)