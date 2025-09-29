def hairofthedog(a,L) :
    """
    https://open.kattis.com/problems/hairofthedog
    """

    temp = ""
    res = 0
    
    for k in range(a) :
        actual = L[k]
        if ((temp != actual) and (actual == "drunk")) :
            res += 1
        temp = actual 
    return res