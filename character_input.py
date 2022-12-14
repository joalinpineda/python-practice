""" 
Character Input 

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 
100 years old. Note: for this exercise, the expectation is that you explicitly
write out the year (and therefore be out of date the next year). 

"""


def future_age(age):
    """"Returns year in which the user will be 100 years old."""

    actual_year = 2022
    future_year = actual_year - age + 100
    return future_year


if __name__ == '__main__':
    print('Welcome!')
    user_name = input('What is your name\n').strip()
    user_age = int(input('Cool! And now, tell me how old are you?\n'))
    user_future_age = future_age(user_age)

    print(f"""
    Hello, {user_name}!
    You will be 100 years old in the year {user_future_age}! 😁
    """)
