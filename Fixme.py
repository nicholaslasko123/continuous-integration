#!/usr/bin/python3

def factorial(n):
    '''
    Returns the product of all numbers from 1 to n.

    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(40)
    815915283247897734345611269596115894272000000000
    >>> factorial(400)
    64034522846623895262347970319503005850702583026002959458684445942802397169186831436278478647463264676294350575035856810848298162883517435228961988646802997937341654150838162426461942352307046244325015114448670890662773914918117331955996440709549671345290477020322434911210797593280795101545372667251627877890009349763765710326350331533965349868386831339352024373788157786791506311858702618270169819740062983025308591298346162272304558339520759611505302236086810433297255194852674432232438669948422404232599805551610635942376961399231917134063858996537970147827206606320217379472010321356624613809077942304597360699567595836096158715129913822286578579549361617654480453222007825818400848436415591229454275384803558374518022675900061399560145595206127211192918105032491008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    '''
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def triangular(n):
    '''
    Returns the nth triangular number.

    The nth triangular number is the sum of all numbers from 1 to n.
    It is like the factorial, but uses addition instead of multiplication.

    >>> triangular(1)
    1
    >>> triangular(2)
    3
    >>> triangular(3)
    6
    >>> triangular(4)
    10
    >>> triangular(40)
    820
    >>> triangular(400)
    80200
    '''
    print("hello")
    return n * (n + 1) // 2  # Using the formula for the nth triangular number
