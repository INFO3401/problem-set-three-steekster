import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def loadAndCleanData (file):
	df = pd.read_csv(file)
	df.fillna(value=0, inplace = True)
	return df
	
def computePDF(feature,dataset):
	dataset[feature].plot.kde()
	plt.show()

def viewDistribution(column,dataset):
	dataset[column].hist()
	plt.show()
	
def viewLogDistribution(column,dataset):
	ax = dataset[column].hist(log = True)
	plt.show()

def computeBins(column, dataset):
	dfcut = pd.qcut(dataset[column],q = 3, duplicates = 'drop')
	catList = dfcut.cat.categories.tolist()
	return catList

def computeDefaultRisk(column, bin, feature, df):
	df = df[(df[feature] >= bin[0]) & (df[feature] <= bin[1])]
	rating_probs = df.groupby(column).size().div(len(df))
	print(rating_probs)
	
def predictDefaultRisk(df,column):
	rating_probs = df.groupby(column).size().div(len(df))
	print("test",rating_probs)
	
	
		
