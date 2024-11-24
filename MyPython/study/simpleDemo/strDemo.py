# encoding: UTF-8

# 字符串

'''
在Python中可以使用单引号或双引号来定义。
在Python中没有字符的概念
'''

info = "Hello wold"

msg = 'This is Hangzhou'

print(info)
print(msg)
print(type(info))
print(type(msg))


'''
那么在开发中使用单引号还是双引号呢？
注意要统一
'''


# 预处理，多行字符串, 三个双引号
info = """
	This is Hangzhou
	Welcome
"""

print(info)


# 续行
info = "This is Hangzhou"\
" Welcome Hangzhou"

print(info)

# 字符串连接

# TypeError: can only concatenate str (not "int") to str, 加号只能拼接字符串类型
# info = "This is Hanghou " + "Welcome to Hanghou " + " xihu" + 50
info = "This is Hanghou " + "Welcome to Hanghou " + " xihu"
print(info)

# 转义字符
info = "This is Hanghou , Here is \"xihu\"\n\t We have Alibaba"
print(info)

# 字符与数值之间的转换
a_num = ord('a')
print(f'小写字母a的数值{a_num}')

a_char = chr(97)
print(f'数字97对应的字符{a_char}')
