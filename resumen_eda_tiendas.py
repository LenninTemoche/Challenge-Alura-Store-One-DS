# Dataframe resumen de análisis exploratorio de las 4 tiendas
# Este código corrige los errores de nombres de columnas

import pandas as pd

def crear_resumen_eda(tienda_1, tienda_2, tienda_3, tienda_4):
    """
    Crea un DataFrame resumen con el análisis exploratorio de las 4 tiendas
    """
    tiendas = {
        "Tienda 1": tienda_1,
        "Tienda 2": tienda_2,
        "Tienda 3": tienda_3,
        "Tienda 4": tienda_4
    }
    
    def resumen_eda(df, nombre_tienda):
        return {
            "Tienda": nombre_tienda,
            "Total Registros": df.shape[0],
            "Filas Duplicadas": df.duplicated().sum(),
            "Valores Nulos": df.isnull().sum().sum(),
            "Precio Promedio": round(df["Precio"].mean(), 2),
            "Precio Mínimo": df["Precio"].min(),
            "Precio Máximo": df["Precio"].max(),
            "Costo Envío Promedio": round(df["Costo de envío"].mean(), 2),
            "Costo Envío Mínimo": df["Costo de envío"].min(),
            "Costo Envío Máximo": df["Costo de envío"].max(),
            "Calificación Promedio": round(df["Calificación"].mean(), 2),
            "Calificación Mínima": df["Calificación"].min(),
            "Calificación Máxima": df["Calificación"].max(),
            "Productos Únicos": df["Producto"].nunique(),
            "Categorías Únicas": df["Categoría del Producto"].nunique(),
            "Vendedores Únicos": df["Vendedor"].nunique(),
            "Fecha Inicio": df["Fecha de Compra"].min(),
            "Fecha Fin": df["Fecha de Compra"].max()
        }
    
    # Crear lista con resumen de cada tienda
    all_eda_data = []
    
    for nombre_tienda, df in tiendas.items():
        all_eda_data.append(resumen_eda(df, nombre_tienda))
    
    # Crear DataFrame resumen
    summary_df = pd.DataFrame(all_eda_data)
    
    return summary_df


# Código para usar en el notebook:
"""
# Importar la función
from resumen_eda_tiendas import crear_resumen_eda

# Crear el resumen
summary_df = crear_resumen_eda(tienda_1, tienda_2, tienda_3, tienda_4)

# Mostrar el resumen
print("\n" + "="*80)
print("RESUMEN DEL ANÁLISIS EXPLORATORIO DE LAS 4 TIENDAS - ALURA STORE LATAM")
print("="*80 + "\n")
display(summary_df)

# Mostrar estadísticas adicionales
print("\n" + "="*80)
print("ESTADÍSTICAS CONSOLIDADAS")
print("="*80)
print(f"Total de registros en todas las tiendas: {summary_df['Total Registros'].sum():,}")
print(f"Precio promedio general: ${summary_df['Precio Promedio'].mean():,.2f}")
print(f"Calificación promedio general: {summary_df['Calificación Promedio'].mean():.2f}")
print(f"Costo de envío promedio general: ${summary_df['Costo Envío Promedio'].mean():,.2f}")
"""
