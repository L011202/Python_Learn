"""
    布尔类型的定义
    比较运算符的运用
    @author:liang
    time:2024年4月12日 21点02分
"""
# 定义变量来存储布尔类型的数据
bool1 = True
bool2 = False
print(f"bool1的内容是{True},bool1的类型是{type(bool1)}")
print("bool2的内容是%s,bool2的类型是%s" % (False,type(bool2)))

# 比较运算符的运用
# ==,!=,>,<,>=,<=

# ==
a = 5
b = 6
c = (a == b)
print(a,b,c)

# !=
d = 10086
e = 10010
f = (d != e)
print("d的值为%d,e的值为%d,f为%s" % (d,e,f))

# >
g = 521
h = 520
i = (g > h)
print(f"g的值为{g},h的值为{h},i为{i},i的类型是{type(i)},i的数值为{int(i)}")

# <
j = (g < h)
print("g的值为%d.h的值为%d，j为%s，j的类型为%s,j的数值大小为%d" % (g,h,j,type(j),(int(j))))

# >=
k = 20011202
l = 20000101
m = (k >= l)
print(k,l,m,type(m),(int(m)))

# <=
n = (k <= l)
print(k,l,type(n))