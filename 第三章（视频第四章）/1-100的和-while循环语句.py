"""
    使用while循环来求1-100的和
    liang
    2024年4月21日 22点44分
"""
i = 1               # 定义变化量,并赋初始值为1
Sum_i = 0           # 定义和变量,并初始化为0
while i <= 100:     # 判断条件
    Sum_i += i      # Sum_i += i  >>>>>   Sum_i = Sum_i + i
    i += 1          # i += 1      >>>>>   i = i+1
print(Sum_i)        # 输出最后计算的数值

