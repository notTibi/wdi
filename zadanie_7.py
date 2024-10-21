def zakres():
    while True:
        try:
            a = int(input("Podaj początek zakresu: "))
            b = int(input("Podaj koniec zakresu: "))
        except ValueError:
            print("Wymagane liczby calkowite.")
        else:
            break
    if b-a > 19:
        avg = (a+b)//2
        if avg%2 == 0:
            for i in range(avg-2,avg+4):
                print(i)
        else:
            for i in range(avg-3,avg+4):
                if i == avg:
                    continue
                print(i)
    else:
        for i in range(a,b+1):
            print(i)
zakres()