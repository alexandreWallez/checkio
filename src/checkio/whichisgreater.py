"""Resolution of https://open.kattis.com/problems/whichisgreater"""

import marimo

app = marimo.App(width="medium")


@app.function
def whichisgreater(x,y) :
    """Resolution of https://open.kattis.com/problems/whichisgreater

    Args:
        x (Integer): the first integer to compare
        y (Integer): the second integer to compare

    Returns:
        Integer : Output a single line with 1 if a > b, 0 otherwise.
    """
    if x <= y :
        return 0
    return 1

@app.cell
def _():
    print(whichisgreater(17,2))
    print(whichisgreater(4,288729948))
