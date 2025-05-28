import pandas as pd
df = pd.read_csv(r"C:\Users\silvi\Downloads\ventas.csv")
#METODOS 
print(df.columns) #veo las columnas
print(df.dtypes) #veo los tipos de datos, cuando sale object es un string generalmente
print(df["Vendedor"]) #veo la columna vendedor

#Metodos comunes para manejo de datos
#df.describe() #me devuelve estadisticas de cada columna numerica
#df.describe(include="all") #me devuelve estadisticas de cada columna numerica y de texto
#df.max() #me devuelve el mayor valor de cada columna
#df.min() #me devuelve el menor valor de cada columna
#df.mean() #me devuelve la media de cada columna
#df.tail() #veo los ultimos 5 registros del db
#df.head() #veo los primeros 5 registro del db
#df.sample(5) #me muestra 5 registros aleatorios

#Metodos para ordenar
#Ordeno por Vendedor
print(df.sort_values("Vendedor")) #me ordena por vendedor, ordena de mayor a menor

print(df.sort_values("Vendedor",inplace=True)) #ordena de mayor a menor, 
#inplace=True modifica el df (no modifica el csv,modifica los datos a partir del csv) original, 
# no es muy recomendable
print(df.sort_values("Vendedor",ascending=False)) #ordena de menor a mayor

#Ahora por importes 
print(df.sort_values("Importe")) #me ordena por importe, ordena de menor a mayor
print(df.sort_values("Importe",ascending=False)) #ordena de mayor a menor

#Busco un dato en particular
#BOOLEAN MASKING: cuales son los registros que cumplen con la condicion
#El boolean masking me devuelve una serie booleana, la podemos usar para mostrar
#los datos que cumplen la cond en el df
print(df["Vendedor"]=="Angelita Lambkin")
#mostrar los registros que en esa serie booleana tengan true

print(df[df["Vendedor"]=="Angelita Lambkin"]) 
#me devuelve los registros que cumplen la condicion

#busco los top 3 valores de mayores ventas de angelita
print(df[df["Vendedor"]=="Angelita Lambkin"].sort_values("Importe",ascending=False).head(3)) 
#me devuelve los 3 mayores importes de angelita

#Otra manera es creando una variable y guardandole el filtrado entonces
df_angelita=df[df["Vendedor"]=="Angelita Lambkin"]
df_angelita_ordenado=df_angelita.sort_values("Importe",ascending=False)
print(df_angelita_ordenado.head(3)) #me devuelve los 3 mayores importes de angelita

#Busco vendedor angelita con sede particular
print(df[(df["Vendedor"]=="Angelita Lambkin") & (df["Sede"]=="Boedo")])

#FUNCIONES DE AGREGACION
df.groupby("Vendedor") #me agrupa por vendedor, entonces mantiene 
#los datos de la columna vendedor y me agrega el resto

#MOSTRAR UN DF CON EL IMPORTE TOTAL POR VENDEDOR
#Agrupo por vendedor y luego sumo los importes de ventas,luego ordeno de mayor a menor
df_ventas_vendedor=df.groupby("Vendedor")["Importe"].sum().sort_values(ascending=False)
print(df_ventas_vendedor) 
import pandas as pd
df = pd.read_csv(r"C:\Users\silvi\Downloads\ventas.csv")
#METODOS 
print(df.columns) #veo las columnas
print(df.dtypes) #veo los tipos de datos, cuando sale object es un string generalmente
print(df["Vendedor"]) #veo la columna vendedor

#Metodos comunes para manejo de datos
#df.describe() #me devuelve estadisticas de cada columna numerica
#df.describe(include="all") #me devuelve estadisticas de cada columna numerica y de texto
#df.max() #me devuelve el mayor valor de cada columna
#df.min() #me devuelve el menor valor de cada columna
#df.mean() #me devuelve la media de cada columna
#df.tail() #veo los ultimos 5 registros del db
#df.head() #veo los primeros 5 registro del db
#df.sample(5) #me muestra 5 registros aleatorios



#Metodos para ordenar
#Ordeno por Vendedor
print(df.sort_values("Vendedor")) #me ordena por vendedor, ordena de mayor a menor

print(df.sort_values("Vendedor",inplace=True)) #ordena de mayor a menor, 
#inplace=True modifica el df (no modifica el csv,modifica los datos a partir del csv) original, 
# no es muy recomendable
print(df.sort_values("Vendedor",ascending=False)) #ordena de menor a mayor

#Ahora por importes 
print(df.sort_values("Importe")) #me ordena por importe, ordena de menor a mayor
print(df.sort_values("Importe",ascending=False)) #ordena de mayor a menor

#Busco un dato en particular
#BOOLEAN MASKING: cuales son los registros que cumplen con la condicion
#El boolean masking me devuelve una serie booleana, la podemos usar para mostrar
#los datos que cumplen la cond en el df
print(df["Vendedor"]=="Angelita Lambkin")
#mostrar los registros que en esa serie booleana tengan true

print(df[df["Vendedor"]=="Angelita Lambkin"]) 
#me devuelve los registros que cumplen la condicion

#busco los top 3 valores de mayores ventas de angelita
print(df[df["Vendedor"]=="Angelita Lambkin"].sort_values("Importe",ascending=False).head(3)) 
#me devuelve los 3 mayores importes de angelita

#Otra manera es creando una variable y guardandole el filtrado entonces
df_angelita=df[df["Vendedor"]=="Angelita Lambkin"]
df_angelita_ordenado=df_angelita.sort_values("Importe",ascending=False)
print(df_angelita_ordenado.head(3)) #me devuelve los 3 mayores importes de angelita

#Busco vendedor angelita con sede particular
print(df[(df["Vendedor"]=="Angelita Lambkin") & (df["Sede"]=="Boedo")])

#FUNCIONES DE AGREGACION
df.groupby("Vendedor") #me agrupa por vendedor, entonces mantiene 
#los datos de la columna vendedor y me agrega el resto

#MOSTRAR UN DF CON EL IMPORTE TOTAL POR VENDEDOR
#Agrupo por vendedor y luego sumo los importes de ventas,luego ordeno de mayor a menor
df_ventas_vendedor=df.groupby("Vendedor")["Importe"].sum().sort_values(ascending=False)
print(df_ventas_vendedor) 