"""
    if elif else的嵌套使用
"""
print("欢迎来到勇往直前网咖")
age = int(input("请出示你的身份证，并说出你的年龄:"))
if age >= 18:
    print("欢迎光临")
    VIP_Level = int(input("请输入你的VIP等级:"))
    if VIP_Level >= 3:
        print("你是我们店的贵宾,你的消费会有8折的优惠，并且送您一瓶现磨咖啡")
    elif VIP_Level < 3:
        print("你是我们店的黄金会员,你可以在这些饮料中任选其一，稍后我们将会送到你的位子上")
    else:
        print("你是我们店的普通会员，祝你游戏连胜")
else:
    print("你是未成年,你不能上网,要好好学习")