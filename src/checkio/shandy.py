"""Resolution of https://open.kattis.com/problems/shandy"""

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
