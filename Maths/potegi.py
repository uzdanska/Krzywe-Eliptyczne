import pandas as pd
from math import gcd as nwd

def pierwiastkiPierwotne(p, g):
    if nwd(p, g) == 1:
        return "NWD({}, {}) = 1, liczba {} jest względnie pierwsza z {}.".format(p, g, g, p)
    else:
        return "NWD({}, {}) != 1, liczba {} nie jest względnie pierwsza z {}.".format(p, g, g, p)

def potegiModulo(p, g):
    listaWyników = []
    listaP = []
    listaG = []
    if nwd(p, g) == 1:
        for i in range(1, p):
            # st.write('{}^({}) = {} mod {}'.format(g, i , g**i%p,p))
            listaP.append(i)
            listaG.append(int(g))
            listaWyników.append(g**i % p)

        potegiP = { 'Podstawa potęgi': pd.Series(listaG),
                    'Wykladnik potęgi': pd.Series(listaP),
                    'wynik modulo {}'.format(int(p)): pd.Series(listaWyników)}

        potegiDf = pd.DataFrame(potegiP)
        return potegiDf.style.background_gradient()