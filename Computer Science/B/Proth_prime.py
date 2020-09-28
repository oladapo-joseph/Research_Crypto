"""
    The Proth theorem
                n = k*(2^n) + 1
    where (2^n) > k,
        A prime of this form is known as a Proth prime

"""


def is_Prime(n):
    '''
    Function checks if a number is a prime number at all.

    Return:
        True or False
    '''
    if n%3==0 or n%2==0 or n%7==0 or n%5==0:
        return False
    else:
        return True

def is_Power_of_Two(n):
    '''
    This is to check a number if it is a power of 2

    Returns:
        True or False
    '''
    return (n and (n & (n - 1)) == False)

def is_Proth_Number(x):
    """
    This function is used to check if for the properties of a proth number.
    For a number, x, to be a prothprime;
        x-1 must be a divisible by an odd number,
        and the remainder must be a power of 2

    Returns:
        True or False
    """
    x = x -1
    y = 1
    while ((x // y)>y):
        if (x % y == 0):
            if (is_Power_of_Two(x // y)):
                return True
        y += 2
    return False

def is_Proth_Prime(n):
    """
    Function to check if a number is a prothprime

    Returns:
        'yes' : if a prothprime number
        'not a proth prime': if a prime number but not a proth prime
        'not a prime number': if not a prime number


    """
    if is_Prime(n):
        if is_Proth_Number(n):
            return('yes')
        else:
            return('not a proth prime')

    else:
         return 'not a prime'
    
value = int(input('Enter a number to check: '))
print(is_Proth_Prime(value))
