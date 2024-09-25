import numpy as np 

Go = float(input("Valor Estacionario: "))
MptGo = float(input("Valor SobrePico: "))
tr = float(input("Tiempo de Rise (10'%' - 90'%' del valor estacionario en la respuesta al escalon): "))

#1
chi = 1/np.sqrt(1 + pow(np.pi/np.log(MptGo/Go - 1), 2))
Q = 1/(2*chi)

#2 fn=wo
fn = (0.37*chi*chi + 0.17)/tr
wn = fn*2*np.pi
if (chi >= 1):
    w1 = wn*(np.sqrt(chi*chi - 1) - chi)
    w2 = -wn*(np.sqrt(chi*chi - 1) + chi)
if (chi < 1):
    w1 = wn*(np.sqrt(-chi*chi + 1) - chi)
    w2 = -wn*(np.sqrt(-chi*chi + 1) + chi)

print(f"Chi = {chi}")
print(f"Q = {Q}")
print(f"Wo = {fn*2*np.pi}")
print(f"Tiempo de 'Settlement': {1/(np.pi*chi*fn)}")
print(f"Polo 1: {w1} rad/seg \n Polo 2: {w2} rad/seg")