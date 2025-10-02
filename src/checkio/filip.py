"""Resolution of https://open.kattis.com/problems/filip"""

import marimo

app = marimo.App(width="medium")


@app.function
def miroir(m) :
    """Reverse a string 

    Args:
        m (String): the string to reverse

    Returns:
        String : reversed string
    """
    res = ""
    if len(m) != 0 :
        res = miroir(m[1:]) + m[0]
    return res

def filip(str1,str2) :
    """Resolution of https://open.kattis.com/problems/filip

    Args:
        str1 (String): first string to compare
        str2 (String): second string to compare

    Returns:
        String : The output should contain the larger of the numbers in the input
    """
    nb1 = miroir(str1)
    nb2 = miroir(str2)
    res = ""

    if nb1 > nb2 :
        res = nb1
    else :
        res = nb2

    return res

@app.cell
def _():
    print(filip("734", "893"))
    print(filip("221", "231"))
