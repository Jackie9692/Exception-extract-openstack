# encoding utf-8

# def cCparams(li, *tup, **dic):
#     print li
#     print tup
#     print dic
#      
#      
# cCparams(1,2,3,5,6)
# cCparams(1,(1,2), a = 7, b= 9)
# dic = {"d": 1}
# 
# cCparams(1,a=2,7)


# class FirstClass():
#     name = ""
#     username = ""
#     
#     def __init__(self, n, u):
#         self.name = n
#         self.username = u
#     
#     def getName(self):
#         return self.name
#     
#     def getUsername(self):
#         return self.username
#     
# def test(a, *b, **c):
#     print a
#     print b
#     print c
#     
# def main():
# #     fc = FirstClass("123", "username");
# #     print fc.getName()
# #     print fc.getUsername()
#     
#     test(123,(123,45),{"name", "xiyuan"})
#     
# if __name__ == "__main__":
#      test(123,(123,45),{"name", "xiyuan"})
#      
     
class Myclass(object): 
#     position = "manager"
    def __init__(self):
        pass
#         self.name = name
#         self.age = age
#         self.position = "john"
        
    def sayHi(self):
        print "Hi"
    def __str__(self):
        return self.name
    
    
class Mysubclass(Myclass):
    def __init__(self):
#         Myclass.__init__(self, name, age)
        super(Myclass, self).__init__()
        self.company = "wonders"
    def sayHi(self):
        print "subclass Hi"
        
        
subMy = Mysubclass()
subMy.sayHi()



    
        
# my = Myclass("Jackie", 22)   
# 
# # print my.__name
# 
# print my.__init__("John", 100)
# 
# print my.age
# 
# my.gender = "male"
# 
# print my.gender
# 
# # # print my.name
# # # print my.age
# # # 
# # # print my.position
# # # 
# # # print Myclass.position       
# 
# 
# print getattr(my, "name") 
# print getattr(my, "position") 
# print getattr(my, "age") 
# 
# # print getattr(my, "age1") 
# 
# print hasattr(my, "age")
#     
# print my
# 
# str(my)    
#     
    
    
      
     
     
     