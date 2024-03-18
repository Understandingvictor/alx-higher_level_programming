#!/usr/bin/python3
def no_c(my_string):
	my_str = ""
	for i in my_string:
		if i == "c":
			del i
		elif i == "C":
			del i
		else:
			my_str.append(i)
	return my_str
