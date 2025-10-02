"""Resolution of https://open.kattis.com/problems/asciikassi """

import marimo

app = marimo.App(width="medium")


@app.function
def asciikassi(nb) :
    """Resolution of https://open.kattis.com/problems/asciikassi 

    Args:
        nb (int): the interior sidelength of the square.

    Returns:
        String : a square of size NxN. 
    """
    res = ""

    res += "+" + "-" *nb + "+" + "\n"

    for _ in range (nb) :
        res += "|" + " " * nb + "|" + "\n"

    res += "+" + "-" *nb + "+"

    return res


@app.cell
def _():
    print(asciikassi(2))
    print(asciikassi(5))
