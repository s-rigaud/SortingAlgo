import time
import random
from functions import *

def bubbleSort(nList):
	arrayStepByStep = []
	for num in range(len(nList)-1,0,-1):
		for i in range(num):
			if nList[i]>nList[i+1]:
				nList[i],nList[i+1] = nList[i+1],nList[i]
				arrayStepByStep.append(str(i)+"→"+str(i+1))
	return arrayStepByStep


def optimisedBubbleSort(nList):
	arrayStepByStep = []
	for num in range(len(nList)-1,0,-1):
		ordered = True
		for i in range(num):
			if nList[i]>nList[i+1]:
				nList[i],nList[i+1] = nList[i+1],nList[i]
				ordered = False
				arrayStepByStep.append(str(i)+"→"+str(i+1))
		if ordered :
			break
	return arrayStepByStep


def cocktailSort(nList):
	arrayStepByStep = []
	for k in range(len(nList)-1, 0, -1):
		swapped = False
		for i in range(k, 0, -1):
			if nList[i]<nList[i-1]:
				nList[i], nList[i-1] = nList[i-1], nList[i]
				arrayStepByStep.append(str(i)+"→"+str(i-1))
				swapped = True
		for i in range(k):
			if nList[i] > nList[i+1]:
				nList[i], nList[i+1] = nList[i+1], nList[i]
				arrayStepByStep.append(str(i)+"→"+str(i+1))
				swapped = True
		if not swapped:
			return arrayStepByStep
	

def selectionSort(nList):
	arrayStepByStep = []
	for i in range(len(nList)-1,0,-1):
		indexMax=0
		for location in range(1,i+1):
			if nList[location]>nList[indexMax]:
				indexMax = location
		nList[i],nList[indexMax] = nList[indexMax],nList[i]
		arrayStepByStep.append(str(i)+"→"+str(indexMax))
	return arrayStepByStep


def insertionSort(nList):
	arrayStepByStep = []
	for i in range(1,len(nList)):
		currentvalue = nList[i]
		position = i
		while position>0 and nList[position-1]>currentvalue:
			nList[position]=nList[position-1]
			arrayStepByStep.append(str(position)+"→"+str(position-1))
			position = position-1
		nList[position]=currentvalue
		
	return arrayStepByStep


def mergeSort(nList):
	pass

def radixSort(nList):
	pass

def bucketSort(nList):
	arrayStepByStep = []
	# creating around (x<=10) buckets each time
	# seems better for visualisation
	bucketSize = 10**(len(str(max(nList)))-1)
	
	buckets =[[] for _ in range(max(nList)//bucketSize+1)]
	for i in range(len(nList)):
		bucketVoulu = buckets[int(nList[i]//bucketSize)]
		bucketVoulu.append(nList[i])
		
	bigBucket = []
	for bucket in buckets:
		bigBucket+=bucket

	######################################################################""
	#Begin to end Visualisation
	bigBucketCopy = bigBucket.copy()
	nListCopy = nList.copy() 
	for num in bigBucketCopy:
		idxNList = nList.index(num)
		idxBB = bigBucket.index(num)
		arrayStepByStep.append(str(idxNList)+'→'+str(idxBB))
		nList[idxNList]=0
		bigBucket[idxBB]=0
		nList[idxBB],nList[idxNList] = nList[idxNList],nList[idxBB]
	###############################################################################""

	res = []
	cpt = 0
	for bucket in buckets:
		insertionSort(bucket)
		res+=bucket
	######################################################################""
	#Begin to end Visualisation

	bigBucketCopyCopy = bigBucketCopy.copy()
	resCopy = res.copy()

	for num in bigBucketCopyCopy:
		idxBB = bigBucketCopy.index(num)
		idxRes = res.index(num)
		arrayStepByStep.append(str(idxBB)+'→'+str(idxRes))
		bigBucketCopy[idxBB]=0
		res[idxRes]=0
		bigBucketCopy[idxRes],bigBucketCopy[idxBB] = bigBucketCopy[idxBB],bigBucketCopy[idxRes]
	###############################################################################""

	fillArrayWithArray(nList,resCopy)
	return arrayStepByStep


def countingSort(nList):
	arrayStepByStep = []
	count = [0 for _ in range(max(nList)+1)]
	res = []

	for num in nList:
		count[num]+=1

	for i in range(len(count)):
		for j in range(count[i]):
			res.append(i)
	######################################################################""
	#Begin to end Visualisation
	resCopy = res.copy()
	nListCopy = nList.copy() 
	for num in nListCopy:
		idxNList = nList.index(num)
		idxRes = res.index(num)
		arrayStepByStep.append(str(idxNList)+'→'+str(idxRes))
		nList[idxNList]=0
		res[idxRes]=0
		nList[idxRes],nList[idxNList] = nList[idxNList],nList[idxRes]
	###############################################################################""

	fillArrayWithArray(nList,resCopy)
	return arrayStepByStep


def smoothSort(nList):
	pass


def heapSort(nList):
	pass

def quickSort(nList):
	pass

def bogoSort(nList):
	arrayStepByStep = []
	size = len(nList)
	orderedList = sorted(nList.copy())
	while(not(areEqual(nList,orderedList))):
		randomNum0 = random.randint(0,size-1)
		randomNum1 = random.randint(0,size-1)
		nList[randomNum0],nList[randomNum1] = nList[randomNum1],nList[randomNum0]
		arrayStepByStep.append(str(randomNum0)+"→"+str(randomNum1))
	return arrayStepByStep
