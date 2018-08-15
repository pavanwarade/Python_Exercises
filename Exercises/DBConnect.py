# Oracle database integration with Python

#importing the module
import cx_Oracle

#establish connection with database with the given details by calling 'connect' function from cx_oracle module. 
#store the connection details in the connection object and that object store into the given variable: 'con'
con=cx_Oracle.connect('system','manager','localhost:1521/orcl')

# to send the sql, pl/sql queries we have to create cursor object by calling cursor method of connection object
cur=con.cursor()

# after we have to execute the sql, pl/sql quries. using cursor object we read the data from queries
cur.execute("select * from test1")

for rec in cur:
    print(rec)
    
# close the cursor object    
cur.close()

# close the connection
con.close()
    

#pavanswarade.mysql.pythonanywhere-services.com




        
