def cutthenegativity(nb,table) :
    """
    https://open.kattis.com/problems/cutthenegativity
    return : printable result
    """

    result = ""
    str = ""
    count = 0

    for k in range(nb) :
        lst = table[k][:]
        for i in range (nb) :
            if (int(lst[i]) >= 1) :
                count += 1
                str += f"{k+1} {i+1} {lst[i]}\n"
    result += f"{count}\n" + str
    return result
