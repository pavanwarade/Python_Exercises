"""
import smtplib
content='welcome to python'
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('pavanswarade@gmail.com','7448112173')
mail.sendmail('narendramodi@gmail.com','pavanswarade@gmail.com.com')
mail.close()
"""

line='python@openSource@language'
word=line.split("@")
for i in word:
    print(i)
    
    
a=['pava','warae']
b=[10,20]
c=['mlk','bul']
z=zip(a,b,c)
print(z)    