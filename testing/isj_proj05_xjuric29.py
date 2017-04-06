#!/usr/bin/python3.6

import re

class Polynomial:
	def __new__ (cls, *argv, **kwargs):		# Arguments verification
		self = super().__new__(cls)
		makeFlag = 0
		
		if len (argv) == 0 and len (kwargs) == 0: # If there is no argument polynomial is 0
			self.__argType = 0
			makeFlag = 1
		elif len (argv) == 1 and len (kwargs) == 0 and type (argv[0]) == list:		# If first argument is list of numbers
			self.__argType = 1
			makeFlag = 1	
			for item in argv[0]:
				if type (item) != int and type (item) != float:
					makeFlag = 0
		elif len (argv) != 0 and len (kwargs) == 0:		# If arguments are numbers
			self.__argType = 2
			makeFlag = 1
			for item in argv:
				if type (item) != int and type (item) != float:
					makeFlag = 0
		elif len (argv) == 0 and len (kwargs) != 0:		# If arguments are in xy=number format
			makeFlag = 1
			self.__argType = 3
			for k, v in zip (kwargs.keys (), kwargs.values ()):
				if not re.search (r"^[x][0-9]", k) or type (v) != int and type (v) != float:
					makeFlag = 0
		if makeFlag == 1:
			return self

	def __init__ (self, *argv, **kwargs):		# Convert arguments to list
		self.__valueList = []
		if self.__argType == 0:
			self.__valueList.append (0)
		elif self.__argType == 1:
			self.__valueList = argv[0]
		elif self.__argType == 2:
			for number in argv:
				self.__valueList.append (number)
		elif self.__argType == 3:
			
a = Polynomial (x0=4, x2=5)
print (a.__argType)
