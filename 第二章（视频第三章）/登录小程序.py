"""
    定义两个变量,用以获取从键盘输入的内容，并给出提示信息
    变量1:变量名:user_name,记录用户名
    变量2:变量名:user_type,记录用户类型
"""

user_name = input()
user_type = input()
# 打印方式1
# print(f"你好,{user_name},你是尊贵的{user_type}用户,欢迎光临")

# 打印方式2
print("你好,%s,你是尊贵的%s用户,欢迎光临" % (user_name,user_type))