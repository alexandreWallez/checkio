def asciikassi(nb) :
    """
    https://open.kattis.com/problems/asciikassi
    """
    str = ""

    str += "+" + "-" *nb + "+" + "\n"

    for k in range (nb) :
        str += "|" + " " * nb + "|" + "\n"

    str += "+" + "-" *nb + "+"

    print(str)