count = 1
while (count <=100):
	if count%5==0 and count%3==0:
		print "CracklePop"
	elif count%3==0:
		print "Crackle"
	elif count%5==0:
		print "Pop"
	else:
		print count;
	count = count+1