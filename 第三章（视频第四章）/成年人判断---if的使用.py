print("欢迎来到游乐场，儿童免费，成人收费")
"""
    语句优化
    print(f"请输入你的年龄:")
    age = input()
"""
age = int(input("请输入你的年龄:"))
# int(age)
if age >= 18:
    print("您已经成年，游玩需补票10元")
print(f"祝您玩的愉快")