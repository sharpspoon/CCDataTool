import csv
import random
import glob



fileLoc = raw_input("Please enter the location of the file: ")
fileName = raw_input("Please enter the name of the file: ")

def readMyFile(filename):
    fullFilePath = fileLoc + fileName
    if '.csv' in fileName:
        dates = []
        scores = []
        row = 0

        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                dates.append(row[0])
                scores.append(row[1])
            for col in row:
                print 1
        print 'Opening file...', fullFilePath

        return dates, scores
    else:
        dates = 'Error code: '
        scores = 'only accept .csv at this time'
        return dates, scores




fullFilePath = fileLoc+fileName
#fullFilePath = 'c:\est.csv'


print 'Opening file...',fullFilePath

dates, scores = readMyFile(fullFilePath)

print(dates)
print(scores)

  