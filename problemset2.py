from utils import *

print("Start!")
data = loadAndCleanData("creditData.csv")
computePDF("MonthlyIncome",data)
for row in data:
	viewDistribution(row, data)
	viewLogDistribution(row, data)
	bins = computeBins(row, data)
	for bin in bins:
		print(row, bin)
		computeDefaultRisk("SeriousDlqin2yrs",[bin.left,bin.right],row,data)
	#predictDefaultRisk(data, row) Can't figure this one out
viewDistribution("MonthlyIncome",data)



print("Done!")