def miroir(m) :
    if len(m) == 0 :
        return ""
    else :
        return miroir(m[1:]) + m[0]

#https://open.kattis.com/problems/filip

x = input()

str1, str2 = x.split()

nb1 = int(miroir(str1))
nb2 = int(miroir(str2))

if nb1 > nb2 :
    print(nb1)
else : 
    print(nb2)