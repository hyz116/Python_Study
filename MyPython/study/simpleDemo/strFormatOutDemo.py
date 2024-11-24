# encoding: UTF-8

# 格式化输出，格式 “字符串” % (var1, var2)

name = "chuye"
age = 18
salary = 5000.34

print("姓名：%s, 年龄：%d, 工资；%f" % (name, age, salary))


# 格式化自动填充，vars()函数
print("姓名：%(name)s, 年龄：%(age)d, 工资；%(salary)f" % vars())


# 自定义完结符，print()函数默认的完结符号为换行符，可以使用 end 来自定义完结符
print("chuye", end=",")
print("杭州", end="\n")
print("程序员", end=".....\n")
