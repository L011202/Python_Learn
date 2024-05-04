"""
    if elif  else 多条件判断语句的使用
"""
# 代码复杂版
# height = int(input("请输入你的身高(cm):"))
# Vip_Level =  int(input("请输入你的Vip等级(1-5):"))
# if height < 120:
#     print("你的身高在免费范围，不需要支付票价")
# elif Vip_Level > 3:
#     print("Vip等级大于3，你可以免费畅玩")
# else:
#     print("您不满足任何免费条件，请支付票价，票价10元，微信、支付宝店铺可以支付")
# 代码简洁版
if int(input("请输入你的身高:")) < 120:
    print("你的身高在免费范围内,不用支付门票,祝您游戏愉快")
elif int(input("请输入你的Vip等级:")) > 3:
    print("您是我们的高级VIP客户,你可以免费畅玩!")
else:
    print("抱歉,你不满足免费条件,需要购买门票,微信支付宝都可以进行支付")

