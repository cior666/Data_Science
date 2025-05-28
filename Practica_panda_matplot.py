import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv(r"C:\Users\silvi\OneDrive\Escritorio\Carrera Data Science\BTCUSD_1hr.csv")

#voy a crear un grafico de como evoluciona el precio de btc con el tiempo.
#para eso voy a hacer un grafico de lineas. Entonces
#Primero debo cambiar el dataframe para que la columna "Date" sea de tipo datetime,
df["Date"]=pd.to_datetime(df["Date"])
x=df["Date"].map(pd.Timestamp.toordinal) #esto convierte las fechas a numeros, para poder hacer la regresion lineal
y=df["Close"]
plt.plot(df["Date"], y, color="blue")
plt.xlabel("fecha")
plt.ylabel("precio btc")
plt.title("Evolucion del precio de bitcoin") #titulo del grafico.
#A esto le puedo agregar mas cosas, como ser una linea de tendencia, para ello:
#Linea de tendencia
z=np.polyfit(x, y, 1) #Aca lo que hago es pasarle x e y, y luego defino el grado del polinomio
#de aproximacion, en este caso 1, porque es una linea recta.
p=np.poly1d(z) #hago la recta
plt.plot(df["Date"],p(x),"r--",label="Tendencia",color="red") #pongo la recta en el grafico, con color rojo y linea discontinua

plt.legend()
plt.show() 
