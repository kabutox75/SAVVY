import csv
from nupic.encoders.scalar import ScalarEncoder

def main():
	readFile()
	
def readFile():
	with open('scalarValues.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			encodeScalarValue(row[0])
	
def encodeScalarValue(value):
	scalarEncoder = ScalarEncoder(551, 1.0, 5.5, resolution=1)
	encodedValue = scalarEncoder.encode(float(value))
	print "Encoding of " + value + ": "
	print encodedValue
	print "\n"	
	
	
	
if __name__ == "__main__": main()