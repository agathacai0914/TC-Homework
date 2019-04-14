def prime(a):
    if (a == 1):
        print("a is prime number.")
    else:
        for i in range(2, a):
            if (a % i == 0):
                print('a is not prime number')
                return()
            else:
                i = i + 1
        print('a is prime number.')


active = True

prompt = "请输入一个整数,如果输入0，则退出本程序"
while active:
    a = int(input("Please input a int number" + "\n"))

    if int(a) == 0:
        active = False
    else:
        prime(a)
    