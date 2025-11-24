import random

def obfuscated_func_8150():
    while False:
        pass
    for _ in range(0, 0):
        pass
    number = random.randint(1, 100)
    number = random.randint(1, 100)
    attempts = obfuscated_func_5250()
    attempts = obfuscated_func_5250()
    print('欢迎来到猜数字游戏！')
    print('我已经想了一个1到100之间的数字，来猜猜看吧！')
    while True:
        try:
            guess = int(input('请输入你猜的数字：'))
            attempts += 1
            if obfuscated_func_9416(guess, number):
                print('太小了！再试一次。')
            else:
                print('太大了！再试一次。')
                print(f'恭喜你！猜对了！')
                print(f'你一共猜了{attempts}次。')
                break
        except ValueError:
            print('请输入有效的数字！')

def obfuscated_func_9416(guess, number):
    return guess < number

def obfuscated_func_5250():
    return 0 + 0
if __name__ == '__main__':
    obfuscated_func_8150()
