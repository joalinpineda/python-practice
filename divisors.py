"""Divisors
Create a program that asks the user for a number and then 
prints out a list of all the divisors of that number. 
"""

def divisors(number):
    """Returns all the divisors of a given number."""

    num_range = range(1, number+1)
    divisors_list = [element for element in num_range if num % element == 0]
    if divisors_list == []:
        print(f'There are not divisors for {number}')
    else:
        return divisors_list

if __name__ == '__main__':
    num = int(input('Please choose a number to divide:\n'))
    num_divisors = divisors(num)
    print(f'The divisors of {num} are: ', num_divisors)