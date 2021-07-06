class Person:
    def __init__(self):
        self.name = '小明'


p = Person()

# id(obj)
# 获取对象的内存地址 <类名 object at 十六进制的内存地址>
print('p的内存地址: ', hex(id(p)))
print('p的字符串表示: ', p)
print(end='\n')

# hasattr(obj, attr_name)
# 判断对象是否有某个属性
print('p具有 name 属性吗? ', hasattr(p, 'name'))
print('p具有 addr 属性吗? ', hasattr(p, 'color'))
print(end='\n')

# getattr(obj, attr_name [, default])
# 获取对象的属性,
# 如果有这个属性的话, 则返回该属性值
# 如果没有的话, 则抛出AttributeError异常, 除非指定了default参数
print('p的 name 属性值为: ', getattr(p, 'name'))
try:
    print('p的 addr 属性值为: ', getattr(p, 'addr'))
except AttributeError as e:
    print(e)
print('p的 color 属性值为: ', getattr(p, 'addr', 'red'))
print(end='\n')

# setattr(obj, attr_name, attr_value)
# 设置对象属性
setattr(p, 'xxx', 1)
print('p的 xxx 属性值为: ', getattr(p, 'xxx'))
print(end='\n')


# isinstance(obj, class_name) or isinstance(obj, (class_name1, class_name2, ...))
# 判断 某个对象是否是某个类的实例
# 相当于java中的 instanceof 关键字
print('数字1是int类的实例吗? ', isinstance(1, int))
print('字符串"a"是dict类的实例吗? ', isinstance('a', dict))
print(end='\n')

# issubclass(subclass, superclass) or issubclass(subclass, (superclass1, superclass2, ...))
print('Person类是object类的子类吗? ', issubclass(Person, object))
print('Person类是str类的子类吗? ', issubclass(Person, str))



