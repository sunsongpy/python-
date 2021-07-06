import io

# 自定义打印的分割符
# 默认是一个空格
print(1, 2, 3, 4, 5, sep='-')

# 不换行打印
# 默认 end='\n'
print('我是第一行, ', end='')
print('我还是第一行')


# 指定输出
# 默认, file=sys.stdout, 即写入到标准输入中, 在控制台显示
# 可以指定其他可写入的对象, 这样就不会打印到控制台了
# 1. 写入到 io.String 的对象中
io_obj = io.StringIO()
print('read_obj里的值: ', io_obj.getvalue())
print('我爱python', file=io_obj)  # "我爱python" 不会打印到控制台, 而是写入到了 io.String 的对象中
print('read_obj里的值: ', io_obj.getvalue())

# 2. 写入到file对象中
file_obj = open('./data.txt', mode='a')
print('我爱python', file=file_obj)  # "我爱python" 不会打印到控制台, 而是写入到了 ./data.txt 文件中
file_obj.close()

