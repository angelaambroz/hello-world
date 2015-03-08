#!/usr/bin/env python 

import os
import random
import time

print "Hi! Welcome to my program."

directory = "/Users/angelaambroz/Downloads/alphabet/"
file_list = os.listdir(directory)

for item in file_list:
	if item == ".DS_Store":
		print "I hope you like this! Just sit back and relax..."		
	else:
		new_file = directory + `random.randint(1,99)` + item
		old_file = directory + item
		os.rename(old_file, new_file)

time.sleep(5)

new_files = os.listdir(directory)

for item in new_files:
	if item == ".DS_Store":
		print "Keep relaxin'..."
	else: 
		test = item.translate(None,"0123456789")
		newer = directory + test
		older = directory + item
		os.rename(older, newer)

time.sleep(5)

print "Now please check Downloads/alphabet for a secret message for you. :)"
