def rev(msg):
    revstr=""
    for i in msg:
        revstr=i+revstr
    print(revstr)
rev("INDIA")

# Factorial 
# 1)
n = 23
fact = 1
 
for i in range(1,n+1):
    fact = fact * i
     
print ("The factorial of 23 is : ",end="")
print (fact)

# 2) 
number=int(input("enter any no: "))
fact=1
for i in range(number):
    fact=fact*(i+1)
print(fact)    




a="pavan"
b=a[::-1]
print(b)


print(input("enter no: ") + (input("enter the no: ")))