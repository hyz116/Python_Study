# encoding: UTF-8

'''
常用数据类型：整数、浮点数、复数、布尔类型、字符串、列表、元祖、字典、日期，并且全部都是引用传递类型。

1. 数值类型：int、float、
2. 序列类型：str、list、tuple
3. 映射类型：dict
4. 集合类型：set、frozenset
5. 布尔类型：bool
6. None Type
'''

# 数值类型
x = 20
y = 18.8
print(f"x is {x}")
print(f"y is {y}")


# 序列类型
# str
name = "chuye"
print(f"my name is {name}")

# list： 有序、可变的集合。可以包含复杂的数据类型
fruits = ["apple", "bnana", "cherry"]
print(f"frutis are {fruits}")

# tuple: 与list类似，但是不可变
coordinates = (10, 10.5)
print(f"coordinates are {coordinates}")
# coordinates = ("hello")
# print(f"coordinates are {coordinates}")

# dict: 无序的key-value对，key 唯一且不可变
person = {"name":"chuye","age":18}
print(f"person info:{person}")

# set Types
# set: 无序且唯一的集合，可变
unique_numbers = {1, 2, 3, 4}
print(f"unique_numbers are {unique_numbers}")

# frozenset: 一旦常见，其元素不能被修改
frozen_numbers = frozenset([1, 2, 3, 4])
print(f"frozen_numbers are {frozen_numbers}")

# bool: 标识布尔类型，其值可以是 True 或者 False
is_active = True
print(f"is_active is {is_active}")

# None Type: 表示值是不确定的，null
# 没有任何内存指向
result = None


# 类型检查和转换
# 类型检查，type函数
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(name))
print(type(fruits))
print(type(coordinates))
print(type(person))
print(type(unique_numbers))
print(type(frozen_numbers))
print(type(is_active))
print(type(result))

## 类型转换
num = 5
float_num = float(num)
print(f"float_num is {float_num}, and type is {type(float_num)}")








