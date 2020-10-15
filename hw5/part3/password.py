import re




passwordRegex = re.compile(r'''(
    [a-zA-Z0-9]+
    )''',re.VERBOSE)



''' strong Password Detection

Author: <your name>
'''


def strong_password(string):
    '''Given a string, return True if is strong, False otherwise

    A strong password is definied as one that is at least eight
    characters long, contains both uppercase and lowercase characters,
    and has at least one digit.

   
    '''
    print("Insert password")
    password = input()


    for groups in passwordRegex.search(password):
        print()

    
    # place your solution in this function