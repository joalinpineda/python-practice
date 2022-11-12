""""
Ask the user for a number. 
Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
"""

def is_even(number):
    """Returns with a boolean if the number is even."""
    
    if number % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    num = int(input('Write a number:\n'))
    if is_even(num):
        print('You picked an even number.')
    else:
        print('You picked an odd number')