from GeneralGraphing import *

def funcionArbitraria(range, Rds):
    enumerador = Rds
    denominador = range
    return enumerador/denominador

rango = realRange(1E-1, 1, False, 500)
funcion = funcionArbitraria(rango, 0.1)
singleGraph(rango, funcion, True, xLabel="$K$ [$log_{10}$]", yLabel="$Z_i$ [$Omega$]", title="$Z_i$/$K$ - Ideal")