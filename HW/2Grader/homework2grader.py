# USAGE:
# extract "bulk_downloads.zip", make sure root directory, "grades.csv" file, and this script are in root of "bulk_downloads" folder

import csv, sys, os, random, traceback
from timeoutfunction import TimeoutFunction, TimeoutFunctionException

from autograder2 import AutoGrader
from autogradersettings import *

gradesCSVPath = os.path.join(root, "grades.csv")
source = open(gradesCSVPath, "rb")
reader = csv.reader(source)
auto = AutoGrader()

gradedCSVPath = os.path.join(root, "graded.csv")
open(gradedCSVPath, "wb").close()

row_index = 0

ERRORGRADE = "ERROR"
TIMEOUTGRADE = "TIMEOUT"

submissions = {}
for dirName, subdirs, files in os.walk(root):
	for subdir in subdirs:
		student = subdir
		truncateIndex = subdir.find('(')
		if truncateIndex > 0:
			student = subdir[0:truncateIndex]
		submissions[student] = subdir
	break

for row in reader:
	columns = row
	output = ""
	if row_index > 2:
		student_index = row_index - 3

		# extract the goods
		gtid = columns[0]
		t2id = columns[1]
		last_name = columns[2]
		first_name = columns[3]
		grade = columns[4]
		
		student_path = ""
		student_dir = ""
		file_path = ""

		# walk to ".\root\student_name\Submission attachment(s)" based on student name
		student_dir = submissions[last_name + "," + first_name]
		student_path = os.path.join(root, student_dir, "Submission attachment(s)")
		print("Student: "+student_path)

		# try to find the path of the student's submitted file
		for dirName, subdirs, files in os.walk(student_path):
			if len(files) >0:
				# this is where the submitted file is
				file_path = os.path.join(student_path, files[0])
				print("File path: "+file_path)

				#################################
				# run autograder, assign grade
				if disablePrint:
					saveOut = sys.stdout
					f = open(os.devnull, 'w')
					sys.stdout = f

				try:
					if timeout:
						grade = TimeoutFunction(auto.runAutoGrader, timeout)(student_path)
					else:
						grade = auto.runAutoGrader(student_path)
					grade = ("" + str(round(grade, 1)))
				except TimeoutFunctionException:
					grade = TIMEOUTGRADE
				except:
					grade = ERRORGRADE
					
				if disablePrint:
					sys.stdout = saveOut

				if grade == ERRORGRADE:
					print "Error in submission."
					traceback.print_exc()
				elif grade == TIMEOUTGRADE:
					print "Submission timed out."

				auto = AutoGrader()
			elif len(files) == 0:
				# no submission?
				grade = "0"
			break

		# output grade
		print "Grade: " + grade
		columns[4] = str(grade)
	
	with open(gradedCSVPath, "ab") as gradeFile:
		writer = csv.writer(gradeFile)
		writer.writerow(columns)
	row_index += 1

source.close()