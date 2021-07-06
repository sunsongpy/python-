def abs_test():
    """
    绝对值函数
    :return:
    """
    return abs(-1)  # 1


def sum_test():
    pass


def div_mod_test():
    """
    商模函数  div(x, y) -> (x//y, x%y)
    :return: (整商, 余数)
    """
    return divmod(7, 2)  # (3, 1)


def max_min_test():
    """
    最大值函数和最小值函数:
        max:
            max(可迭代对象[, key=func])
            max(x, y, z, ...[, key=func])

            注意key参数，可以传入一个函数，用于获取判断的依据，如果是一个以复杂对象为元素的数组，找出其中'最大'的一个时，就比较有用了
        min:
            同上
    :return:
    """
    person = [{'name': 'sun', 'age': 18}, {'name': 'song', 'age': 16}]
    return max(person, key=lambda x: x['age'])  # {'name': 'sun', 'age': 18}


def pow_test(x, y, z=None):
    """
    幂函数
        pow(x, y) -> x**Y
        pow(x, y, z) -> x**y % z
    :return:
    """
    return pow(x, y, z)
