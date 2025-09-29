import math

def secret(nb,all_message) :
    """
    https://open.kattis.com/problems/secretmessage
    """
    
    all_new_message = []

    for i in range(nb) :
        
        message = all_message[i]
        L = len(message)
        
        if int(math.sqrt(L))*int(math.sqrt(L)) == L :
            K = int(math.sqrt(L))
        else :
            K = math.floor(math.sqrt(L))+1
            
        M = K*K
        
        for j in range(M-L) :
            message+="*"
        lst = list(message)
        lst = [lst[r*K:(r+1)*K] for r in range(K)]
        lst_rotated = [[lst[K-1-c][r] for c in range(K)] for r in range(K)]
        new_message = ""
            
        for o in range(K) :
            for l in range(K) :
                if lst_rotated[o][l] != "*" :
                    new_message += lst_rotated[o][l]
                    
        all_new_message.append(new_message)
            
    return all_new_message    

