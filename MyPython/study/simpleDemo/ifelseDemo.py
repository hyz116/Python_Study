# encoding: UTF-8
# if 分支语句
age = 20
if 18 <= age <= 22: # 表达式后面需要跟一个冒号, 布尔表达式不需要使用括号括起来
	print('我是一个大学生') # 采用缩进来表示该语句为if表达式作用内的语句
print('即使不是大学生，每天都要学习') # 如果没有缩进，该语句不属于if表达式里的语句

# if...else... 结构
money = 1000000.00
if money >= 1000000.00:
	print('我是一个富人')
else:
	print('我是一个穷人')

# 多分支判断语句
score = 65.0
if 60 <= score <= 70:
	print('差等生')
elif 70 < score <=80:
	print('中等生')
elif 80 < score <=90:
	print('优等生')
else: # 最后的 else 是可选的
	print('三好学生')
