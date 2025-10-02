"""Resolution of https://open.kattis.com/problems/millifaersla"""

import marimo

app = marimo.App(width="medium")


@app.function
def millifaersla(a,b,c) :
    """Resolution of https://open.kattis.com/problems/millifaersla

    Args:
        a (Integer): first Intger to compare
        b (Integer): seconde Intger to compare
        c (Integer): third Intger to compare

    Returns:
        String : Output the name of the service with the lowest transaction fee 
        in a single line.
    """

    msg = ""

    if ((a < b) and (a < c)) :
        msg = "Monnei"
    elif b < c :
        msg = "Fjee"
    else :
        msg = "Dolladollabilljoll"

    return msg

@app.cell
def _():
    print(millifaersla(17,2,3))
    print(millifaersla(14744,265548,22894))
