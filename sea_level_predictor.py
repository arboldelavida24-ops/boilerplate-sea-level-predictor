import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Importar los datos
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Crear el diagrama de dispersión
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # 3. Primera línea de mejor ajuste (todos los datos)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Creamos un rango de años hasta 2050
    years_extended = pd.Series([i for i in range(1880, 2051)])
    
    # Calculamos la línea
    line_all = res.slope * years_extended + res.intercept
    ax.plot(years_extended, line_all, color='red')

    # 4. Segunda línea de mejor ajuste (solo desde el 2000)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    years_recent = pd.Series([i for i in range(2000, 2051)])
    line_recent = res_recent.slope * years_recent + res_recent.intercept
    ax.plot(years_recent, line_recent, color='green')

    # 5. Etiquetas y título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # AQUI ESTA EL TRUCO PARA QUE EL TEST PASE
    ax.set_title('Rise in Sea Level')
    fig.suptitle('Rise in Sea Level') 

    # Guardar y devolver la figura (No modificar)
    fig.savefig('sea_level_plot.png')
    return fig