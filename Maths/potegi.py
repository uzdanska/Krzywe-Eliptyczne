import pandas as pd
import streamlit as st
import pandas as pd
def potegiModulo(p, g):
    # liczbyM = []
    # for i in range(1, p):
    #     st.write('{}^({}) = {} mod {}'.format(g, i , g**i%p,p))
    #     liczbyM.append(g**i % p)
    # dfPotegiMod = pd.DataFrame
    return '{}^({}) = {} mod {}'.format(int(g), int(p - 1), int(g) ** int((p - 1)) % int(p), int(p))

# potegiModulo(53, 2)

# liczbyModulo = []
# for i in range(1, 53):
#     print('2^(' + str(i) + ') = ' + str(2**i % 53) +  ' mod 53')
#     liczbyModulo.append(2**i % 53)

# # print(liczbyModulo)

# print(sorted(liczbyModulo))


## algorytm ElGamala
# # print(2**13 % 53)
# # x = 16 *(32**7)
# # print(x % 53)
# # print(2**5 % 53)
# # print(30**5 % 53)
# p, g, a, b, m = 53, 2, 5, 7, 16
# A = g**a
# print('A = ' +  str(A))
# c1 = g**b % p
# c2 = m*(A**b)% p
# print('(', c1, ', ', c2, ')')
# g57 = c1**a % p
# print(g57)
# x = 22 *(-8)
# y = 23 * 45
# print(y % 53)
