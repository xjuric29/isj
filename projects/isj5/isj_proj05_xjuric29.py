#!/usr/bin/env python3

import re, collections

class Polynomial:
	"""Class for polynomial objects"""
	def __new__ (cls, *argv, **kwargs):		# Arguments verification
		"""This method verify arguments, if arguments are bad, new instance will not create"""
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
				if not re.search (r"^[x][0-9]+$", k) or type (v) != int and type (v) != float:
					makeFlag = 0
		if makeFlag == 1:
			return self

	def __init__ (self, *argv, **kwargs):		# Convert arguments to list
		"""Settings important object variables and arguments processing"""
		self.__valueList = []
		if self.__argType == 0:
			self.__valueList.append (0)
		elif self.__argType == 1:
			self.__valueList = argv[0]
		elif self.__argType == 2:
			for number in argv:
				self.__valueList.append (number)
		elif self.__argType == 3:
			sortedDict = collections.OrderedDict(sorted(kwargs.items()))
			keyCounter = 0
			for key, value in sortedDict.items ():
				while keyCounter != int (key[1:]):		# Appends 0 if exponent is missing
					self.__valueList.append (0)
					keyCounter += 1
				self.__valueList.append (value)
				keyCounter += 1
		for number in reversed (self.__valueList):		# Delete useless 0 if 0 is not only value, this is important for some next methods
			if number == 0 and len (self.__valueList) != 1:
				self.__valueList.pop ()
			else:
				break

	def __str__ (self):
		"""Method returns in human form polynomial"""
		return self.__listToString (self.__valueList)

	def __eq__ (self, other):
		"""This method is called when polynomials is comparing, compare polynomial in string human form"""
		return self.__listToString (self.__valueList) == str (other)

	def __add__ (self, other):
		a = self.__valueList
		b = other.getList ()
		if len (a) > len (b):		# Find which list has less lenght and add it to var a
			tmp = a
			a = b
			b = tmp
		resultList = []
		count = 0
		for i in range (len (b) - len (a)):	# Increase lenght a to b
			a.append (0)
		for number in a:		# Provide adding polynomials
			resultList.append (number + b[count])
			count += 1
		return self.__listToString (resultList)	# Return result in human form

#	def __pow__ (self, other):
#		resultList = self.__valueList
#		for range (other - 1):

	def __listToString (self, polList):
		"""Auxiliary private method for returns polynomial by input list in human form"""
		exp = len (polList) - 1
		firstX = 1		# First cycle flag for right sign displaying
		result = ""
		
		for number in reversed (polList):
			if firstX == 1 and number < 0:		# If in first loop will be number positive, + will not be displayed
				result += "- "
				firstX = 0
			elif firstX == 1:
				firstX = 0
			elif firstX == 0 and number > 0 :
				result += " + "
			elif firstX == 0 and number < 0:
				result += " - "
			
			number = abs (number)		# Sign is resloved and it is no longer necessary
			
			if exp == 0 and number != 0 or exp == 0 and len (polList) == 1:		# Decides whether the element of Polynomial displays and how
				result += str (number)
			elif number == 0:
				result += ""
			elif exp == 1:
				if number != 1:
					result += str (number) + "x"
				else:
					result += "x"
			else:
				if number != 1:
					result += str (number) + "x^" + str (exp)
				else:
					result += "x^" + str (exp)
			exp -= 1
		return result

	def __getNumber (self, base):
		"""Auxiliary private method for self.at_value ()"""
		exp = len (self.__valueList) - 1
		result = 0
		for number in reversed (self.__valueList):		# To result save sum of total number * base^exp 
			result += number * base ** exp
			exp -= 1
		return result

	def at_value (self, *argv):
		"""Returns calculated after x input"""
		if len (argv) == 1:
			return self.__getNumber (argv[0])
		elif len (argv) == 2:		# If count of arguments is 2, returns difference of both calculated values
			return self.__getNumber (argv[1]) - self.__getNumber (argv[0])
		else:
			return 0

	def derivative (self):
		"""Returns new polynomial object who was derivated"""
		derivateList = []
		if len (self.__valueList) == 1:		# If is in list just one value with 0 exponent, returns 0
			derivateList.append (0)
		else:
			count = 0
			for number in self.__valueList:
				derivateList.append (number * count)
				count += 1
			derivateList = derivateList[1:]
		new = Polynomial (derivateList)
		return new
	
	def getList (self):
		return self.__valueList

def test ():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92


if __name__ == '__main__':
    test()
