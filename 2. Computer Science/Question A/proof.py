def Fibonacci(n):
    '''
    Function to find the nth term of the Fibonacci sequence
    Args:
        n : integer
            the position of the desired number

    Return:
        x : integer
            the nth term in the fibonacci series

    '''
    if n ==0:
        return (0)
    if n==1:
        return 1
    else:
        x = Fibonacci(n-1)+ Fibonacci(n-2)
        return (x)

print(Fibonacci(15))
