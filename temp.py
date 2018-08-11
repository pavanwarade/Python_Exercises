"""addition=[1,2,3,4,5,6,7,8,9,10]
jazz=0
for i in addition:
    jazz=jazz+i
print ("First Ten Number Addition is: ", jazz)


#y=int(input("enter the number: "))
y=[5,10,15,20,25,30]
x=-1          # initially we assign x value is -1 coz 
              #we dont know which one is greater including 0
print("before", x) 
for num in y:
    if num>x:   #if num is greater than x value then execute it
        x=num  #assining x value to the num
    print(x,num)
print("after",x)    

def x(a,b,c,d):
    print(d,c,a,b)
    print(c,a,b,d)
    print(a,b,d,c)
    print(b,c,d,a)
x(1,2,3,4)   #a=1, b=2, c=3, d=4

pattern=int(input("enter any number: "))
for i in range(pattern, 0,-1):
    for j in range (0,pattern):
        print
    for j in range (0,i):
        print"*"
print 

 """
print (5+5)
      
