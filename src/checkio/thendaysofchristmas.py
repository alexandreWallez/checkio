"""Resolution of https://open.kattis.com/problems/thendaysofchristmas"""

import marimo

app = marimo.App(width="medium")


@app.function
def thendaysofchristmas(n):
    """Resolution of https://open.kattis.com/problems/thendaysofchristmas

    Args:
        n (Integer): The input consists of a single integer, N,
        the number of days of Christmas (1<=N<=366)

    Returns:
        (Integer,Integer): the first contains the number of gifts you receive 
        on the Nth day, and the second contains the total number of gifts 
        you have received by the end of the Nth day.
    """

    nb_gift_current = 0
    nb_gift = 0

    for k in range(n+1) :
        nb_gift_current = int(k*(k+1)/2)
        nb_gift += nb_gift_current

    return (nb_gift_current,nb_gift)

@app.cell
def _():
    print(thendaysofchristmas(2))
    print(thendaysofchristmas(17))
