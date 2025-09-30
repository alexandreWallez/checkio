"""Resolution of https://open.kattis.com/problems/cutthenegativity """

def cutthenegativity(nb,table) :
    """Resolution of https://open.kattis.com/problems/cutthenegativity

    Args:
        nb (Integer): number of lines
        table (Array of Integers): a table of airline tracks costs of flights

    Returns:
        String : The first line is the number of direct flights, This is to be followed by m lines
        of the form u,v and c, indicating that there is a direct flight from u to v with a cost of c 

    """
    result = ""
    res = ""
    count = 0

    for k in range(nb) :
        lst = table[k][:]
        for i in range (nb) :
            if int(lst[i]) >= 1 :
                count += 1
                res += f"{k+1} {i+1} {lst[i]}\n"
    result += f"{count}\n" + res
    return result
