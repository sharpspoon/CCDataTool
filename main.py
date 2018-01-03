import csv
import _random
def readMyFile(filename):
    dates = []
    scores = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            dates.append(row[0])
            scores.append(row[1])
            print csvDataFile

    return dates, scores


dates, scores = readMyFile('c:\est.csv')
text = raw_input("prompt")
print text
print(dates)
print(scores)

  