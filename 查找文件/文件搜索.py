import glob

# glob(pattern) or glob(pattern, recursive=True)
# recursive=False, 默认只匹配当前路径下的文件
print(glob.glob('*.txt'))

# recursive=True并且pattern="**"时, 返回当前路径下所有的文件，包括递归子目录
print(glob.glob('**', recursive=True))

# iglob同上, 只是返回一个迭代器,  glob()其实就是list(iglob())

