#!/usr/bin/env python3

import string

def balanced_paren (parenstr):
	"""Check if in string are correctly us parentheses"""
	stack = []
	brackets = { ')':'(', ']':'[', '}':'{', '>':'<'}
	length = len (parenstr)
	for char in parenstr:
		if char in "([{<":		# If char is beginnig brackets store it in stack
			stack.append (char)
		if char in ")]}>":
			if stack != [] and stack[-1] == brackets[char]:		# Exclusion falls like ")" or "{)"
				stack = stack[:-1]
			else:
				return False
	if stack == []:		# Exclusion falls like "("
		return True
	else:
		return False

def caesar_list (word, key = [1, 2, 3]):
	"""Return Ceasar cipher from word shifted by values in list"""
	alphabet = list (string.ascii_lowercase)
	for char in word:		# Check if all chars from word are in ascii lowercase alphabet
		if char not in alphabet:
			raise ValueError
	newWord = ""
	count = 0
	keyLength = len (key)
	for char in word:
		newWord += alphabet[(alphabet.index (char) + key[count % keyLength]) % 26]		# To string newchar (in first cycle blank) append shift char from alphabet
		count += 1
	return newWord

def caesar_varnumkey (word, *argv):
	"""Return Ceasar cipher from word shifted by values in args"""
	if argv == ():
		return caesar_list (word)
	else:
		key = []
		for arg in argv:
			key.append (arg)
		return caesar_list (word, key)
