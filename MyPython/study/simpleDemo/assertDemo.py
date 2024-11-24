# encoding: UTF-8
age = 20
assert 18 < age < 25, '年龄不符合范围' # 【, '断言表达式为False时输出错误信息'】
print('程序执行到这里')

assert 25 < age < 30, '年龄不符合范围'
print('程序不会执行到这里')