"""
    range的使用，看range范围里有几个偶数
"""
count = 0
for i in range(1,100):          # 1-99
    if i%2 == 0:
        count += 1              # 偶数个数+1
print("1到100(不包含100本身)范围内,有%d个偶数" % count)