"""Resolution of https://open.kattis.com/problems/hairofthedog"""

import marimo

app = marimo.App(width="medium")


@app.function
def hairofthedog(a,lst) :
    """Resolution of https://open.kattis.com/problems/hairofthedog

    Args:
        a (Integer):  the number a of consecutive days where you have logged your behaviour
        lst (Array of String): array of string containing “drunk” or “sober”

    Returns:
       Integer : The number of days you were hungover.
    """

    temp = ""
    res = 0

    for k in range(a) :
        actual = lst[k]
        if ((temp != actual) and (actual == "drunk")) :
            res += 1
        temp = actual
    return res

@app.cell
def _():
    print(hairofthedog(5,["sober","drunk","drunk","sober","sober"]))
    print(hairofthedog(5,["sober","drunk","sober","drunk","sober"]))
