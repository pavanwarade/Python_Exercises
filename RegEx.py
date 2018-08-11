"""
# 1) match () meythod
import re
hg="pavanswarade@gmail.com pavanswarade@gmail.com"
mat=re.match("^p.+@",hg)
print(mat)
"""



# 3)Findall() method
"""
import re
line="pet:cat i lovecat pet:cow i love cow"
mat= re.findall("^l.+c",line) #Non Greedy (? mark entertain non-greedy string)
print(mat)
"""

"""
import re
line="pet:cat i love cat pet:cow i love cow"
mat= re.findall("^p.+:",line)  #Greedy
print(mat)
"""

import re
line="love cat pet:cow i love cow"
mat= re.findall("^l.+?e",line) #Non Greedy (? mark entertain non-greedy string)
print(mat)
# search() method
"""
import re
line="love cat pet:cow i love cow"
mat= re.search("p.+o",line) #Non Greedy (? mark entertain non-greedy string)
print(mat.group())

import re
line="i love my country india pavanswarade@gmail.com:pavan warade"
mat=re.search("p.+?e",line) # Non-greedy
print(mat.group())

# split () method
import re
line="love cat pet:cow i love cow"
mat= re.split("c.w",line) #Non Greedy (? mark entertain non-greedy string)
print(mat)


import re
line="i love my country india pavanswarade@gmail.com:pavan warade"
mat=re.split("p.+?n",line)
print(mat)

"""
#replace() method
"""
import re
mymails="pavanswarade@gmail.com, nareshit@abc.com, jhfkfunnn@dnf.com, nhdjjm@njdhh.com, nmkhhjnsj@hhx.com"
mat=re.sub("@\w+","@gmail",mymails)
print(mat) 
"""

###########............Regular Expression By LOKESHIT.........################################

import re
regex= "[a-zA-Z]+ (\d+)"
matches=re.findall(regex,"June 24, augast 9, Dec 20, Feb 10")
for match in matches:
    print("match month: ",match)

import re
regex="([a-zA-Z]+) \d+"
matches=re.finditer(regex,"June 24, August 09, Jan 25, Feb")
for match in matches:
    print("match at index",match.start(),match.end())

import re
regex=re.compile("(\w+) world")
result=regex.search("Hello world is the easiest world")
if result:
    print(result.start(),result.end())

####............Extract Mail Ids From the file..............################
    
import re
regex=re.compile ("\S+@\S+")
fp=open("Email.txt")
data=fp.read()
res=regex.findall(data)
for result in res:
    print(result)
    
#######........Valid the password .............###########
import re    
    
    
    




















