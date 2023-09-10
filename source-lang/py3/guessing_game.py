#! python3
import random

'''
python语法关键字

class 定义类
def   定义函数

条件语句

    if ...
    if ... else ...
    if ... elif ...
    if ... elif ... else ...

循环语句

    for ...
    for ... in ...
    while ...

    循环语句中的一些关键字
    
        continue  跳过剩下步骤，进入下一次循环
        break     跳出循环

python的一些约定

- 函数一般命名为全小写单词之间使用_连接（蛇形命名）
- 类对象名一般单次首字母大写（大驼峰），如NoteBook

在一个类对象中：
1. `_`  单下划线前缀表示 protected
2. `__` 双下划线前缀表示 private
3. 类对象的每一个功能函数一般第一个参数都命名为 self, self指代对象自己

不在类对象中：
1. `_` 通常表示忽略，不使用的变量
'''

# class 关键字，创建一个对象


import random


class GuessingName:

    # def 关键字，创建一个函数
    def __init__(self):

        # self. 前缀表示该变量属于GuessingName，coder 无法直接获取该变量
        # _ 表示该变量是受保护变量，只能由该对象或者继承自该对象的子对象访问
        # __ 表示该变量是私有变量，只能由该对象本身访问
        self.__secret_number = random.randint(1, 101)

    def _get_guess_number(self):
        guess = input("Please input your guess.")

        try:
            guess = int(guess)
        except ValueError as _:
            return None

        return guess

    def run(self):
        print("Guess the number!")

        guess_num: int = 0
        while True:
            guess_num = self._get_guess_number()

            if not guess_num:
                continue
            elif guess_num == self.__secret_number:
                print('You win!')
                break
            elif guess_num < self.__secret_number:
                print('Too small!')
            else:
                print('Too big!')


if __name__ == "__main__":

    def for_in_example():
        '''
        循环语句 for ... in ... 使用举例
        '''
        for i in "Hello, world!":  # ['H', 'e', 'l', 'l', 'o', ',', 'w', 'o', 'r', 'l', 'd', '!']:
            print(f'{i}', end='')
        print()
    for_in_example()

    GuessingName().run()
