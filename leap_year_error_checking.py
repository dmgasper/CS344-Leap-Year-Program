#!/usr/bin/python


# To run this program, use the following command:
#
# python leap_year_error_checking.py YEAR
#
# where YEAR is a valid integer
#
# Example usage:
#
# $ python david_gasper_hw1.py 2012
# 2012 is a leap year


import sys

if (len(sys.argv) != 2):
	print ("Incorrect number of arguments supplied!")
else:
	try:
		year = int(sys.argv[1])
		if (year % 4 == 0 and not(year % 100 == 0) and not(year % 400 == 0)):
			print (str(year) + " is a leap year")
		else:
			print (str(year) + " is not a leap year")
	except ValueError:
		print ("Argument is not a valid year!")
