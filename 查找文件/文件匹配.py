import fnmatch

# fnmatch(file_name, pattern)
# 判断 file_name是否符合 pattern
# pattern 支持 unix通配符:
# * 匹配任何字符
# ? 匹配单一字符
# [] 匹配字符组
# [!] 排除匹配字符组
print(fnmatch.fnmatch('abc.txt', '*.txt'))
print(fnmatch.fnmatch('abc.txt', 'a?c.txt'))
print(fnmatch.fnmatch('abc.txt', 'a?.json'))
print(fnmatch.fnmatch('abc.txt', 'a[a-z]c.txt'))
print(fnmatch.fnmatch('abc.txt', 'a[!1-9]c.txt'))
print(end='\n')


# filter([file_name1, file_name2, ...], pattern)
print(fnmatch.filter(['abc.txt', 'edf.json', 'home.txt'], '*.txt'))
