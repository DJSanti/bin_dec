###############################################################################
# Name: Samantha Santiago
# Date: 03/19/2018
# Objective: Mathematically implement a Vigenere cipher to encrypt and decrypt
# messages
###############################################################################

#imports ascii letters and sys commands
import sys
from string import ascii_uppercase, ascii_lowercase

# creates list of letters
alphabet = ascii_uppercase + ascii_lowercase 

# testing out some of the math here...
# i = 7
# print ord(alphabet[(i + 52) % 52])
# print chr(ord(alphabet[(i + 52) % 52]))

# encryption function
def encrypt(text, key):
	ciphertext = ''
	key_len = len(key)
	key_int = [ord(x) for x in key]
	text_int = [ord(x) for x in text]
	for i in text:
		if not i in alphabet:
			ciphertext += i
		elif i.isalpha():
			ciphertext += 'e'
	return ciphertext

# decryption function	
def decrypt(text, key):
	plaintext = ''
	key_len= len(key)
	key_int = [ord(i) for i in key]
	text_int = [ord(i) for i in text]
	for i in text:
		if not i in alphabet:
			plaintext += i
		elif i.isalpha():
			plaintext += 'd'
	return plaintext

# Main function - executed once program is started	
def Main():
	# main function
	while True:
		# error handling to make sure whole argument is typed in
		if (len(sys.argv) == 3):
			text = sys.stdin.readline()
			for i in range(2, len(sys.argv)):
				if not text:
					exit()
				if (sys.argv[1] == "-e"):
					key = sys.argv[i]
					print encrypt(text, key)
				elif (sys.argv[1] == "-d"):
					key = sys.argv[i]
					print decrypt(text, key)
				else:
					print "error: unknown option"
		else:
			print "Error. Try again."
			exit()
		
Main()
