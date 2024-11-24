# encoding: UTF-8

print('赋值运算符')
# 赋值运算符
num = 1024
print('num = %d' % num)

print('算术运算符')
# 加法计算

num_a = 10
num_b = 20
result = num_a + num_b # 进行加法计算
print('加法计算结果：' + str(result)) # 字符串连接运算符

# 使用括号改变多个运算符的优先级
num = 3 * 6 - 9 - 8 + 6/2 + 10
print(num) # 14.0
num = 3 * (6 - 9 - 8) + 6/2 + 10
print(num) # -20.0

# 算术运算符
result = (1+2)*(4/2)
print('整数遇到浮点数结果为浮点数：%f' % result) # 6.0

## 使用整除
result = (1+2)*(4//2)
print('整数*整数结果为整数：%d' % result) # 6

## 除法 和 整除
print('整数相除不尽：%s' % (10/4))
print('除法计算返回商:%s' % (10//4))

print('取模运算：%s' % (10 % 4))

## 幂运算
result = 10 ** 3
print("10的3次方结果为：%s" % result)

## 简化赋值运算符
num_a = 10
num_a += 100 # 等价于 num_a = num_a + 100
print('num_a = %s' % num_a)

# 字符串上使用乘法运算 (其他算术运算符不支持)
info = 'hello wold\t'
info = 3
print(f'字符串上使用乘法运算结果为重复出现：{info}')

#######################3
# 关系运算符
print('关系运算符')
print('100 == 100 ? %s' % (100 == 100))
print('100 != 100 ? %s' % (100 != 100))
print('100 > 90 ? %s' % (100 > 90))
print('100 >= 90 ? %s' % (100 >= 90))
print('100 < 90 ? %s' % (100 < 90))
print('100 < 102 ? %s' % (100 <= 102))

# 数值类型内容比较
num_a = 10
num_b = 10
result = num_a == num_b # 判断两个变量的内容是否相同
print('num_a == num_b ? %s' % result)

# 字符串类型内容比较
print('字符串类型内容比较，"Alibaba" == "Alibaba" ? %s', ('Alibaba' == 'Alibaba')) # True
print('字符串类型内容比较，"alibaba" == "Alibaba" ? %s', ('alibaba' == 'Alibaba')) # False

# 通过ord()函数观察字母"a" 与 字母 "A" 的数值
print('a ord value is %s' % ord('a'))
print('A ord value is %s' % ord('A'))
print('a > A ? %s' % ('a' > 'A'))

## 同时使用多个运算符
age = 18
result = 15 <= age <= 28
print(result)

## 逻辑运算
age = 25
logic_a = (20 <= age <= 30) 
logic_b = (age >= 30)
print('logic_a and logic_b result %s' % (logic_a and logic_b)) 
print('logic_a or logic_b result %s' % (logic_a or logic_b)) 
print('not logic_b result %s' % (not logic_b)) 

## 位运算
num_a = 13 # 二进制：1101
num_b = 7  # 二进制：0111 
print('按位与运算结果：%s' % (num_a & num_b)) # 二进制结果为：0101，十进制为：5
print('按位或运算结果：%s' % (num_a | num_b)) # 二进制结果为：1111，十进制为：15
print('按位异或运算结果：%s' % (num_a ^ num_b)) # 二进制结果为：1010，十进制为：10

## 身份运算符号
num_a = 2
num_b = 1 + 1
num_c = 4 - 2
print('num_a 变量的内存地址：%s' % id(num_a)) 
print('num_b 变量的内存地址：%s' % id(num_b)) 
print('num_c 变量的内存地址：%s' % id(num_c)) 
# num_a、num_b、num_c 的值都是2，这三个变量都指向了同一块内存地址。

info_a = 'Alibaba'
info_b = 'Alibaba'
print('info_a 变量的内存地址：%s' % id(info_a))
print('info_b 变量的内存地址：%s' % id(info_b))
# info_a、info_b 的值相同的，这两个变量都指向了同一块内存地址。

num_int = 10
num_float = 10.0
print('10 == 10.0 ? %s' % (10 == 10.0)) # 10 == 10.0 ? True
print('整形变量内存地址：%s，浮点型变量内存地址：%s' % (id(num_int),id(num_float))) #整形变量内存地址：4411130384，浮点型变量内存地址：4412212752
# PY 里认为 10 和 10.0 的内容是相同的，因为在计算时整形会向浮点型转换后再计算，但是他们的内存地址是不同的。
# 所有依靠 “==” 是无法区分内存关系的，需要 == 和 内存双判断（在Java中如果是引用类型，那么 == 是判断变量的内存地址是否相同）
# 身份运算符就是为了解决这个问题

## is or is not
print('num_a is num_b ? %s' % (num_a is num_b)) # True
print('num_a is num_c ? %s' % (num_a is num_c)) # True
print('info_a is not info_b ? %s' % (info_a is not info_b)) # False
print('num_int is num_float ? %s' % (num_int is num_float)) # False

## 常量
C_a = 'HELLO'
C_b = 'HELLO'
print('C_a is C_b %s' % (C_a is C_b))

17746291639





