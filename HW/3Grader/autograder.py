from autograder2 import AutoGrader
from autogradersettings import *
import os
import sys

def getOrNone(array, index):
	if len(array) > index:
		return array[index]
	return None

def main():
	args = sys.argv

	filePath = getOrNone(args, 1)

	auto = AutoGrader()
	grade = auto.runAutoGrader(filePath)

	print "Grade:", grade

if __name__ == "__main__":
	main()
