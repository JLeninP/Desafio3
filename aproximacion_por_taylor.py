import sys
import sympy as sp

# Carga de un capacitor en un punto entre 
# t=0 y t > 0, este estado es llamado estado transitorio.

# q(t) = Q(1 - e^(-t/RC)) [Coulombios]

# C: Valor de la capacitancia del capacitor [F]
# Q: Carga máxima del capacitor [Coulombios]
# R: Valor de la resistencia del resistor [ohm]
#C, Q, R y e son constantes.

t: object = sp.symbols('t', real = True)

e: float = sp.E
C: float = sp.S(0.1)
Q: float = sp.S(1)
R: float = sp.S(20)

q: object = Q * (1 - e**(-t/(R*C)))

#Entrada de Datos 
sys.stdout.write("\n\t-Ingresar valores separados por espacios (a b c).")
sys.stdout.write("\n\t-Usar punto para valores con decimales (0.1).")
sys.stdout.write("\n\nIngresar t0, t1 y n(orden de aproximación): ")

L: list[float] = list(map(float, sys.stdin.readline().split()))

t0: float = L[0]
t1: float = L[1]
n: int = int(L[2]) + 1#Sumado 1 porque python no toma el ultimo valor del rango
h: float = t1 - t0

qi = q

sys.stdout.write(F'\nORDEN\tt0\tt1\th\tq(t1)\t\t\tRn')
for i in range(n):
    q_prima = sp.diff(q, t, i + 1)
    
    Rn = q_prima * h**(i + 1) / sp.factorial(i + 1)
    sys.stdout.write(F'\n{i}\t{t0}\t{t1}\t{h}\t{sp.N(qi.subs({t:t0}))}\t{abs(sp.N(Rn.subs({t:t0})))}')
    qi += Rn

sys.stdout.write('\n--------------------Fin de programa--------------------\n')