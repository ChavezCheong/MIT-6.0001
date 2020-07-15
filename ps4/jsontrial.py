import requests
import json
from decimal import Decimal

#API Call
resp = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=96e66346-68bb-4ca9-b001-58bbf39e36a7")
rawdata = resp.json()
data = []


def max_temp(inputlist, year):
    temperatures = []
    for sublist in inputlist:
        if sublist[0] == str(year):
            temperatures.append(sublist[1])
    return max(temperatures)

for row in rawdata["result"]["records"]:
    datarow = []
    year = row["month"][0:4]
    temperature = Decimal(row["max_temperature"])
    datarow.append(year)
    datarow.append(temperature)
    data.append(datarow)

print(data)


yearcount = set([])
for sublist in data:
    yearcount.add(sublist[0])

onlymax = []
for year in yearcount:
    onlymaxrow= []
    onlymaxrow.append(year)
    onlymaxrow.append(max_temp(data, year))
    onlymax.append(onlymaxrow)

onlymax.sort(key = lambda x: x[1])

finaldata= []
search1 = 1982
search2 = 1998

for item in data:
    if item[0] in range(search1, search2):
        print(item[0])
        finaldata.append(item)

data = finaldata


