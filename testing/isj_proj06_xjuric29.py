#!/usr/bin/env python3

import copy

def first_nonrepeating (string):
	"""The function print first unique char from inserted string"""
	if type (string) != str:		# If var string is not string
		return None
	tmp = {}
	for char in string:		# To tmp dict store chars like keys and char counts like values
		if char in dict.keys (tmp):
			tmp[char] += 1	
		else:
			tmp[char] = 1
	for key, value in zip (dict.keys (tmp), dict.values (tmp)):
		if value == 1:
			return key
	return None

def combine4 (origList, result):
	"""From first four numbers in list print all expressinos which are equal with fifth number"""
	if type (result) != int or type (origList) != list or len (origList) != 4: # Input data checking
		return None
	for item in origList:
		if type (item) != int:
			return None

	allComb = []
	signs = ["+", "-", "*", "/"]
	numberRange = [0, 1, 2, 3]
	for brackets in range (10):		# Bruteforce method to saving all combination (division by zero included) of inserted numbers and signs and brackets. I apologize for this solution, task was definitely to recursion but I dont have more time for changing alghorithm.
# 10 options of brackets:
# 0: (a b) c d
# 1: (a b)(c d)
# 2: a b (c d)
# 3: a (b c) d
# 4: (a b c) d
# 5: ((a b) c) d
# 6: (a (b c)) d
# 7: a (b c d)
# 8: a ((b c) d)
# 9: a (b (c d))
		for number1 in range (4):	# To result string (expr7) insert first number
			expr1 = ""
			if brackets == 0 or brackets == 1 or brackets == 4 or brackets == 5 or brackets == 6:	# If is combination with ( on start, insert it before number
				expr1 += "("
				if brackets == 5:
					expr1 += "("
			expr1 += str (origList[number1])
			for sign1 in range (4):		# To result string (expr7) insert first sign
				expr2 = expr1
				expr2 += signs[sign1]
				if brackets == 3 or brackets == 6 or brackets == 7 or brackets == 8 or brackets == 9:
					expr2 += "("		# If is combination with ( after sign, insert it
					if brackets == 8:
						expr2 += "("
				numberRange2 = copy.deepcopy (numberRange)		 # To numberRange2 copy numberRange without number1 index
				numberRange2.remove (number1)
				for number2 in numberRange2:		# To result string (expr7) insert second number
					expr3 = expr2
					expr3 += str (origList[number2])
					for sign2 in range (4):
						expr4 = expr3
						if brackets == 0 or brackets == 1 or brackets == 5:		# If is combination with ) before sign, insert it
							expr4 += ")"
						expr4 += signs[sign2]
						if brackets == 1 or brackets == 2 or brackets == 9:		# If is combination with ( after sign, insert it
							expr4 += "("
						numberRange3 = copy.deepcopy (numberRange)		 # To numberRange3 copy numberRange without number1 and number2 index
						numberRange3.remove (number1)
						numberRange3.remove (number2)
						for number3 in numberRange3:		# To result string (expr7) insert third number
							expr5 = expr4
							expr5 += str (origList[number3])
							for sign3 in range (4):
								expr6 = expr5
								if brackets == 3 or brackets == 4 or brackets == 5 or brackets == 6 or brackets == 8:	# If is combination with ) before sign, insert it
									expr6 += ")"
									if brackets == 6:
										expr6 += ")"
								expr6 += signs[sign3]
								numberRange4 = copy.deepcopy (numberRange)		# To numberRange3 copy numberRange without number1, number2, number3 index

								numberRange4.remove (number1)
								numberRange4.remove (number2)
								numberRange4.remove (number3)
								for number4 in numberRange4:		# To result string (expr7) insert last sign, for is useless
									expr7 = expr6
									expr7 += str (origList[number4])
									if brackets == 1 or brackets == 2 or brackets == 7 or brackets == 8 or brackets == 9:		# If is combination with ) after sign, insert it
										expr7 += ")"
										if brackets == 9:
											expr7 += ")"
									allComb.append (expr7)		# Result combination
	resultComb = []
	for expr in allComb:		# To resultComb (which is returned) save just combination of expressinon which are equal result and are not with zero division
		try:
			exprResult = eval (expr)
		except ZeroDivisionError:
			continue
		if exprResult == result:
			resultComb.append (expr)
	if len (resultComb) != 0:
		return resultComb


