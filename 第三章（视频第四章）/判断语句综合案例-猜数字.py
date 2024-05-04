import random
num = random.randint(1,10)
print(num)
guess_num = int(input("请输入猜的数字:"))
if guess_num == num:
    print("针不错,一次就猜对了")
else:
    if guess_num > num:
        print("你猜的数字比随机数大")
    else:
        print("你猜的数字比随机数小")
    guess_num = int(input("请输入你猜的数字:"))
    if guess_num == num:
        print("你真棒，第二次就猜对了!")
    else:
        if guess_num > num:
            print("你猜的数比随机数大")
        else:
            print("你猜的数比随机数小")
        guess_num = int(input("请你输入你猜的数字:"))
        if guess_num == num:
            print("猜对喽!")
        else:
            if guess_num > num:
                print("你猜的数比随机数大")
            else:
                print("你猜的数比随机数小")
