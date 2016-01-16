# encoding utf-8

def hello():
    print "hello"


# def hello(name):
#     print name    
# def hello():
#     print "hello two"
# a = 1
# print a
# 
# hello()

class Myclass():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print "hello" + self.name
        
        
        
        
if __name__ == "__main__":
    hello()
    myclass = Myclass("Jackie", 24)
    myclass.hello()


