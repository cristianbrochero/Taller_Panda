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