"""Resolution of https://open.kattis.com/problems/shandy"""

import marimo

app = marimo.App(width="medium")


@app.function
def shandy(beer,lemonade) :
    """Resolution of https://open.kattis.com/problems/shandy

    Args:
        beer (Integer): number of bottles of beer
        lemonade (Integer): number of bottles of lemonade

    Returns:
        Integer : the number of shandies you can serve
    """

    res = 0

    if beer > lemonade :
        res = lemonade*2
    else :
        res = beer*2

    return res

@app.cell
def _():
    print(shandy(50,20))
    print(shandy(17,2))
