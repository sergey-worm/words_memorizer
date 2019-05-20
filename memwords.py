#!/usr/bin/python3

import sys
import os
import random
import re

OK = 0
WRONG = 0

class colors:
	endc   = '\033[0m'
	green  = '\033[92m'
	red    = '\033[91m'
	blue   = '\033[94m'
	yellow = '\033[93m'

# view:  "w1,w2,w3,...: t1,t2,t3,..."
def process_line(line):
	substrs = re.split(':', line)
	# ask one word from left/right and expect answer from right/left
	ask_substr = random.randint(0, 1)
	words_ask = re.split(',', substrs[ask_substr])
	words_exp = re.split(',', substrs[not ask_substr])
	words_ask = [item.strip() for item in words_ask]
	words_exp = [item.strip() for item in words_exp]
	# ask
	a = random.randint(0, len(words_ask)-1)
	print("ask    |  {}".format(words_ask[a]))
	for i in range(0, 3):
		print("answer |  ".format(words_ask[a]), end="")
		answer = input()
		# check answer
		if answer in words_exp:
			global OK
			OK += 1
			print("       |", colors.green, "ok - {}".format(OK), colors.endc)
			break
		if answer == 'q':
			print("       |", colors.blue, "exit", colors.endc)
			sys.exit()
		else:
			global WRONG
			WRONG += 1
			print("       |", colors.yellow, "wrong - {}".format(WRONG), colors.endc)
			if i == 2:
				print("       |", colors.red, "failed:  {}".format(words_exp), colors.endc)
	print("-------+------------------------------")

def main():
	filepath = sys.argv[1]

	if not os.path.isfile(filepath):
		print("File path {} does not exist. Exiting.".format(filepath))
		sys.exit()

	with open(filepath) as fp:
		lines = fp.readlines()
		while True:
			l = random.randint(0, len(lines)-1)
			line = lines[l].rstrip('\n')
			if not line or line[0]=='#':
				continue
			process_line(line)

if __name__ == '__main__':
	main()
