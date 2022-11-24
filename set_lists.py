""""
String lists
Ask the user for a string and print out whether this string 
is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""
def is_palindrome(word):
    """Evaluate if a given word is a palindrome or not
    and print it the result on console. 
    (A palindrome is a string that reads the same forwards and backwards.)
    """

    word = word.replace(' ', '')#Remove blanks
    reverse_word = word[::-1]#Turns the word given into its mirror
    if reverse_word == word:#If both are equal, it is a palindrome
        print('Is a palindrome')
    else:
        print('Is not a palindrome')


if __name__ == '__main__':
    word = input('Write a word\n')
    is_palindrome(word)
