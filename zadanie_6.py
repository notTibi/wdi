def obliczenia():
    a = int(input())
    b = int(input())
    if a < 0 and b < 0:
        print("Obie liczby są mniejsze od 0. Kończę program.")
    else:
        if a < 0:
            a *= -1
        elif b < 0:
            b *= -1
        print("Suma:", a+b)
        print("Różnica:", a-b)
        print("Iloczyn:", a*b)
        if a*b == 10:
            print ("Yay!")
        print("Iloraz:", a/b)
        print("Kwadraty:", a*a, b*b)
        print("Pierwiastki drugiego stopnia:", a**(1/2), b**(1/2))
obliczenia()
#single
"""m
u
l
t
i
l
i
n
e"""