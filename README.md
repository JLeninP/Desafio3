---
title: "DESAFIO 3"
subtitle: "Aproximación por Series de Taylor"
author: "Lenin Pocoaca"
date: "2024-09-05"
output: pdf_document
---

# Carga de un capacitor
La carga de un capacitor en un punto entre 
t=0 y t > 0, esta dado por la siguiente función

$$q(t) = Q(1 - e^{-\frac{t}{RC}})$$

Donde:
- $C$: Valor de la capacitancia del capacitor [Faradios]
- $Q$: Carga máxima del capacitor [Coulombios]
- $R$: Valor de la resistencia del resistor [ohmios]

Ademas $C, Q, R \text{ y } e$ son constantes, es decir conocemos su valor.

Para este ejemplo se tomará los siguientes valores:
$$C = 0.1\text{ Faradios}$$
$$Q = 1.0\text{ Coulombios}$$
$$R = 20.0\text{ Ohmios}$$
Con ayuda de la biblioteca $SymPy$ de python, se realizara el calculo de las derivadas de orden $i, i \,\epsilon\,[1, 2, 3, ..., n]$

```{python, collapse = TRUE, echo = FALSE}
import sys
import sympy as sp

t: object = sp.symbols('t', real = True)

e: float = sp.E
C: float = sp.S(0.1)
Q: float = sp.S(1.0)
R: float = sp.S(20.0)

q: object = Q * (1 - e**(-t/(R*C)))
```

Para este ejemplo tomaremos $t_{0}=7$ , para aproximarnos al valor de $t_{1}=8$, usando expansiones de la serie de Taylor con $n$ desde 0 hasta 6. 

```{python, collapse = TRUE, echo = FALSE}
t0: float = 7
t1: float = 8
n: int = 6 + 1#Sumado 1 porque python no toma el ultimo valor del rango
h: float = t1 - t0

q1 = q

sys.stdout.write(F'\nORDEN\tt0\tt1\th\tq(t1)\t\t\tRn')
for i in range(n):
    q_prima = sp.diff(q, t, i + 1)
    
    Rn = q_prima * h**(i + 1) / sp.factorial(i + 1)
    sys.stdout.write(F'\n{i}\t{t0}\t{t1}\t{h}\t{sp.N(qi.subs({t:t0}))}\t{abs(sp.N(Rn.subs({t:t0})))}')
    qi += Rn

sys.stdout.write('\n--------------------Fin de programa--------------------\n')
```
Y se obtiene el siguiente resultado.
```{python, collapse = TRUE, echo = FALSE}
ORDEN   t0      t1      h       q(t1)                   Rn
0       7.0     8.0     1.0     0.969802616577682       0.0150986917111593
1       7.0     8.0     1.0     0.984901308288841       0.00377467292778981
2       7.0     8.0     1.0     0.981126635361051       0.000629112154631635
3       7.0     8.0     1.0     0.981755747515683       0.0000786390193289544
4       7.0     8.0     1.0     0.981677108496354       0.00000786390193289544
5       7.0     8.0     1.0     0.981684972398287       6.55325161074620E-7
6       7.0     8.0     1.0     0.981684317073125       4.68089400767586E-8
--------------------Fin de programa--------------------
```