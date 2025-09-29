def miroir(m) :
    if len(m) == 0 :
        return ""
    else :
        return miroir(m[1:]) + m[0]

def filip(str1,str2) :
    """
    https://open.kattis.com/problems/filip
    """
    nb1 = miroir(str1)
    nb2 = miroir(str2)
    
    res = ""

    if nb1 > nb2 :
        res = nb1
    else : 
        res = nb2
        
    return res