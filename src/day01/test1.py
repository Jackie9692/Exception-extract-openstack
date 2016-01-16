# -*- coding:utf-8 -*-

# import xlwt
# from datetime import datetime
# 
# style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
#     num_format_str='#,##0.00')
# style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
# 
# wb = xlwt.Workbook()
# ws = wb.add_sheet('A Test Sheet')
# 
# ws.write(0, 0, 1234.56, style0)
# ws.write(1, 0, datetime.now(), style1)
# ws.write(2, 0, 1)
# ws.write(2, 1, 1)
# ws.write(2, 2, xlwt.Formula("A3+B3"))

# wb.save('C:\Users\daxu\workspace\Demo\example.xls')
# str_utf_8 = "汉子"
# str_assi = "hanzi"
# print len(str_utf_8)
# print len(str_assi)

# u = u'汉'
# print repr(u) # u'\u6c49'
# print u # u'\u6c49'
# s = u.encode('UTF-8')
# print repr(s) # '\xe6\xb1\x89'
# print u
# u2 = s.decode('UTF-8')
# print repr(u2) # u'\u6c49'
#  
# # 对unicode进行解码是错误的
# s2 = u.encode('UTF-8')
# print s2
# 同样，对str进行编码也是错误的
# u2 = s.encode('UTF-8')

# raiseMsgStack = {}

# lineArr = ["d", "(name, sex))qwe","wewqe"]
# 
# # if len(raiseMsgStack) == 0:
# #     print "stack is empty"
# 
# labelNum = 1;
# 
# msg = ""
# 
# for line in lineArr:
#     for char in line:
#         print char
#         if char == '(' :
#             labelNum += 1
#         elif char == ')':
#             labelNum = labelNum - 1
#         else:
#             pass
#         if labelNum == 0:
#             break
#         else:
#             msg = msg + char
#     if labelNum == 0:
#             break
#            
# print msg


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x
    

# print my_abs(-1)
# try:
#     my_abs('A')
# except TypeError as err:
#     print err
# else:
#     print "no exception"
# finally:
#     print "finally"
# print my_abs(-1.2)    


class MyClass:
    name = "Jackie"
    def sayHello(self):
        print self.name
                     
                     
def testVaribleParameter(aa, *nums, **dicts):
    print nums
    print dicts
    dicts.name = "nihai"
    print dicts
                                    

#      测试可变参数      
# def f1(a, b, c = 0, *d, **kw):
#     print('a =', a, 'b =', b, 'c =', c ,'d =', d, 'kw =', kw)
# args = (1, 2, 3)
# kw = {'name': 'jackie'}
# f1(args, *(1, 2, 3), **kw)        
# f1(*args, **kw)        
    
#测试汉诺塔

def move(n, A, B, C):
    if n == 0: 
        return 
    else:
        move(n-1, A, C, B)
        print(A, '->', C)
        move(n-1, B, A, C)
        
# move(3,'A','B', 'C')
    
colors = ["red", "yellow", "blue"]
for x in range(5):
   print(x)
   
for i in range(0, len(colors)):
    print(i, colors[i])









    
         


