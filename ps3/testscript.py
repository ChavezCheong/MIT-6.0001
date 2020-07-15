def checksum(inputlist, num):
    lastindex = len(inputlist)
    runningcounter = 0
    while runningcounter != lastindex:
        for i in range(runningcounter + 1, lastindex):
            if inputlist[runningcounter] + inputlist[i] == num:
                return True
        runningcounter += 1
    return False

def fasterchecksum(inputlist, num):
    sortedlist = sorted(inputlist)
    firstindex = 0
    secondindex = len(inputlist) - 1
    while firstindex != secondindex:
        if sortedlist[firstindex] + sortedlist[secondindex] > num:
            secondindex -= 1
        elif sortedlist[firstindex] + sortedlist[secondindex] < num:
            firstindex += 1
        else:
            return True
    return False

testlist = [1,2,3,7,9]

print(fasterchecksum(testlist, 10))