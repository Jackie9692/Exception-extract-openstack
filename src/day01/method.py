# encoding utf-8


# a = 0;
# def method():
#     a = 100
#     print a
#     
# 
# print a 
# method()
# 
# print a


dic = {"key1":"value1", "key2":"value2"}
# dic.has_keys()

print "%s" + " hdhhh"%("sggyt")


t=('a','b')  
d={'A':'AB','B':'Ab'}  
  
def ab(a,b,A,B):  
    print a,b,A,B  
  
def main(*d,**k):  
    print d,k  
  
if __name__ == '__main__':  
    apply(main,(2,3))  
    apply(main,(2,3),{'a':'5','b':'6'})  
    apply(main,(),{'a':'5','b':'6'})  
  
    main(2,3,a=4,b=5)  
    ab(*t,**d)  