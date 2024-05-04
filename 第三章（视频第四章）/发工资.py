"""
    发工资
    员工编号1-20,从编号1开始,依次领取工资,每人可领取1000元
    领取工资时,财务判断员工的绩效分(1-10)（随机生成）,若低于5，不发工资，下一位
    若工资发完了,结束发工资
"""
import random
money = 10000                           # 工资总数
count = 0                               # 发放员工数量统计
for i_worker in range(1,21):            # for循环体
    num = random.randint(1,10)          # 绩效分数生成
    if num < 5:                        # 绩效判断
        print("员工%d,绩效分%d,低于5,不发工资,下一位" % (i_worker,num,))          # 输出不符合提示
        continue                        # 通过continue跳过下面的循环
    else:
        count += 1                      # 可领取工资数量+1
        if money == 0:                  # 如果工资余额为0,则直接跳出循环
            print("工资发完了,下个月领取吧")           # 输出提示
            break                                  # 跳出循环
        print(f"向员工{i_worker},发放工资{1000}元,账户余额还剩余{money-1000}")             # 输出提示
        money -= 1000                                         # 工资总数-1000
def  my_len(date):
    count = 0
    for i in date:
        count += 1
    print(count)

str = "abcdefg"
my_len(str)