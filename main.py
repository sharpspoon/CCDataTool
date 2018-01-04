#import csv
#import random
#import glob


#print 'CallidusCloud Data Import Tool Copyright 2018'
#print ''
#fileLoc = raw_input("Please enter the location of the file: ")
#fileName = raw_input("Please enter the name of the file: ")

#def readMyFile(fileName):
#    fullFilePath = fileLoc + fileName
#    if '.csv' in fileName:
#        csvArray = []
#        row = 0

#        with open(fileName) as csvDataFile:
#            csvReader = csv.reader(csvDataFile)
#            ncol = len(next(csvReader))
#            nrow = sum(1 for row in csvDataFile)
#            print 'ncol',ncol
#            print 'nrow',nrow
#            for row in csvReader:
#                csvArray.append(row[nrow])
#                nrow = nrow-1
#                #csvArray.append(row[1])
#        print 'Opening file...', fullFilePath

#        return csvArray
#    else:

#        return csvArray




#fullFilePath = fileLoc+fileName
##fullFilePath = 'c:\est.csv'


#print 'Opening file...',fullFilePath

#csvArray = readMyFile(fullFilePath)

#print(csvArray)

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




#fulleFilePath = fileLoc+fileName
fullFilePath = 'c:\est.csv'


print 'Opening file...',fullFilePath

dates, scores = readMyFile(fullFilePath)

print(dates)
print(scores)

  