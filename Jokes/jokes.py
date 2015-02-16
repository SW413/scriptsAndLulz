import urllib.request
import sys
import re

p = re.compile('<li>(.+?)</li>', re.DOTALL)
i = 1

while True:
	if i == 23:
		break
	jokes = []
	url = 'http://www.dead-baby-joke.com/dbj_' + '{0:03d}'.format(i) + '.htm'
	f = urllib.request.urlopen(url)
	
	text = f.read().decode('windows-1252')	
	jokes = p.findall(text)
	for joke in jokes:
		jokeOut = re.sub('<[^>]*>', ' ', joke)
		for s in jokeOut.split('\n'):
			if s.lstrip().rstrip() != "":
				print(s.lstrip().rstrip())
	i += 1



