"""
    ATM模拟
"""
money = 5000000
# name = input("尊敬的客户,请输入你的名字:>")
name = None
def menu():
    """
    操作菜单
    :return:   None
    """
    print("[1]  查询余额\t")
    print("[2]  存   款\t")
    print("[3]  取   款\t")
    return None
def put1():             # 查询余额函数
    """
    全局变量money
    :return: None
    """
    global money
    print(f"尊敬的{name},你的银行卡余额为:{money}")            # 输出信息
    # menu()                                                 # 返回菜单
def put2():             # 存款操作
    global money
    money += int(input("请输入你要存款的金额:>"))             # 输入要存的数额，并加到money中
    print("尊贵的%s,您已存款成功,你的账户余额为:%d" % (name,money))       # 输出提示
    # menu()                                                # 返回菜单
    return None
def put3():
    """
    取款操作
    :return:None
    """
    global money
    money -= int(input("请输入你要取款的金额:>"))           # 输入取款的金额，并在money中减去取的金额
    print("尊敬的%s,您已成功取款,你的账户余额为%d" % (name,money))          # 输出提示信息
    return None    # 返回None的话return可以省略

"""
    函数入口
"""
name = input("尊敬的客户,请输入你的名字:>")       # 客户首先输入名字登记
# menu()                                       # 显示菜单
"""
    判断输入的数字,
"""
num = 1
while num:
    num_option = int(input("请选择操作!\n"))
    if num_option == 1:
        put1()
        menu()
        continue
    elif num_option == 2:
        put2()
        menu()
        continue
    elif num_option == 3:
        put3()
        menu()
        continue
    else:
        break




