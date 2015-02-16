#!/usr/bin/python

import time

productOne = 10


while productOne >0:
	time.sleep(1)
	print(productOne)
	productOne -=1

if productOne ==0:
	print("Done!")