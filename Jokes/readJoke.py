import sys
import random   
import time
from subprocess import call    

data = "jokes2"
num_lines = sum(1 for line in open(data))
f = open(data, 'r')
jokes = []
endLines = ["Top kek", "LOL", "Kappa", "what the fuck", "ha ha ha", "Top kek", "Top kek"]
i = 0 

f.seek(0, 2)
eof = f.tell()
f.seek(0, 0)

while f.tell() != eof:
	jokes.append(f.readline() + " ; " + f.readline()) 
	

shuffledJokes = random.shuffle(jokes)

while i < len(jokes):
	say = jokes[i].split(" ; ", 2)
	print(say[0])  
	call(["Say", say[0]])
	if say[0].strip().endswith("?"): 
		time.sleep(1)
	else:
		time.sleep(0.25)
	print(say[1]) 
	call(["Say", say[1]])
	wait = random.randint(2,3)
	time.sleep(wait) 
	call(["Say", "-v", "Kate", random.choice(endLines)])
	wait = random.randint(5,300)
	print(wait)
	time.sleep(wait) 
	i += 1   
	           