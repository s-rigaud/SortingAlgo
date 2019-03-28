import random

def areEqual(arr1, arr2):   
	if len(arr1) != len(arr2):
		return False
	for i in range(0, len(arr1)):
		if arr1[i] != arr2[i]:
			return False
	return True 

