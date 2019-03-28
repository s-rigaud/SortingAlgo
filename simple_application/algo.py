import time, random
from functions import *

def bubble_sort(nList):
	array_steps = []
	for num in range(len(nList)-1,0,-1):
		for i in range(num):
			if nList[i]>nList[i+1]:
				nList[i],nList[i+1] = nList[i+1],nList[i]
				array_steps.append(str(i)+"-"+str(i+1))
	return array_steps


def optimised_bubble_bort(nList):
	array_steps = []
	for num in range(len(nList)-1,0,-1):
		ordered = True
		for i in range(num):
			if nList[i]>nList[i+1]:
				nList[i],nList[i+1] = nList[i+1],nList[i]
				ordered = False
				array_steps.append(str(i)+"-"+str(i+1))
		if ordered :
			break
	return array_steps


def cocktail_sort(nList):
	array_steps = []
	for k in range(len(nList)-1, 0, -1):
		swapped = False
		for i in range(k, 0, -1):
			if nList[i]<nList[i-1]:
				nList[i], nList[i-1] = nList[i-1], nList[i]
				array_steps.append(str(i)+"-"+str(i-1))
				swapped = True
		for i in range(k):
			if nList[i] > nList[i+1]:
				nList[i], nList[i+1] = nList[i+1], nList[i]
				array_steps.append(str(i)+"-"+str(i+1))
				swapped = True
		if not swapped:
			return array_steps
	

def selection_sort(nList):
	array_steps = []
	for i in range(len(nList)-1,0,-1):
		indexMax=0
		for location in range(1,i+1):
			if nList[location]>nList[indexMax]:
				indexMax = location
		nList[i],nList[indexMax] = nList[indexMax],nList[i]
		array_steps.append(str(i)+"-"+str(indexMax))
	return array_steps


def insertion_sort(nList):
	array_steps = []
	for i in range(1,len(nList)):
		currentvalue = nList[i]
		position = i
		while position>0 and nList[position-1]>currentvalue:
			nList[position]=nList[position-1]
			array_steps.append(str(position)+"-"+str(position-1))
			position = position-1
		nList[position]=currentvalue
		
	return array_steps


def merge_sort(nList):
	pass

def radix_sort(nList):
	pass

def bucket_sort(nList):
	array_steps = []
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

	#Making transition between starting position and pseudo-sorted array in buckets
	bigBucketCopy = bigBucket[:]
	nListCopy = nList[:]
	for num in bigBucketCopy:
		idxNList = nList.index(num)
		idxBB = bigBucket.index(num)
		array_steps.append(str(idxNList)+'-'+str(idxBB))
		nList[idxNList]=0
		bigBucket[idxBB]=0
		nList[idxBB],nList[idxNList] = nList[idxNList],nList[idxBB]

	res = []
	cpt = 0
	for bucket in buckets:
		insertion_sort(bucket)
		res+=bucket

	#Making transition between not sorted and sorted array
	bigBucketCopyCopy = bigBucketCopy[:]
	resCopy = res[:]

	for num in bigBucketCopyCopy:
		idxBB = bigBucketCopy.index(num)
		idxRes = res.index(num)
		array_steps.append(str(idxBB)+'-'+str(idxRes))
		bigBucketCopy[idxBB]=0
		res[idxRes]=0
		bigBucketCopy[idxRes],bigBucketCopy[idxBB] = bigBucketCopy[idxBB],bigBucketCopy[idxRes]

	nList = resCopy[:]

	return array_steps


def counting_sort(nList):
	array_steps = []
	count = [0 for _ in range(max(nList)+1)]
	res = []

	for num in nList:
		count[num]+=1

	for i in range(len(count)):
		res+= [i for j in range(count[i])]
	
	#Making transition between not sorted and sorted array
	resCopy = res[:]
	nListCopy = nList[:]
	for num in nListCopy:
		idxNList = nList.index(num)
		idxRes = res.index(num)
		array_steps.append(str(idxNList)+'-'+str(idxRes))
		nList[idxNList]=0
		res[idxRes]=0
		nList[idxRes],nList[idxNList] = nList[idxNList],nList[idxRes]

	nList = resCopy[:]

	return array_steps


def smooth_sort(nList):
	pass


def heap_sort(nList):
	pass

def quick_sort(nList):
	pass

def bogo_sort(nList):
	"""Mixing until it's randomly sorted"""
	array_steps = []
	size = len(nList)
	orderedList = sorted(nList[:])
	while not areEqual(nList,orderedList) :
		randomNum0 = random.randint(0,size-1)
		randomNum1 = random.randint(0,size-1)
		nList[randomNum0],nList[randomNum1] = nList[randomNum1],nList[randomNum0]
		array_steps.append(str(randomNum0) + "-" + str(randomNum1))
	return array_steps