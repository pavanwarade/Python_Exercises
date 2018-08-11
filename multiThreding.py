import threading
class x(threading.Thread):
    def run(self):
        for p in range(1,101):
            print(p)
class y(threading.Thread):
    def run(self):
        for q in range(101,201):
            print(q)            
x=x()
y=y()
x.start()
y.start()            


help(threading)  

          

print ("C:\Users\hh\narendra")