"""
    9*9乘法表   for循环嵌套
"""
i = 0
j = 0
for i in range(1,10):
    for j in range(1, i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()
