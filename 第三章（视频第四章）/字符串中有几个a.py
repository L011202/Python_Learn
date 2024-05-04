"""
    使用for循环来输出字符串，并判断有几个a
"""
str1 = "We briefly staggered, and the tide ebbed at the end, paying tribute to this meeting."   # 字符串初始化
# “我们短暂交错，尾声潮落，致敬这场遇见”
count = 0                                # a数量统计变量
for x in str1:                           # for循环
    if x == 'a':                         # 判断字符是否和a相等
        count += 1                       # a的数量加1
    print("%s" % x,end='')               # 输出字符串，并且不换行
print(f"字符串中有{count}个a")             # 输出后边的文本文字

