"""
python的string模块提供了常见的字符常量、字符串模板类和格式化类
"""

import string
import json
import random

# 1.常见的常量，如果要生成定长的字母和数字组合的字符串，就不需要自己定义常量了
print('八进制字符(0-7): ', string.octdigits)
print('十进制字符(0-9): ', string.digits)
print('十六进制字符(0-9a-fA-F) ', string.hexdigits)
print('a-z: ', string.ascii_lowercase)
print('A-Z: ', string.ascii_uppercase)
print('a-Z: ', string.ascii_letters)
print('空白字符: ', json.dumps(string.whitespace))
print('标点符号: ', string.punctuation)
print('可打印字符: ', json.dumps(string.printable))


def generate_random_string(length=32, include_uppercase=False):
    if include_uppercase:
        letters = string.ascii_letters
    else:
        letters = string.digits + string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


if __name__ == '__main__':
    print('随机生成32位定长的数字和字母的字符串: ', generate_random_string(32))



