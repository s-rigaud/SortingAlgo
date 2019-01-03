import random

def areEqual(arr1, arr2):   
	for i in range(0, len(arr1)):
		if (arr1[i] != arr2[i]):
			return False
	return True 

def fillArrayWithArray(array1,array2):
	assert len(array1)==len(array2), "The two arrays have not the same length, size array1 : {0}, size array2 : {1}".format(len(array1),len(array2))
	for i in range(len(array2)):
		array1[i]=array2[i]

def initializeList():
	numbersList=[]
	for _ in range(55):
		# 4 to be a minimum visible 
		numbersList.append(random.randint(4,10000))
	return numbersList