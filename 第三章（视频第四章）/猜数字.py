import random       # 导入random函数包
number = random.randint(1,50)           # 随机生成一个随机数，范围在1-50
# print("输入1进行积分查询")
score = 0
# print(number)
if int(input("请输入你第一次猜的数字:")) == number:
    print("恭喜您，一次就猜对喽!")
    score += 3
    i = int(input("输入1进行积分查询\n"))
elif int(input("请输入你第二次猜的数字:")) == number:
    print("祝贺你，在第二次就猜对了")
    score += 2
    i = int(input("输入1进行积分查询\n"))
elif int(input("请输入你第三次猜的数字:")) == number:
    print("你真厉害，居然猜对了")
    score += 1
    i = int(input("输入1进行积分查询\n"))
else:
    print("非常遗憾。三次机会已经用完了，你没有猜对，请再接再厉")
    score += 0
    i = int(input("输入1进行积分查询\n"))
if i == 1:
    print("你的积分为:%d" % score)
