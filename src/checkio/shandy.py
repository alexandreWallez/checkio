def shandy(beer,lemonade) :
    """
    https://open.kattis.com/problems/shandy
    """
    
    res = 0
    
    if beer > lemonade :
        res = lemonade*2
    else :
        res = beer*2
        
    return res
