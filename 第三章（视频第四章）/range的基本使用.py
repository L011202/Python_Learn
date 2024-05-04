"""
    range的三种语法
"""

# 语法一
num = 5
for i in range(5):          # range(5)是从0开始,但是不包括num
    print("%d " % i,end='')
print()

# 语法二
for x in range(0,5):        # range的范围为0 - 4 ,不包括后边的数字
    print(f"{x} ",end='')
print()

# 语法三
for y in range(0,11,2):     # range的范围为0 - 11 ,不包括后边的那个数字,步宽为2
    print(f"{y} ",end='')
