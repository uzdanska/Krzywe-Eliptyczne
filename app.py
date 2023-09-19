
import streamlit as st
import pandas as pd
from math import pow
import subprocess

# Define the path to your requirements.txt file
requirements_file = "requirements.txt"

# Use subprocess to run the pip install command
try:
    subprocess.check_call(["pip", "install", "-r", requirements_file])
    print("Dependencies installed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

import plotly.express as plte
from Maths.pierwsze import liczbyPierwsze, czyPierwsza
from Maths.potegi import potegiModulo, pierwiastkiPierwotne

N, px, py = 60, [], []

def fx(x):
    """
    Funkcja zwracająca wartość równania w zależności od x, wstawiając do równania krzywej eliptycznej.
    Args:
        x (int): wartość współrzędnej x danego punktu.
    Return:
        wartość funkcji w punkcie x.
    Raises:
        ValueError: zwraca wyjątek gdy x nie jest liczbą całkowitą.
    """
    try:
        x = int(x)
        return pow(x, 3) + a * x + b
    except ValueError as e:
        print("ValueError exception: ", e)

def fy(y):
    """
    Funkcja zwracająca wartość równania w zależności od y, wstawiając do równania krzywej eliptycznej.
    Args:
        y (int): wartość współrzędnej y danego punktu.
    Return:
        wartość funkcji w punkcie y.
    Raises:
        ValueError: zwraca wyjątek gdy y nie jest liczbą całkowitą.
    """
    try:
        y = int(y)
        return pow(y, 2)
    except ValueError as e:
        print("ValueError exception: ", e)


def wspPunktow(p):
    """
    Funkcja dodająca do listy wartości punktów modulo p jeśli obie strony równania są równe modulo p.
    Warunkiem jest żeby p bylo liczbą pierwszą.

    Args:
        p (int): liczba pierwsza.

    Return:
        wartości punktów w ciele Z modulo p.
    """
    try:
        p = int(p)
        if czyPierwsza(p) == True:
            for i in range(0, p):
                for j in range(0, p):
                    modulofx = fx(i)%p
                    modulofy = fy(j)%p
                    if modulofx == modulofy:
                        px.append(i)
                        py.append(j)
    except ValueError as e:
        print("ValueError exception: ", e)

def rownanieZapis(a, b, p):
    """
    Funkcja zwracająca odpowiednie znaki w równaniu krzywej eliptycznej w zależności od wartości
    podanych przez użytkownika.

     Args:
        a (int): współczynnik a,
        b (int): współczynnik b,
        p (int): liczba pierwsza.

    Return:
        odpowiednie równanie w zalężnośći od wartości a i b.
    """
    if a > 0 and b > 0:
        return st.latex('''E: y^2 = x^3 + {}x + {}  \ \ (mod \ {})'''.format(int(a), int(b), p))
    elif a > 0 and b < 0:
        return st.latex('''E: y^2 = x^3 + {}x  {} \ \ (mod \ {})'''.format(int(a), int(b), p))
    elif a < 0 and b < 0:
        return st.latex('''E: y^2 = x^3 {}x  {} \ \ (mod \ {})'''.format(int(a), int(b), p))
    elif a < 0 and b > 0:
        return st.latex('''E: y^2 = x^3 {}x + {} \ \ (mod \ {})'''.format(int(a), int(b), p))
    elif a == 0 and b > 0:
        return st.latex('''E: y^2 = x^3 + {} \ \ (mod \ {})'''.format(int(b), p))
    elif a == 0 and b < 0:
        return st.latex('''E: y^2 = x^3  {} \ \ (mod \ {})'''.format(int(b), p))
    elif a > 0 and b == 0:
        return st.latex('''E: y^2 = x^3 + {}x \ \ (mod \ {})'''.format(int(a), p))
    elif a < 0 and b == 0:
        return st.latex('''E: y^2 = x^3  {}x \ \ (mod \ {})'''.format(int(a), p))
    else:
        return st.latex('''E: y^2 = x^3 \ \ (mod \ {})'''.format(p))

def wykres():
    """
    Funkcja rysująca wykres punktowy krzywych eliptycznych w ciele skończonym.

    Return:
        wykres punktowy.
    """

    fig = plte.scatter(df, x=px, y=py, color_discrete_sequence=['#000957'])
    fig.update_layout({
        'title': 'Krzywa eliptyczna nad ciałem modulo {}'.format(p),
        'plot_bgcolor': 'rgba(124, 154, 172, 0.6)',
        'paper_bgcolor': 'rgba(124, 154, 172, 0.2)'
    })
    st.write(fig)

## Tytuł
st.markdown(f'<h1 style="color:#371B58;font-size:34px;font: "monospace">{"Krzywe Eliptyczne nad ciałami skończonymi"}</h1>', unsafe_allow_html=True)

## Nagłówek
st.sidebar.markdown(f'<h2 style="color:#21325E;font-size:23px;font: "monospace">{"Parametry krzywej:"}</h2>', unsafe_allow_html=True)

## wybór współczynnika a przez użytkownika
a = st.sidebar.number_input(
    label = 'Współczynnik a',
    value = -1
)
## wybór współczynnika b przez użytkownika
b = st.sidebar.number_input(
    label = "Współczynnik b",
    value = 4
)


## zmiana zakresu liczb pierwszych
changeP = st.sidebar.checkbox('Zmiana zakresu liczb pierwszych')

if changeP:
    N = st.sidebar.number_input(
        label = "Zakres wyboru liczb pierwszych",
        min_value = N
    )

p = st.sidebar.select_slider(
    label = "Liczba pierwsza",
    options = liczbyPierwsze(N),
    value = 7 )

noweBtn = st.sidebar.checkbox(label = 'Dodaj / usuń równanie')
zapiszBtn = st.sidebar.checkbox(label = "Zapisz parametry", value = noweBtn)
daneBtn = st.sidebar.checkbox('Pokaż współrzędne punktów: ', value = noweBtn)
wykresBtn = st.sidebar.checkbox(label = "Wygeneruj wykres", value = noweBtn)

if zapiszBtn:
    st.markdown(f'<h5 style="color:#4C3575;font-size:15px;font:"monospace">{"Postać krzywej eliptycznej: "}</h5>',
                unsafe_allow_html=True)
    rownanieZapis(a, b, p)

wspPunktow(p) #wywołanie funkcji

#dodanie wartości px - lista pierwszych współrzędnych, py - list drugich współrzędnych do słownika
moduloP = { 'Wsp x': pd.Series(px),
            'Wsp y': pd.Series(py)}

# dodanie słownika do tabeli danych
df = pd.DataFrame.from_dict(moduloP)
if daneBtn:
    st.markdown(f'<h5 style="color:#4C3575;font-size:15px;font:"monospace">{"Współrzędne punktów: "}</h5>',
                unsafe_allow_html=True)

    ## wyśrodkowanie tabeli:
    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col3:
        pass
    with col2:
        st.write(df.style.background_gradient()) #ustawienie tła tabeli danych

if wykresBtn and zapiszBtn:
    st.markdown(f'<h5 style="color:#4C3575;font-size:15px;font:"monospace">{"Wykres punktowy: "}</h5>',
                unsafe_allow_html=True)
    wykres()

if wykresBtn and zapiszBtn == False:
    st.write('Najpierw zapisz równanie')


st.markdown(f'<h2 style="color:#4C3575;font-size:15px;font:"monospace">{"Pierwiastki pierwotne oraz generator grupy"}</h2>',
                unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    P = st.select_slider(
        label="Modulo",
        options=liczbyPierwsze(N),
        value=7
    )

with col2:
    g = st.number_input(
        label="Podstawa potęgi",
        min_value = 1,
        value = 17
    )

## wyśrodkowanie przycisku Oblicz
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    pass
with col2:
    pass
with col3:
    potegowanieBtn = st.button('Oblicz:')
with col5:
    pass
with col4:
    pass

if potegowanieBtn:
    st.write('Rozwiązanie: ')
    st.write(pierwiastkiPierwotne(P, g))
    st.write(potegiModulo(P, g))