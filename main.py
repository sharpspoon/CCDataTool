import csv
import _random


fileLoc = raw_input("Please enter the location of the file: ")
fileName = raw_input("Please enter the name of the file: ")
print fileLoc
print fileName

def readMyFile(filename):
	
    dates = []
    scores = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            dates.append(row[0])
            scores.append(row[1])
            #print csvDataFile

    return dates, scores



fulleFilePath = fileLoc+fileName
print 'full file path=',fulleFilePath

dates, scores = readMyFile(fulleFilePath)

print(dates)
print(scores)

  