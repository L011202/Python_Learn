"""
    通过input语句获取键盘输入的身高
    判断是否超过120cm,并通过print给出提示信息
"""
str1 = "^^欢迎来到动物园^^"
str2 = "**您的身高已经超过120cm,游玩需要进行买票，票价为10元**"
str3 = "**您的身高没有超过120cm,游玩不需要买票，祝您游玩愉快**"
str4 = "--祝您玩的愉快--"
print(str1)
highth = int(input("请输入你的身高(cm):"))         # int类型转换
if highth >= 120:
    print(str2)
else:
    print(str3)
print(str4)