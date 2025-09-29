def spavanac(x,y):
    """
    https://open.kattis.com/problems/spavanac
    """
    
    res = (0,0)
    
    if y < 45 :
        if x == 0 :
            res = (23,60-(45-y))
        else :
           res = (x-1,60-(45-y))
    else :
        res = (x,y-45)
        
    return res
