from pathlib import Path
import csv

"""
Input a filename and open if existing. Return the filename and file pointer
"""

def getFile():
    while True:
        filename=input("Type the filename ")
        my_file = Path(filename)
        if my_file.exists():
            break
        else:
            print(filename + " is not existing.\n Input the file again ")
            continue
        
    datafile = open(filename,"r")
    return filename, datafile

# Get the filename and file pointer
fname, fpointer = getFile();

# Read the first line of the file to get the column headers
header = fpointer.readline();
# Split the header separated by "," and get the list of column labels
columns = header.split(",")

minNum = [1000000, 1000000, 1000000]
maxNum = [0, 0, 0]
mean = [0, 0, 0]
reader = csv.reader(fpointer, delimiter=",")
for line in reader:
    line[1] = float(line[1])
    line[2] = float(line[2])
    line[3] = float(line[3])
    if line[1] < minNum[0]:
        minNum[0] = line[1]
    if line[2] < minNum[1]:
        minNum[1] = line[2]
    if line[3] < minNum[2]:
        minNum[2] = line[3]
    if line[1] > maxNum[0]:
        maxNum[0] = line[1]
    if line[2] > maxNum[1]:
        maxNum[1] = line[2]
    if line[3] > maxNum[2]:
        maxNum[2] = line[3]
    mean[0] += line[1]
    mean[1] += line[2]
    mean[2] += line[3]

mean[0] /= 100
mean[1] /= 100
mean[2] /= 100

data = ["Loyalty", "Usage", "AgeGrouo"]

colName = ["", "Minimum", "Mean", "Maximum"]

print("{:<10} {:<9} {:<7} {:<10}".format("  ", "Minimum", "Mean", "Maximum"))
i = 0
ctr = 3
for i in range(3):
    print("{:<10} {:<9.2f} {:<7.2f} {:<10.2f}".format(data[i], minNum[i], mean[i], maxNum[i]))


