work_money = int(input("请输入你的工资:"))
str1 = "你的工资已经足够你生活了，继续保持，但是仍要努力拼哦"
str2 = "你的工资还不足够你的日常花销以及养活你的未来,请继续加油,不要灰心丧气哦,要每天都有活力哦"
if work_money >= 10000:
    print(str1+f"\nwork_money:{work_money}" )
else:
    print(str2+"\nwork_money:%d" % work_money)
print("要充满活力，要斗志昂扬")