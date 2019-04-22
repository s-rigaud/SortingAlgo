"""
This module tends to implement all algorithm which can be implemented
using the tkinter interface (app.py)
"""


from random import randint
from functions import are_equals

def bubble_sort(nb_list: list):
    """ Bubble Sort Algorithm """
    for num in range(len(nb_list)-1, 0, -1):
        for i in range(num):
            if nb_list[i] > nb_list[i+1]:
                nb_list[i], nb_list[i+1] = nb_list[i+1], nb_list[i]
                yield str(i) + "-" + str(i+1)


def optimised_bubble_bort(nb_list: list):
    """ 'Optmised' Bubble Sort Algorithm """
    for num in range(len(nb_list)-1, 0, -1):
        ordered = True
        for i in range(num):
            if nb_list[i] > nb_list[i+1]:
                nb_list[i], nb_list[i+1] = nb_list[i+1], nb_list[i]
                ordered = False
                yield str(i) + "-" + str(i+1)
        if ordered:
            break


def cocktail_sort(nb_list: list):
    """ Cocktail Sort Algorithm """
    for k in range(len(nb_list)-1, 0, -1):
        swapped = False
        for i in range(k, 0, -1):
            if nb_list[i] < nb_list[i-1]:
                nb_list[i], nb_list[i-1] = nb_list[i-1], nb_list[i]
                yield str(i) + "-" + str(i-1)
                swapped = True
        for i in range(k):
            if nb_list[i] > nb_list[i+1]:
                nb_list[i], nb_list[i+1] = nb_list[i+1], nb_list[i]
                yield str(i) + "-" + str(i+1)
                swapped = True
        if not swapped:
            break


def selection_sort(nb_list: list):
    """ Selection Sort Algorithm """
    for i in range(len(nb_list)-1, 0, -1):
        max_index = 0
        for location in range(1, i+1):
            if nb_list[location] > nb_list[max_index]:
                max_index = location
        nb_list[i], nb_list[max_index] = nb_list[max_index], nb_list[i]
        yield str(i)+"-"+str(max_index)


def insertion_sort(nb_list: list):
    """ Insertion Sort Algorithm """
    for i in range(1, len(nb_list)):
        currentvalue = nb_list[i]
        position = i
        while position > 0  and  nb_list[position-1] > currentvalue:
            nb_list[position] = nb_list[position-1]
            yield str(position) + "-" + str(position-1)
            position -= 1
        nb_list[position] = currentvalue


def merge_sort(nb_list: list):
    """ Merge Sort Algorithm """

def radix_sort(nb_list: list):
    """ Radiw Sort Algorithm """

def bucket_sort(nb_list: list):
    """ Bucket Sort Algorithm """

    #Range for numbers in a bucket
    bucket_range = 10**(len(str(max(nb_list)))-1)
    #Create 10 buckets
    buckets = [[] for _ in range(10)]
    #Add to the right bucket
    for number in nb_list:
        change_bucket = buckets[int(number // bucket_range)]
        change_bucket.append(number)

    bucket_ordered_nb_list = []
    for bucket in buckets:
        bucket_ordered_nb_list += bucket

    #Making transition between starting array and pseudo-sorted array
    copy_bucket_ordered_nb_list = bucket_ordered_nb_list[:]

    for num in copy_bucket_ordered_nb_list:
        nb_list_index = nb_list.index(num)
        bucket_index = bucket_ordered_nb_list.index(num)

        nb_list[nb_list_index] = 0
        bucket_ordered_nb_list[bucket_index] = 0
        nb_list[bucket_index], nb_list[nb_list_index] = nb_list[nb_list_index], nb_list[bucket_index]

        yield str(nb_list_index) + '-' + str(bucket_index)

    sorted_list = []
    for bucket in buckets:
        bucket.sort()
        sorted_list += bucket

    #Making transition between not sorted and sorted array
    bucket_ordered_nb_list = copy_bucket_ordered_nb_list[:]

    for num in copy_bucket_ordered_nb_list:
        bucket_index = bucket_ordered_nb_list.index(num)
        sorted_list_index = sorted_list.index(num)

        bucket_ordered_nb_list[bucket_index] = 0
        sorted_list[sorted_list_index] = 0
        bucket_ordered_nb_list[bucket_index], bucket_ordered_nb_list[sorted_list_index] = bucket_ordered_nb_list[sorted_list_index], bucket_ordered_nb_list[bucket_index]

        yield str(bucket_index) + '-' + str(sorted_list_index)

def counting_sort(nb_list: list):
    """ Counting Sort Algorithm """
    count = [0 for _ in range(max(nb_list)+1)]
    res = []

    for num in nb_list:
        count[num] += 1

    for i in range(len(count)):
        res += [i for j in range(count[i])]

    #Making transition between not sorted and sorted array
    copy_nb_list = nb_list[:]
    for num in copy_nb_list:
        nb_list_index = nb_list.index(num)
        res_index = res.index(num)

        nb_list[nb_list_index] = 0
        res[res_index] = 0
        nb_list[res_index], nb_list[nb_list_index] = nb_list[nb_list_index], nb_list[res_index]

        yield str(nb_list_index) + '-' + str(res_index)

def smooth_sort(nb_list: list):
    """ Smooth Sort Algorithm """

def heap_sort(nb_list: list):
    """ Heap Sort Algorithm """

def quick_sort(nb_list: list):
    """ Quick Sort Algorithm """

def bogo_sort(nb_list: list):
    """Mixing until it's randomly sorted"""
    ordered_list = sorted(nb_list[:])
    while not are_equals(nb_list, ordered_list):
        random_num0 = randint(0, len(nb_list)-1)
        random_num1 = randint(0, len(nb_list)-1)
        nb_list[random_num0], nb_list[random_num1] = nb_list[random_num1], nb_list[random_num0]
        yield str(random_num0) + "-" + str(random_num1)
