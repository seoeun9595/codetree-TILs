num1, num2 = map(int, input().split())
num = 1
for i in range(num1):
    for j in range(num2):
        print(num, end = ' ')
        num += 1
    print()