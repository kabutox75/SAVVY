import csv
from nupic.encoders.category import CategoryEncoder

def main():
	readFile()
	
def readFile():
	with open('categoryValues.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			encodeCategoryValue(row[0])
	
def encodeCategoryValue(value):
	categoryEncoder = CategoryEncoder(23, ['art', 'tiger', 'lion', 'leopard', 'cheetah', 'puma', 'cat2' ,'monkey'])
	encodedValue = categoryEncoder.encode(value)
	print "Encoding of " + value + ": "
	print encodedValue
	print "\n"	
	
	
	
if __name__ == "__main__": main()