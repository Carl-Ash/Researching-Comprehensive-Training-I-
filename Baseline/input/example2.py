import random

def guess_number():
    # 生成1-100之间的随机数
    number = random.randint(1, 100)
    attempts = 0
    
    print("欢迎来到猜数字游戏！")
    print("我已经想了一个1到100之间的数字，来猜猜看吧！")
    
    while True:
        try:
            guess = int(input("请输入你猜的数字："))
            attempts += 1
            
            if guess < number:
                print("太小了！再试一次。")
            elif guess > number:
                print("太大了！再试一次。")
            else:
                print(f"恭喜你！猜对了！")
                print(f"你一共猜了{attempts}次。")
                break
                
        except ValueError:
            print("请输入有效的数字！")

# 运行游戏
if __name__ == "__main__":
    guess_number()
