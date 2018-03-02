import csv
from datetime import datetime
from nupic.encoders.date import DateEncoder

def main():
	readFile()
	
def readFile():
	with open('dateValues.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			encodeDateValue(row[0])
	
def encodeDateValue(value):
	dateEncoder = DateEncoder(season=11)
	dateTimeValue = datetime.strptime(value, "%m/%d/%Y %H:%M")
	encodedValue = dateEncoder.encode(dateTimeValue)
	print "Encoding of " + value + ": "
	print encodedValue
	print "\n"	
	
if __name__ == "__main__": main()