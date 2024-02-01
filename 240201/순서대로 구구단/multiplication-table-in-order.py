num1, num2 = map(int, input().split())

if num1 <= num2:
    for i in range(1, 10):
        for j in range(num1, num2+1):
            print(f"{j} * {i} = {j*i}", end = '  ')
        print("")
else:
    for i in range(1, 10):
        for j in range(num1, num2-1, -1):
            print(f"{j} * {i} = {j*i}", end = '  ')
        print("")