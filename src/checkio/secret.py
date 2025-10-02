"""Resolution of https://open.kattis.com/problems/secretmessage"""

import math
import marimo

app = marimo.App(width="medium")


@app.function
def secret(nb,all_message) :
    """Resolution of https://open.kattis.com/problems/secretmessage

    Args:
        nb (Integer): number of original message
        all_message (Array of String): array of original message

    Returns:
        String : For each original message, output the secret message
    """

    all_new_message = []

    for i in range(nb) :

        message = all_message[i]
        l = len(message)

        if int(math.sqrt(l))*int(math.sqrt(l)) == l :
            k = int(math.sqrt(l))
        else :
            k = math.floor(math.sqrt(l))+1

        m = k*k

        for _ in range(m-l) :
            message+="*"
        lst = list(message)
        lst = [lst[r*k:(r+1)*k] for r in range(k)]
        lst_rotated = [[lst[k-1-c][r] for c in range(k)] for r in range(k)]
        new_message = ""

        for o in range(k) :
            for l in range(k) :
                if lst_rotated[o][l] != "*" :
                    new_message += lst_rotated[o][l]

        all_new_message.append(new_message)

    return all_new_message

@app.cell
def _():
    print(secret(2,["iloveyoutooJill","TheContestisOver"]))
