"""
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list 
that has all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from 
the original list a that are smaller than that number given by the user.
"""
def less_than(list_of_elements, num):
    """Returns a list that contains the elements less than the given number."""
    less_than = []
    for element in list_of_elements:
        if element < num:
            less_than.append(element)
    return less_than


if __name__ == '__main__':

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print('The elements in the list are ', a)
    choose_number = int(input('Choose a number:\n'))
    # if choose_number in a:
    #     print(choose_number, 'is in the list')
    # else:
    #     print(choose_number, 'is not in the list')
    new_list = less_than(a, choose_number)
    print(f'The elements less than {choose_number} are: ', new_list)