import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url) 

data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)

aux = data['Ubicación del caso'].value_counts()

data.loc[data['Estado'] == 'leve','Estado'] = 'Leve'
data.loc[data['Estado'] == 'LEVE','Estado'] = 'Leve'

data.loc[data['Ubicación del caso'] == 'casa','Ubicación del caso'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA','Ubicación del caso'] = 'Casa'

data.loc[data['Sexo'] == 'm','Sexo'] = 'M'
data.loc[data['Sexo'] == 'f','Sexo'] = 'F'

data.loc[data['Edad'] == 'Casa','Edad'] = 36
data.loc[data['Edad'] == 'Leve','Edad'] = 36
data.loc[data['Edad'] == 'M','Edad'] = 36
data.loc[data['Edad'] == 'F','Edad'] = 36


data.mean()

#1
data['Estado'].count()

#2
data['Nombre municipio'].nunique()

#3
data['Nombre municipio'].value_counts()

#4
aux = data.loc[(data['Ubicación del caso'] == 'Casa')]
NumeroDePersonasEnCasa = aux.shape[0]

#5
aux = data.loc[(data['Recuperado'] == 'Recuperado')]
NumeroDePersonasRecuper = aux.shape[0]

#6
aux = data.loc[(data['Estado'] == 'Fallecido')]
NumeroDePersonasFallecidas = aux.shape[0]

#7
data.sort_values(by=data.loc[(data['Tipo de contagio'] == 'Importado')],ascending=False )
data.sort_values(by=data.loc[(data['Tipo de contagio'] == 'Relacionado')],ascending=False )

#8
data['Nombre departamento'].nunique()

#9
data['Nombre departamento'].value_counts()


#10
data.sort_values(by='Ubicación del caso',ascending=False )

#11
data['Nombre departamento'].value_counts().head(10)

#12
aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size()
aux.sort_values(ascending=False).head(10)

#13
aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre departamento').size()
aux.sort_values(ascending=False).head(10)

#14
data['Nombre municipio'].value_counts().head(10)

#15
aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre municipio').size()
aux.sort_values(ascending=False).head(10)

#16
aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre municipio').size()
aux.sort_values(ascending=False).head(10)

#17
aux = data.groupby(['Nombre departamento', 'Nombre municipio']).size()
aux.sort_values(ascending=False)

#18
aux = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo']).size()
aux.sort_values(ascending=False)

#19
data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo'])['Edad'].mean()

#20
aux = data.groupby(['Nombre del país']).size()
aux.sort_values(ascending=False)

#21
aux = data.groupby(['Fecha de diagnóstico']).size()
aux.sort_values(ascending=False)

#22
cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
cantidad_recuperados = data.query('Recuperado == "Recuperado"').shape[0]
cantidad_casos = data.shape[0]
tasa_mortalidad = cantidad_muertes / cantidad_casos * 100
tasa_recuperacion = cantidad_recuperados / cantidad_casos * 100

#23
cantidad_muertes_dep = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size()
cantidad_recuperados_dep = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size()
cantidad_casos_dep = data.groupby('Nombre departamento').size()
tasa_mortalidad_dep = cantidad_muertes_dep / cantidad_casos_dep * 100
tasa_recuperacion_dep = cantidad_recuperados_dep / cantidad_casos_dep * 100
data2 = pd.DataFrame({'tasa_mortalidad_dep': tasa_mortalidad_dep, 'tasa_recuperacion_dep':tasa_recuperacion_dep})

#24
cantidad_muertes_ciu = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size()
cantidad_recuperados_ciu = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size()
cantidad_casos_ciu = data.groupby('Nombre municipio').size()
tasa_mortalidad_ciu = cantidad_muertes_ciu / cantidad_casos_ciu * 100
tasa_recuperacion_ciu = cantidad_recuperados_ciu / cantidad_casos_ciu * 100
data3 = pd.DataFrame({'tasa_mortalidad_ciu': tasa_mortalidad_ciu, 'tasa_recuperacion_ciu':tasa_recuperacion_ciu})

#25
data.groupby(['Nombre municipio', 'Ubicación del caso']).size()

#26
data.groupby(['Nombre municipio', 'Sexo'])['Edad'].mean()

#27
data[(data['Recuperado'] == 'Recuperado')].groupby('Fecha de diagnóstico').size().plot()
data[(data['Estado'] == 'Fallecido')].groupby('Fecha de diagnóstico').size().plot()

#28
aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size()
aux.sort_values(ascending=False).head(10).plot()
aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre departamento').size()
aux.sort_values(ascending=False).head(10).plot()

#29
aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre municipio').size()
aux.sort_values(ascending=False).head(10).plot()
aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre municipio').size()
aux.sort_values(ascending=False).head(10).plot()

#30
aux = data[(data['Estado'] == 'Fallecido')].groupby('Edad').size()
aux.sort_values(ascending=False).head(10)

#31
data.groupby('Ubicación del caso').mean()

#32
data.groupby('Ubicación del caso').size().plot(kind='bar')

#33
data.groupby('Sexo').size().plot(kind='bar')

#34
data.groupby('Tipo de contagio').size().plot(kind='bar')

#35
data[(data['Recuperado'] == 'Recuperado')].groupby('Fecha de diagnóstico').size().plot(kind='bar')
data[(data['Estado'] == 'Fallecido')].groupby('Fecha de diagnóstico').size().plot(kind='bar')

