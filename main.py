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


print 'CallidusCloud Data Import Tool Copyright 2018'
print ''
fileLoc = raw_input("Please enter the location of the file: ")
fileName = raw_input("Please enter the name of the file: ")

def readMyFile(filename):
    fullFilePath = fileLoc + fileName
    if '.csv' in fileName:
        col1 = []
        col2 = []
        col3 = []
        row = 0

        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            #ncol = len(next(csvReader))
            #nrow = sum(1 for row in csvDataFile)
            #print 'ncol',ncol
            #print 'nrow',nrow
            try:
                for row in csvReader:
                    print ','.join(row)
            except csv.Error as e:
                    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


        print 'Opening file...', fullFilePath

        return col1, col2, col3
    else:
        return 'Only accept .CSV for this release'




fullFilePath = fileLoc+fileName
#fullFilePath = 'c:\est.csv'


print 'Opening file...',fullFilePath

col1, col2, col3 = readMyFile(fullFilePath)

print(col1)
print(col2)
print(col3)

  