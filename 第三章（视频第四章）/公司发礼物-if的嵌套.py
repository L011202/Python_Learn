"""
    if elif else的嵌套使用
"""
print("欢迎来到日进斗金科技有限公司")
if int(input("请输入你的年龄:")) >= 18:
    if int(input("请在次确认你的年龄:")) <= 30:
        print("你的年龄符合领取年龄")
        if int(input("请输入的任职时间(年):")) >= 2:
            print("你可以领取奖品，去那边登记后领取就行了")
        else:
            if int(input("请输入你的工作级别(1-8):")) >= 3:
                print("你符合领取奖品的条件,请在那边进行登记,稍后会有人给你送到你的工位")
            else:
                print("你不符合领取奖品的条件,请你再接再厉")
    else:
        print("你的年龄超过了领取条件,你可以去二楼领取你们的保健品")
else:
    print("你的条件不符合,请再接再厉")