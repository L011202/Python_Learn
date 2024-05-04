name = "ZTBU"
Stock_Pirce = 19.99
Stocl_Code = "001234"
Stock_Day_Increase = 1.5
Growth_Day_Num = 7
print(f"公司名称{name},股票代码{Stocl_Code},当前股价{Stock_Pirce}")
# 控制小数点后的精度为2
print("每日增长系数为%.2f,经过%d天的增长后,股价达到了:%.2f" % (Stock_Day_Increase,Growth_Day_Num,(Stock_Pirce*(Stock_Day_Increase**Growth_Day_Num))))