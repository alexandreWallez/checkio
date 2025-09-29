def millifaersla(a,b,c) :
    """
    https://open.kattis.com/problems/millifaersla
    """
    
    msg = ""

    if ((a < b) and (a < c)) :
        msg = "Monnei"
    elif b < c :
        msg = "Fjee"
    else :
        msg = "Dolladollabilljoll"
        
    return msg