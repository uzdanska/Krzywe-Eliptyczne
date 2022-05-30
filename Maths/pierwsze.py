def czyPierwsza(n):
    """
    Funkcja sprawdza czy n jest liczbą pierwszą

    Args:
        n (int): liczba wybrana przez użytkownika

    Return:
        True: jeśli n jest liczbą pierwszą
        False: jeśli n nie jest liczbą pierwszą

    Raises:
        ValueError: zwraca wyjątek gdy N nie jest liczbą całkowitą.
    """
    try:
        n = int(n)
        if n <= 1:  # ujemne liczby
            return False
        elif n % 2 == 0 and n > 2:  # n % 2 == 0 dodatnie parzyste 
            return False
        else: # dodatnie nieparzyste i dwójka
            for i in range(3, n, 2): # od 3 do n z krokiem 2 czyli tylko nieparzyste
                if n % i == 0: ## n dzieli i to znaczy że liczba i nie jest pierwszą
                    return False
            return True ## pozostałe np 2
    except ValueError as e: # jeśli n nie można zamienić na liczbę całkowitą
        print("ValueError exception: ", e)

# n = input('Podaj liczbę: ')
# print(czyPierwsza(n))

def liczbyPierwsze(N):
    """
    Funkcja wypisuje wszystkie liczby pierwsze do wybranego zakresu N
    
    Args:
        N (int): zakres liczb całkowitych 

    Return:
        listę liczb pierwszych do wybranego zakresu
    
    Raises:
        ValueError: zwraca wyjątek gdy N nie jest liczbą całkowitą.
    """
    try:
        N = int(N)
        lista = [] 
        for i in range(3,N):
            if czyPierwsza(i):
                lista.append(i)
        return lista
    except ValueError as e:
        print("ValueError exception: ", e)
