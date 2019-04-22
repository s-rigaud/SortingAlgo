""" Single test between two arrays """

def are_equals(arr1: list, arr2: list):
    """ Test if two array are equals"""
    if len(arr1) != len(arr2):
        return False
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return False
    return True
