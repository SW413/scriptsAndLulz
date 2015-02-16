import sys
import random   
import time
from subprocess import call    

data = "lyrics"
num_lines = sum(1 for line in open(data))
f = open(data, 'r')
jokes = []
i = 0 

f.seek(0, 2)
eof = f.tell()
f.seek(0, 0)

while f.tell() != eof:
	jokes.append(f.readline() + " ; " + f.readline()) 
	i += 1

rand = random.randint(0, i) 
call(["Say", jokes[rand].split(" ; ", 2)[0]]) 
time.sleep(1)
call(["Say", jokes[rand].split(" ; ", 2)[1]])  
	
	
 

