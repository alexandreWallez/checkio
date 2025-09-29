def thendaysofchristmas(N):
    """
    1 <= N <= 366
    https://open.kattis.com/problems/thendaysofchristmas
    """

    nb_gift_current = 0
    nb_gift = 0

    for k in range(N+1) :
        nb_gift_current = int(k*(k+1)/2)
        nb_gift += nb_gift_current

    return (nb_gift_current,nb_gift)