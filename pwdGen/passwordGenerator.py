#!/usr/bin/python

import sys
import random

def generatePassword(data, numAnswer, symbols, wordLen, upperC):
	f = open(data, 'r')
	wholeList = []
	wordArray = []
	length = 0
	for line in f:
	    wholeList.append( line )
	wholeList.sort(key = len)
	i = 0
	while True:
		if len(wholeList[i]) > wordLen + 1:
			wordArray.append(wholeList[i])
		if len(wholeList[i]) > wordLen + 2:
			break
		i += 1
	numLines = len(wordArray)

	if numAnswer.lower() == "y":
		number = random.randint(10,99)
		if symbols != "":
			middle = str(number) + str(random.choice(symbols))
		else:
			middle = str(number)
	elif numAnswer.lower() == "n":
		if symbols != "":
			middle = str(random.choice(symbols))
		else:
			middle = ""
	else:
		return "You answered wrong!"
	first = random.randint(0, numLines)
	second = random.randint(0, numLines)
	wordOne = wordArray[first].strip()
	wordTwo = wordArray[second]
	if upperC.lower() == "y":
		x = random.randint(0, 1)
		if x == 0:
			password = '{}{}{}'.format(wordOne.upper(), middle, wordTwo)
		elif x == 1:
			password = '{}{}{}'.format(wordOne, middle, wordTwo.upper())
	elif upperC.lower() == "n":
		password = '{}{}{}'.format(wordOne, middle, wordTwo)
	return password

def passwordStrength(password):
	score = 0
	msg = []
	symbols = ["!", "#", "%", "&", "/", "(", ")", "=", "?", ",", ".", " "]
	a = 0
	b = 0
	if len(password) > 10:
		print "LENGTH: " + str(len(password))
		score += 1.5
	elif len(password) >= 6:
		print "LENGTH: " + str(len(password))
		score += 1
	else:
		print "WARNING: You should have atleast 9 characters!"
		print "You only have " + str(len(password))
	while True:
		if password.find(str(b)) == -1:
			b += 1
		elif password.find(str(b)) != -1:
			print "CONTAINS: NUMBERS"
			score += 1
			break
		if b == 10:
			print "WARNING: You should have numbers!"
			break
	if password.islower() or password.isupper():
		print "WARNING: You should have mix upper and lower case!"
	else:
		print "CONTAINS: MIXED CASE"
		score += 1
	while True:
		if password.find(symbols[a]) == -1:
			a += 1
		elif password.find(symbols[a]) != -1:
			score += 1.5
			print "CONTAINS: SYMBOLS"
			break
		if a == len(symbols):
			break
	if score <= 2:
		print "Password strength: Weak"
	elif score <= 3:
		print "Password strength: Medium"
	elif score <= 4:
		print "Password strength: Strong"
	elif score > 4:
		print "Password strength: Ultra strong!"
	
wordLen = random.randint(3, 10) #int( input("How long should the two words be? ") )
numAnswer = random.choice("yn")#raw_input("Should the password contain numbers? y/n ").strip()
symbols = random.choice("!#%&/()=?")#raw_input("What special characters do you want in your password? (leave blank if none) ")
upperC = random.choice("yn")#raw_input("Should one of the words be upper case? y/n ").strip()
password = generatePassword("5desk.txt", numAnswer, symbols, wordLen, upperC)
print password
passwordStrength(password)
