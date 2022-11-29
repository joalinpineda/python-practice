"""
Let’s say I give you a list saved in a variable: 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes 
a new list that has only the even elements of this list in it.
"""

def newList(list_of_elements):
    """Returns a list that contains the even elements of 
    the given list."""

    return [element for element in list_of_elements if element%2 == 0]

if __name__ == '__main__':
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    new_list = newList(a)
    print(new_list)