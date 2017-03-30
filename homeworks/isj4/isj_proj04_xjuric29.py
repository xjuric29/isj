#!/usr/bin/env python3

def balanced_paren (parenstr):
	brackets = []
	lenght = len (parenstr)
	count = 1
	for char in parenstr:
		if char in "([{<":
			brackets.append (char)
		if char in "]}>":
			if count <= lenght and ord (brackets[-count]) == (ord (char) - 2):
				count += 1
			else:
				return False
		if char == ')':
                        if count <= lenght and ord (brackets[-count]) == (ord (char) - 1):
                                count += 1
                        else:
                                return False
	return True;

def caesar_list (word, key):
	pass

def caesar_varnumkey (key):
	pass

#print (balanced_paren ("{1<2(>3)}"))
