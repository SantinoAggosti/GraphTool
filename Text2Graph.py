import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo ignorando las líneas que no son datos
file_path = 'C:/Users/santi/OneDrive/Escritorio/ITBA/TC2/TP3-TC2/Ejercicio2/Simulaciones/CircuitoCompensado.txt'  # Cambia esto por la ruta correcta de tu archivo

title = input("Title: ")
print("T/t for time, F/f for frequency[hz], W/w for frequency[rad/seg]")

xLabel = input("X Label: ")
yLabel = input("Y Label: ")

xVar = input("X variable Name (Just like in text file): ")
yVar = input("Y variable Name (Just like in text file): ")

# Leer el archivo y separar los datos en listas cuando aparece una línea que comienza con "S"
data_lists = []
current_data = []

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('S' or 't'):
            if (current_data and len(current_data) > 1):
                data_lists.append(current_data)
                current_data = []
        else:
            current_data.append(line.strip().split('\t'))

if current_data:
    data_lists.append(current_data)  # Asegurarse de agregar la última curva

# Convertir las listas de datos en DataFrames
data_frames = []
for data in data_lists:
    df = pd.DataFrame(data, columns=[xVar, yVar])
    df[xVar] = pd.to_numeric(df[xVar], errors='coerce')
    df[yVar] = pd.to_numeric(df[yVar], errors='coerce')
    df = df.dropna()
    data_frames.append(df)

# Configurar etiquetas de los ejes
if xLabel.lower() == 't':
    xLabel = "Tiempo [seg]"
elif xLabel.lower() == 'f':
    xLabel = "Frecuencia [Hz]"
elif xLabel.lower() == 'w':
    xLabel = "Frecuencia [rad/seg]"

if yLabel.lower() == 'v':
    yLabel = "Diferencia de Potencial [V]"

nCurves = int(input("Number of Curves: "))
labels = [input(f"Label {i}:") for i in range(nCurves)]

# Graficar los datos
plt.figure(figsize=(10, 6))
for i, df in enumerate(data_frames[:nCurves]):
    plt.plot(df[xVar], df[yVar], label=labels[i])

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.grid(True)
plt.show()