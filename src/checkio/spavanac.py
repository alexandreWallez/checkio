"""Resolution of https://open.kattis.com/problems/spavanac"""

import marimo

app = marimo.App(width="medium")


@app.function
def spavanac(x,y):
    """Resolution of https://open.kattis.com/problems/spavanac

    Args:
        x (Integer): the hours
        y (Integer): the minutes

    Returns:
        (Integer,Integer): the time 45 minutes before input time.
    """

    res = (0,0)

    if y < 45 :
        if x == 0 :
            res = (23,60-(45-y))
        else :
            res = (x-1,60-(45-y))
    else :
        res = (x,y-45)

    return res

@app.cell
def _():
    print(spavanac(17,20))
    print(spavanac(0,10))
