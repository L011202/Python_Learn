"""
    猜数字,直到猜出来为止
"""
import random                   # 导入random包
num = random.randint(1,100)     # 生成随机刷,范围1-100
# print(num)
i = 1                           # 次数,次数要从1开始
guess_num = int(input("请输入你要猜的数:"))             # 第一次输入
while guess_num != num:                            # 如果猜的数和则个随机数不相等，则进入循环,反之跳出
    if guess_num > num:                            # 如果猜的数比这个随机数大
        print("你猜的数比这个随机数大")
    else:                                          # 如果猜的数比这个随机数小
        print("你猜的数比这个随机数小")
    guess_num = int(input("请输入你要猜的数:"))       # 再次输入猜的数
    i += 1                                         # 猜一次，次数+1
print(f"你猜了{i}次")                               # 使用格式化输出进行次数输出
