import cx_Oracle
con=cx_Oracle.connect('system','manager','localhost:1521/orcl')
cur=con.cursor()
cur.execute("select * from test1")
for rec in cur:
    print(rec)
cur.close()
con.close()
    

#pavanswarade.mysql.pythonanywhere-services.com




        