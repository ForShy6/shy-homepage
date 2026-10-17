# -*- coding: utf-8 -*-
"""
猜数字小游戏
规则：程序随机生成一个 1-100 的整数，玩家不断输入猜测，
      程序提示"大了"或"小了"，直到猜中为止。
运行方式：在命令行执行  python guess_number.py
"""

import random  # 引入随机数模块，用于生成答案


def main():
    # 第 1 步：随机生成 1 到 100 之间的整数作为本局答案
    answer = random.randint(1, 100)
    guess_count = 0  # 记录有效猜测的次数（无效输入不计数）

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个 1 到 100 之间的整数，开始猜吧！")

    # 第 2 步：进入循环，直到玩家猜中才结束
    while True:
        user_input = input("请输入你猜测的数字（1-100）：").strip()

        # 第 3 步：校验输入是否为整数，不是整数则提示并重新输入
        try:
            guess = int(user_input)
        except ValueError:
            print("输入无效：请输入一个整数哦，本次不计入猜测次数。")
            continue  # 跳过本轮剩余代码，回到循环开头

        # 第 4 步：校验数字是否在 1-100 范围内
        if guess < 1 or guess > 100:
            print("超出范围：数字需要在 1 到 100 之间，本次不计入猜测次数。")
            continue

        # 走到这里说明是有效猜测，次数加 1
        guess_count += 1

        # 第 5 步：比较猜测值与答案，给出提示
        if guess > answer:
            print("大了，再往小猜一猜！")
        elif guess < answer:
            print("小了，再往大猜一猜！")
        else:
            # 猜中了：输出恭喜信息和总次数，并用 break 结束循环
            print(f"恭喜你，猜对了！答案就是 {answer}。")
            print(f"本局你一共猜了 {guess_count} 次。")
            break


if __name__ == "__main__":
    # 直接运行本文件时，从 main() 开始执行
    main()
