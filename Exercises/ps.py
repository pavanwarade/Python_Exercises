"""
x=open("report.txt",mode="r")# read mode is default here/whether type or not its read.
for cheez in x:
    print(cheez)
"""
"""
temp="NareshIT 22536 for 445 Nit"
data=[x for x in (int(x) for x in temp if x.isdigit()) if x%2 ==0]
print(data)
"""
"""
class person:
    def __init__(self,username):
        self.username=username
        self.__password="sai"
        self._hii='gii'
    def get_pass(self,sam):
        if sam=="ram":
            return self.__password
        else:
            print("wrong username")
myobj=person("ps")
myobj.get_pass("ram")
"""
"""
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))

"""
"""
t=(1,2,4,3,8,9)
[t(i) for i in range (0,len(t),2)]

"""
"""
print(math.copysign(3,-1))
"""
"""
import math
print(math.fabs(-3.4))
"""











































