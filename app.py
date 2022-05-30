import streamlit as st
import pandas as pd
import numpy as np
import math
from Maths.pierwsze import liczbyPierwsze, czyPierwsza
from Maths.potegi import potegiModulo
import random
import plotly.express as plte

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
        return math.pow(x, 3) + a * x + b
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
    while True:
        try:
            y = int(y)
            return math.pow(y, 2)
        except ValueError as e:
            print("ValueError exception: ", e)

def modulo(p):
    """
    Funkcja dodająca do listy wartości punktów modulo p jeśli obie strony równania są równe 0 modulo p.
    Warunkiem jest żeby p bylo liczbą pierwsz.

    Args:
        p (int): liczba pierwsza.

    Return:
        wartości punktów w ciele Z modulo p.

    """
    try:
        p = int(p)
        if czyPierwsza(p) == True and p != 2:
            for i in range(0, p):
                for j in range(0, p):
                    modulofx = fx(i)%p
                    modulofy = fy(j)%p
                    if modulofx == modulofy:
                        px.append(i)
                        py.append(j)
        else:
            p = random.choice(liczbyPierwsze(50))
            print(p)
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
    fig = plte.scatter(df, x=px, y=py, color_discrete_sequence=['#000957'])
    fig.update_layout({
        'title': 'Krzywa eliptyczna nad ciałem modulo {}'.format(p),
        'plot_bgcolor': 'rgba(124, 154, 172, 0.6)',
        'paper_bgcolor': 'rgba(124, 154, 172, 0.2)'
    })
    st.write(fig)



st.markdown(f'<h1 style="color:#371B58;font-size:34px;font: "monospace">{"Krzywe Eliptyczne nad ciałami skończonymi"}</h1>', unsafe_allow_html=True)
st.sidebar.markdown(f'<h2 style="color:#21325E;font-size:23px;font: "monospace">{"Parametry krzywej:"}</h2>', unsafe_allow_html=True)
a = st.sidebar.number_input(
    label = 'Współczynnik a',
    min_value = -100,
    value = 5
)

b = st.sidebar.number_input(
    label = "Współczynnik b",
    min_value = -100,
    value = -20
)

changeP = st.sidebar.checkbox('Zmiana zakresu liczb pierwszych')
if changeP:
    N = st.sidebar.number_input(
        label = "Zakres wyboru liczb Pierwszych",
        min_value = N
    )

p = st.sidebar.select_slider(
    label = "Liczba pierwsza",
    options = liczbyPierwsze(N),
    value = 17
)
# st.markdown(f'<h2 style="color:#4C3575;font-size:23px;font:"monospace">{"Krzywe eliptyczne nad ciałami skończonymi"}</h2>', unsafe_allow_html=True)


modulo(p)
moduloP = { 'Wsp x': pd.Series(px),
            'Wsp y': pd.Series(py)
}
df = pd.DataFrame.from_dict(moduloP)

noweBtn = st.sidebar.checkbox(label = 'Zaznacz/odznacz wszystkie')
zapiszBtn = st.sidebar.checkbox(label = "Zapisz parametry", value = noweBtn)
daneBtn = st.sidebar.checkbox('Pokaż współrzędne punktów: ', value = noweBtn)
wykresBtn = st.sidebar.checkbox(label = "Wygeneruj wykres: ", value = noweBtn)

if zapiszBtn:
    st.markdown(f'<h5 style="color:#4C3575;font-size:15px;font:"monospace">{"Postać krzywej eliptycznej: "}</h5>',
                unsafe_allow_html=True)
    rownanieZapis(a, b, p)
if daneBtn:
    st.markdown(f'<h5 style="color:#4C3575;font-size:15px;font:"monospace">{"Współrzedne punktów :"}</h5>',
                unsafe_allow_html=True)
    st.write(df.style.background_gradient())


if wykresBtn and zapiszBtn:
    st.markdown(f'<h5 style="color:#4C3575;font-size:15px;font:"monospace">{"Wykres: "}</h5>',
                unsafe_allow_html=True)
    wykres()
if wykresBtn and zapiszBtn == False:
    st.markdown(f'<h5 style="color:#4C3575;font-size:15px;font:"monospace">{"Wykres: "}</h5>',
                unsafe_allow_html=True)
    st.write('Najpierw zapisz')
st.markdown(f'<h2 style="color:#4C3575;font-size:15px;font:"monospace">{"Potęgowanie modulo"}</h2>',
                unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    P = st.number_input(
        label = "Wybor modulo",
        min_value = 1,
        value = 13
    )
with col2:
    g = st.number_input(
        label="Potęga",
        min_value = 1,
        value = 17
    )

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
    st.write(potegiModulo(P, g))
