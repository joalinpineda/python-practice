"""
Take two lists, say for example these two:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
"""
import random

def overlap(list_a, list_b):
    """overlap function
    Returns a list with the elements that are in
    both list_a and list_b without duplicates.
    """
    new_array =list(set(element for element in list_b if element in list_a))
    return new_array


if __name__ == '__main__':
    #Given 2 lists
    b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    overlap_list = overlap(a,b)
    print(overlap_list) #[1, 2, 3, 5, 8, 13]

    #With random list
    random_list1 = [random.randint(1, 100) for _ in range(10)]
    random_list2 = [random.randint(1, 100) for _ in range(10)]
    random_lists_overlap = overlap(random_list1, random_list2)
    print('Random list 1: ', random_list1)
    print('Random list 2: ',random_list2)
    print('Common elements: ', random_lists_overlap)

