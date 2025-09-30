"""Resolution of https://open.kattis.com/problems/asciikassi """

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
