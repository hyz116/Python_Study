# encoding: UTF-8

# 从键盘输入两个数字，进行加法计算

num_a = int(input("请输入第一个整数:"))

num_b = int(input("请输入第二个整数:"))

result = num_a + num_b

print(result)
print(type(result))

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(num_a + " + " + num_b + " = " + result)
# 任何数据与字符串使用“+”连接都是需要使用 str() 先转为字符串
print(str(num_a) + " + " + str(num_b) + " = " + str(result))
