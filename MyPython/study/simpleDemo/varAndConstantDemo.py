# encoding: UTF-8

# 变量：变量是内存中用于存储数据的命名位置。在程序运行过程中其值可以被修改。它是动态类型，可以是不同的数据类型。
"""
一些特点：
1. 动态类型：Python 是动态类型，不需要声明数据类型，它在运行时决定数据类型
2. 命名规则：参考标识符定义
3. 赋值
4. 再赋值

其他
可以使用 del 删除变量
"""

x = 10 # x is an integer
print(f"x value is {x}")

#print(f"xxx {var or constant}) format output

x = "hello"  # x is an String
print(f"x value is {x}")

del x
# print(x)



# 常量：常量是一种变量，其值在整个程序中保持不变。
"""
特点：
1. 命名格式以大写字母为主，多个大写字母以下划线分割
2. 不变性
"""

MY_NAME = "chuye"
print(f"My name is {MY_NAME}")

# MY_NAME = "huangyuze"

'''
变量和常量用于存储和管理数据
'''