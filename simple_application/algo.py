import time, random
from functions import are_equals

def bubble_sort(nList:list):
	for num in range(len(nList)-1,0,-1):
		for i in range(num):
			if nList[i] > nList[i+1]:
				nList[i], nList[i+1] = nList[i+1], nList[i]
				yield (str(i) + "-" + str(i+1))


def optimised_bubble_bort(nList:list):
	for num in range(len(nList)-1,0,-1):
		ordered = True
		for i in range(num):
			if nList[i]>nList[i+1]:
				nList[i],nList[i+1] = nList[i+1],nList[i]
				ordered = False
				yield (str(i)+"-"+str(i+1))
		if ordered :
			break


def cocktail_sort(nList:list):
	for k in range(len(nList)-1, 0, -1):
		swapped = False
		for i in range(k, 0, -1):
			if nList[i]<nList[i-1]:
				nList[i], nList[i-1] = nList[i-1], nList[i]
				yield (str(i)+"-"+str(i-1))
				swapped = True
		for i in range(k):
			if nList[i] > nList[i+1]:
				nList[i], nList[i+1] = nList[i+1], nList[i]
				yield (str(i)+"-"+str(i+1))
				swapped = True
		if not swapped:
			break


def selection_sort(nList:list):
	for i in range(len(nList)-1, 0, -1):
		indexMax = 0
		for location in range(1, i+1):
			if nList[location]>nList[indexMax]:
				indexMax = location
		nList[i], nList[indexMax] = nList[indexMax], nList[i]
		yield (str(i)+"-"+str(indexMax))


def insertion_sort(nList:list):
	for i in range(1,len(nList)):
		currentvalue = nList[i]
		position = i
		while position > 0  and  nList[position-1] > currentvalue:
			nList[position] = nList[position-1]
			yield (str(position)+"-"+str(position-1))
			position -= 1
		nList[position] = currentvalue


def merge_sort(nList:list):
	pass

def radix_sort(nList:list):
	pass

def bucket_sort(nList:list):
	#Range for numbers in a bucket
	bucket_range = 10**(len(str(max(nList)))-1)
	#Create 10 buckets
	buckets =[[] for _ in range(10)]
	#Add to the right bucket
	for number in nList :
		bucketVoulu = buckets[int(number // bucket_range)]
		bucketVoulu.append(number)

	bucket_ordered_nList = []
	for bucket in buckets:
		bucket_ordered_nList += bucket

	#Making transition between starting array and pseudo-sorted array
	copy_bucket_ordered_nList = bucket_ordered_nList[:]

	for num in copy_bucket_ordered_nList:
		nList_index = nList.index(num)
		bucket_index = bucket_ordered_nList.index(num)

		nList[nList_index] = 0
		bucket_ordered_nList[bucket_index] = 0
		nList[bucket_index], nList[nList_index] = nList[nList_index], nList[bucket_index]

		yield (str(nList_index) + '-' + str(bucket_index))

	sorted_list = []
	for bucket in buckets:
		bucket.sort()
		sorted_list += bucket

	#Making transition between not sorted and sorted array
	bucket_ordered_nList = copy_bucket_ordered_nList[:]

	for num in copy_bucket_ordered_nList:
		bucket_index = bucket_ordered_nList.index(num)
		sorted_list_index = sorted_list.index(num)

		bucket_ordered_nList[bucket_index] = 0
		sorted_list[sorted_list_index] = 0
		bucket_ordered_nList[bucket_index], bucket_ordered_nList[sorted_list_index] = bucket_ordered_nList[sorted_list_index], bucket_ordered_nList[bucket_index]

		yield (str(bucket_index) + '-' + str(sorted_list_index))

def counting_sort(nList:list):
	count = [0 for _ in range(max(nList)+1)]
	res = []

	for num in nList:
		count[num] += 1

	for i in range(len(count)):
		res += [i for j in range(count[i])]

	#Making transition between not sorted and sorted array
	copy_nList = nList[:]
	for num in copy_nList:
		nList_index = nList.index(num)
		idxRes = res.index(num)

		nList[nList_index] = 0
		res[idxRes] = 0
		nList[idxRes], nList[nList_index] = nList[nList_index], nList[idxRes]

		yield (str(nList_index) + '-' + str(idxRes))

def smooth_sort(nList:list):
	pass

def heap_sort(nList:list):
	pass

def quick_sort(nList:list):
	pass

def bogo_sort(nList:list):
	"""Mixing until it's randomly sorted"""
	ordered_list = sorted(nList[:])
	while not are_equals(nList, ordered_list) :
		random_num0 = random.randint(0, len(nList)-1)
		random_num1 = random.randint(0, len(nList)-1)
		nList[random_num0], nList[random_num1] = nList[random_num1], nList[random_num0]
		yield str(random_num0) + "-" + str(random_num1)
