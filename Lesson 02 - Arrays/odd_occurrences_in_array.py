# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    # use hashtable to count occurences
    count_items = {}

    for item in A:

        count_items[item] = count_items.get(item, 0) + 1

    
    for key, value in count_items.items():

        if (value == 1) | (value % 2 == 1):

            return key