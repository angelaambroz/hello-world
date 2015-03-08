#!/usr/bin/env python 

import time
import webbrowser

count = 1

print("This program started on " +time.ctime())
while (count<=4):
	time.sleep(5)
	webbrowser.open("http://www.google.com/", new=2, autoraise=True)
	count = count+1


