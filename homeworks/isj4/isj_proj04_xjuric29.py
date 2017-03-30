#!/usr/bin/env python3

import string

def balanced_paren (parenstr):
	tmp = []
	brackets = { ')':'(', ']':'[', '}':'{', '>':'<'}
	length = len (parenstr)
	for char in parenstr:
		if char in "([{<":		# If char is beginnig brackets store it in tmp
			tmp.append (char)
		if char in ")]}>":
			if tmp != [] and tmp[-1] == brackets[char]:		
				tmp = tmp[:-1]
			else:
				return False
	if tmp == []:
		return True
	else:
		return False

def caesar_list (word, key = [1, 2, 3]):
	alphabet = list (string.ascii_lowercase)
	for char in word:		# Check if all chars from word are in ascii lowercse alphabet
		if char not in alphabet:
			raise ValueError
	newWord = ""
	count = 0
	keyLength = len (key)
	for char in word:
		newWord += alphabet[(alphabet.index (char) + key[count % keyLength]) % 26]		# To string newchar (in first cycle blank) append shift char from alphabet
		count += 1
	return newWord

def caesar_varnumkey (key):
	pass

print (balanced_paren ("{("))
#caesar_list ("")
