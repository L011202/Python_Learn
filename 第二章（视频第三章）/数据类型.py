# 方式一 ：使用print直接输出类型信息

print(type("好好学习，不负好时光"))
print(type(6666))
print(type(3.14))

print("------------------")
print("    输出分隔符      ")
print("------------------\n\n")

# 方式二 : 使用变量存储type()语句的结果

string_type = type("好好学习，不负青春年华")
int_type = type(66666)
float_type = type(3.14)

""""
    使用print输出结果
"""
print(string_type)
print(int_type)
print(float_type)

print("------------------")
print("    输出分隔符      ")
print("------------------\n\n")

# 方式三: 使用typr()语句，查看变量中存储的数据类型信息


# 给变量赋值
name = "好好学习，不负人间一遭"
name_type = type(name)

# 输出
print(name_type)

