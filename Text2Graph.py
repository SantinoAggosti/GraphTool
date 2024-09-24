import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo ignorando las líneas que no son datos
file_path = 'C:/Users/santi/OneDrive/Escritorio/ITBA/TC2/TP3-TC2/Ejercicio2/Simulaciones/CircuitoSinCompensar.txt'  # Cambia esto por la ruta correcta de tu archivo

# Leer el archivo, ignorando las líneas que comienzan con "Step Information"
data = pd.read_csv(file_path, sep='\t', comment='S', header=None, names=['time', 'V(n006)'])

# Limpiar los datos quitando filas que contienen encabezados adicionales
data = data[pd.to_numeric(data['time'], errors='coerce').notnull()]

#Para ignorar puntos previos
offset = 15

title = input("Title: ")


print("T/t for time, F/f for frequency[hz], W/w for frequency[rad/seg]")

xLabel = input("X Label: ")
yLabel = input("Y Label: ")

if (xLabel == 'T' or xLabel == 't'):
    xLabel = "Tiempo [seg]"
elif (xLabel == 'F' or xLabel == 'f'):
    yLabel = "Frecuencia [Hz]"
elif (xLabel == 'W' or xLabel == 'w'):
    yLabel = "Frecuencia [rad/seg]"
if (yLabel == 'V' or yLabel == 'v'):
    yLabel = "Diferencia de Potencial [V]"

xVar = input("X variable Name (Just like in text file): ")
yVar = input("Y variable Name (Just like in text file): ")
nCurves = input("Number of Curves: ")
nCurves = int(nCurves)
labels = ["", "", ""]
for i in range(nCurves):
    label = input(f"Label {i}:")
    labels[i] = label

# Convertir a tipo numérico para asegurar que los datos sean correctos
data[xVar] = pd.to_numeric(data[xVar])
data[yVar] = pd.to_numeric(data[yVar])
plt.figure(figsize=(10, 6))
for i in range(nCurves):
    i = i + 1
    datapoints = int(len(data[xVar])/3)
    print(datapoints)
    # Graficar los datos
    plt.plot(data[xVar][datapoints*(i-1) + offset:datapoints*i], data[yVar][datapoints*(i-1) + offset:datapoints*i], label = labels[i-1])
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
plt.show()