###############################################################################
# Name: Samantha Santiago
# Date: 03/19/2018
# Objective: Mathematically implement a Vigenere cipher to encrypt and decrypt
# messages
###############################################################################

#imports ascii letters and sys commands
import sys

# encryption function
def encrypt(text, key):
	ciphertext = ""
	on_letter = 0
	value = 0
	key_len = len(key)
	
	for i in range(0,len(text)):
		if on_letter == key_len:
			on_letter = 0
		if text[i].isalpha():
			if text[i] >= 'a' and text[i] <= 'z':
				value = 97
			elif text[i] >= 'A' and text[i] <= 'Z':
				value = 65
			
			plain_num = ord(text[i]) - value
			
			shift = ord(key[on_letter]) - 97
			
			new_letter_num = plain_num + shift
			
			if new_letter_num > 25:
				new_letter_num = new_letter_num % 26
			
			new_letter_num += value
			
			new_letter = chr(new_letter_num)
			
			ciphertext += new_letter
			
			on_letter += 1
		else:
			ciphertext += text[i]
		
	return ciphertext

# decryption function	
def decrypt(text, key):
	plaintext = ""
	on_letter = 0
	value = 0
	key_len = len(key)
	
	for i in range(0,len(text)):
		if on_letter == key_len:
			on_letter = 0
		if text[i].isalpha():
			if text[i] >= 'a' and text[i] <= 'z':
				value = 97
			elif text[i] >= 'A' and text[i] <= 'Z':
				value = 65
			
			plain_num = ord(text[i]) - value
			
			shift = ord(key[on_letter]) - 97
			
			new_letter_num = (plain_num - shift) + 26
			
			if new_letter_num > 25:
				new_letter_num = new_letter_num % 26
			
			new_letter_num += value
			
			new_letter = chr(new_letter_num)
			
			plaintext += new_letter
			
			on_letter += 1
		else:
			plaintext += text[i]
	return plaintext

# Main function - executed once program is started	
def Main():
	while True: # need this to CTRL-D the fuck out
		# error handling: catches if something went wrong
		if (len(sys.argv) == 3):
			text = sys.stdin.readline() 
			for i in range(2, len(sys.argv)):
				if text == "\n": # catches if only enter was hit; keeps coming up on last test
					print "Error: no input entered. Exiting now..."
					exit()
				if (sys.argv[1] == "-e"):
					key = ''.join(sys.argv[i].lower().replace(" ", ""))
					print encrypt(text, key).rstrip()
				elif (sys.argv[1] == "-d"):
					key = ''.join(sys.argv[i].lower().replace(" ", ""))
					print decrypt(text, key).rstrip()
				else:
					print "Error: unknown option. Exiting now..." # works; thank GOD
					exit()
		else:
			print "Error. Try again by typing your command as follows: python vigenere.py [-d/-e] [key]" # general error handling works
			exit()
		
Main()
