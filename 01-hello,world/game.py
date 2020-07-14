print('---------an easy game-----------')

temp = input("有奖猜一个数字:\n")   #输入
guess = int(temp)

if guess == 8:  # 注意：缩进必须严格
    print("right")
    print("but I'm kidding，no rewards")
else:
    print("wrong")

print("游戏结束")