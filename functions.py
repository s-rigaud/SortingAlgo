import random

def areEqual(arr1, arr2):   
	for i in range(0, len(arr1)):
		if (arr1[i] != arr2[i]):
			return False
	return True 

def initialize_list():
	return [random.randint(4,10000) for _ in range(55)]

