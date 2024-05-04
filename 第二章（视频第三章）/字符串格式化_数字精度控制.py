class_num = 2002
Student_ID = 200501230253
avr_money = 1100.99
# 多个变量占位，变量要用括号括起来，并按照占位的顺序填入

# 将输入的int型数据转为str再拼接
message = "我的本科专业是物联网工程，班级是物联网工程本科%s班,我的学号是%s,每个月的生活费大概%s" % (class_num, Student_ID,avr_money)
print("进行转换转换拼接")
print(message + "\n")

# 不转换类型，直接拼接
print("不进行转换拼接")
message1 = "我的本科专业是物联网工程，班级是物联网工程本科%d班,我的学号是%d,每个月的生活费大概%f" % (class_num, Student_ID,avr_money)
print(message1)