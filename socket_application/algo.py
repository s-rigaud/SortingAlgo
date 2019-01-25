import time, random
from functions import *

def bubble_sort(nList):
	array_step_by_step = []
	for num in range(len(nList)-1,0,-1):
		for i in range(num):
			if nList[i]>nList[i+1]:
				nList[i],nList[i+1] = nList[i+1],nList[i]
				array_step_by_step.append(str(i)+"-"+str(i+1))
	return array_step_by_step


def optimised_bubble_bort(nList):
	array_step_by_step = []
	for num in range(len(nList)-1,0,-1):
		ordered = True
		for i in range(num):
			if nList[i]>nList[i+1]:
				nList[i],nList[i+1] = nList[i+1],nList[i]
				ordered = False
				array_step_by_step.append(str(i)+"-"+str(i+1))
		if ordered :
			break
	return array_step_by_step


def cocktail_sort(nList):
	array_step_by_step = []
	for k in range(len(nList)-1, 0, -1):
		swapped = False
		for i in range(k, 0, -1):
			if nList[i]<nList[i-1]:
				nList[i], nList[i-1] = nList[i-1], nList[i]
				array_step_by_step.append(str(i)+"-"+str(i-1))
				swapped = True
		for i in range(k):
			if nList[i] > nList[i+1]:
				nList[i], nList[i+1] = nList[i+1], nList[i]
				array_step_by_step.append(str(i)+"-"+str(i+1))
				swapped = True
		if not swapped:
			return array_step_by_step
	

def selection_sort(nList):
	array_step_by_step = []
	for i in range(len(nList)-1,0,-1):
		indexMax=0
		for location in range(1,i+1):
			if nList[location]>nList[indexMax]:
				indexMax = location
		nList[i],nList[indexMax] = nList[indexMax],nList[i]
		array_step_by_step.append(str(i)+"-"+str(indexMax))
	return array_step_by_step


def insertion_sort(nList):
	array_step_by_step = []
	for i in range(1,len(nList)):
		currentvalue = nList[i]
		position = i
		while position>0 and nList[position-1]>currentvalue:
			nList[position]=nList[position-1]
			array_step_by_step.append(str(position)+"-"+str(position-1))
			position = position-1
		nList[position]=currentvalue
		
	return array_step_by_step


def merge_sort(nList):
	pass

def radix_sort(nList):
	pass

def bucket_sort(nList):
	array_step_by_step = []
	# creating around (x<=10) buckets each time
	# seems better for visualisation
	bucketSize = 10**(len(str(max(nList)))-1)
	
	buckets =[[] for _ in range(max(nList)//bucketSize+1)]
	for i in range(len(nList)):
		bucketVoulu = buckets[int(nList[i]//bucketSize)]
		bucketVoulu.append(nList[i])

	bigBucket = []
	for bucket in buckets:
		bigBucket += [number for number in bucket]

	######################################################################""
	#Begin to end Visualisation
	bigBucketCopy = bigBucket.copy()
	nListCopy = nList.copy() 
	for num in bigBucketCopy:
		idxNList = nList.index(num)
		idxBB = bigBucket.index(num)
		array_step_by_step.append(str(idxNList)+'-'+str(idxBB))
		nList[idxNList]=0
		bigBucket[idxBB]=0
		nList[idxBB],nList[idxNList] = nList[idxNList],nList[idxBB]
	###############################################################################""

	res = []
	cpt = 0
	for bucket in buckets:
		insertion_sort(bucket)
		res+=bucket
	######################################################################""
	#Begin to end Visualisation

	bigBucketCopyCopy = bigBucketCopy.copy()
	resCopy = res.copy()

	for num in bigBucketCopyCopy:
		idxBB = bigBucketCopy.index(num)
		idxRes = res.index(num)
		array_step_by_step.append(str(idxBB)+'-'+str(idxRes))
		bigBucketCopy[idxBB]=0
		res[idxRes]=0
		bigBucketCopy[idxRes],bigBucketCopy[idxBB] = bigBucketCopy[idxBB],bigBucketCopy[idxRes]
	###############################################################################""

	print(nList)
	print(resCopy)

	nList = resCopy.copy()

	print(nList)
	print(resCopy)
	return array_step_by_step


def counting_sort(nList):
	array_step_by_step = []
	count = [0 for _ in range(max(nList)+1)]
	res = []

	for num in nList:
		count[num]+=1

	for i in range(len(count)):
		res+= [i for j in range(count[i])]
	######################################################################""
	#Begin to end Visualisation
	resCopy = res.copy()
	nListCopy = nList.copy() 
	for num in nListCopy:
		idxNList = nList.index(num)
		idxRes = res.index(num)
		array_step_by_step.append(str(idxNList)+'-'+str(idxRes))
		nList[idxNList]=0
		res[idxRes]=0
		nList[idxRes],nList[idxNList] = nList[idxNList],nList[idxRes]
	###############################################################################""

	print(nList)
	print(resCopy)

	nList = resCopy.copy()

	print(nList)
	print(resCopy)
	return array_step_by_step


def smooth_sort(nList):
	pass


def heap_sort(nList):
	pass

def quick_sort(nList):
	pass

def bogo_sort(nList):
	array_step_by_step = []
	size = len(nList)
	orderedList = sorted(nList.copy())
	while(not(areEqual(nList,orderedList))):
		randomNum0 = random.randint(0,size-1)
		randomNum1 = random.randint(0,size-1)
		nList[randomNum0],nList[randomNum1] = nList[randomNum1],nList[randomNum0]
		array_step_by_step.append(str(randomNum0)+"-"+str(randomNum1))
	return array_step_by_step