#!/usr/bin/env python 

import os

def rename_files():
	#(1) get file names from given folder
	directory = "/Users/angelaambroz/Downloads/prank/"
	file_list = os.listdir(directory)
	print(file_list)

		#(2) remove numerics from file names
	for item in file_list:
		if item == ".DS_Store":
			print "skipping ds store"
		else:
			item_new = item.translate(None,"0123456789")
			new_file = directory + item_new
			old_file = directory + item
			os.rename(old_file, new_file)


rename_files()

