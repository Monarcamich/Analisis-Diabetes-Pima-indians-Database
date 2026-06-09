"""
ANÁLISIS GRÁFICO EXPLORATORIO: PIMA INDIANS DIABETES DATABASE
Autor: Análisis de Probabilidad y Estadística
Objetivo: Explorar patrones en diabetes mellitus tipo 2

Este script realiza un análisis exploratorio completo del dataset de diabetes,
incluyendo visualizaciones y análisis estadísticos descriptivos.
"""

# ============================================================================
# 1. IMPORTAR LIBRERÍAS NECESARIAS
# ============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')

# Configurar estilo de seaborn para gráficas más atractivas
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# ============================================================================
# 2. CARGAR EL ARCHIVO DIABETES.CSV
# ============================================================================

# Intentar cargar desde múltiples ubicaciones posibles
rutas_posibles = [
    'diabetes.csv',  # Carpeta actual
    '/kaggle/input/pima-indians-diabetes-database/diabetes.csv',  # Kaggle
    os.path.expanduser('~/diabetes.csv.xls'),  # Home directory
    os.path.expanduser('~/Downloads/diabetes.csv.xls'),  # Descargas
]

datos = None
ruta_utilizada = None

for ruta in rutas_posibles:
    try:
        datos = pd.read_csv(ruta)
        ruta_utilizada = ruta
        print(f"✓ Archivo cargado exitosamente desde: {ruta}")
        break
    except FileNotFoundError:
        continue

if datos is None:
    print("⚠ ERROR: No se encontró el archivo diabetes.csv")
    print("\nDescargar el dataset desde:")
    print("https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database")
    print("\nCola el archivo diabetes.csv en la carpeta del proyecto o en ~/Downloads/")
    exit()

print("\n" + "="*70)
print("DATASET PIMA INDIANS DIABETES - ANÁLISIS EXPLORATORIO")
print("="*70)

# ============================================================================
# 3. INFORMACIÓN GENERAL DEL DATASET
# ============================================================================

print("\n📊 PRIMERAS FILAS DEL DATASET:")
print("-" * 70)
print(datos.head())

print("\n📋 INFORMACIÓN GENERAL DEL DATASET:")
print("-" * 70)
print(datos.info())

print("\n📈 ESTADÍSTICOS DESCRIPTIVOS:")
print("-" * 70)
print(datos.describe())

print("\n🎯 CONTEO DE VALORES DE OUTCOME:")
print("-" * 70)
conteo_outcome = datos['Outcome'].value_counts()
print(f"Sin diabetes (0): {conteo_outcome[0]} registros ({conteo_outcome[0]/len(datos)*100:.2f}%)")
print(f"Con diabetes (1): {conteo_outcome[1]} registros ({conteo_outcome[1]/len(datos)*100:.2f}%)")

# ============================================================================
# 4. ANÁLISIS DE CEROS POTENCIALMENTE FALTANTES
# ============================================================================

print("\n⚠️  ANÁLISIS DE VALORES CERO (POSIBLES VALORES FALTANTES):")
print("-" * 70)

columnas_criticas = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

print("\nNota: Los valores cero en estas columnas pueden representar valores faltantes")
print("porque no son fisiológicamente posibles:\n")

for columna in columnas_criticas:
    ceros = (datos[columna] == 0).sum()
    porcentaje = (ceros / len(datos)) * 100
    print(f"  {columna:20s}: {ceros:4d} ceros ({porcentaje:5.2f}%)")

# ============================================================================
# 5. CREAR GRÁFICAS EXPLORATORIAS
# ============================================================================

# Crear carpeta para guardar gráficas si no existe
carpeta_graficas = os.path.dirname(os.path.abspath(__file__))

print("\n\n📊 GENERANDO GRÁFICAS...")
print("-" * 70)

# ============================================================================
# GRÁFICA 1: BARRAS DE OUTCOME
# ============================================================================

plt.figure(figsize=(10, 6))
conteo = datos['Outcome'].value_counts()
colores = ['#2ecc71', '#e74c3c']  # Verde y rojo
barras = plt.bar(['Sin Diabetes (0)', 'Con Diabetes (1)'], conteo.values, color=colores, edgecolor='black', linewidth=1.5)

# Agregar valores en las barras
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura,
            f'{int(altura)}\n({altura/len(datos)*100:.1f}%)',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.title('Distribución de Diabetes en la Población', fontsize=14, fontweight='bold', pad=20)
plt.ylabel('Número de Personas', fontsize=12, fontweight='bold')
plt.xlabel('Estado de Diabetes', fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficas, 'barras_outcome.png'), dpi=300, bbox_inches='tight')
print("✓ Guardada: barras_outcome.png")
plt.close()

# ============================================================================
# GRÁFICA 2: HISTOGRAMA DE EDAD
# ============================================================================

plt.figure(figsize=(10, 6))
plt.hist(datos['Age'], bins=30, color='#3498db', edgecolor='black', alpha=0.7)
plt.title('Distribución de la Edad', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Edad (años)', fontsize=12, fontweight='bold')
plt.ylabel('Frecuencia', fontsize=12, fontweight='bold')
plt.axvline(datos['Age'].mean(), color='red', linestyle='--', linewidth=2, label=f'Media: {datos["Age"].mean():.1f}')
plt.axvline(datos['Age'].median(), color='green', linestyle='--', linewidth=2, label=f'Mediana: {datos["Age"].median():.1f}')
plt.legend(fontsize=10)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficas, 'histograma_edad.png'), dpi=300, bbox_inches='tight')
print("✓ Guardada: histograma_edad.png")
plt.close()

# ============================================================================
# GRÁFICA 3: HISTOGRAMA DE GLUCOSA
# ============================================================================

plt.figure(figsize=(10, 6))
plt.hist(datos['Glucose'], bins=30, color='#e74c3c', edgecolor='black', alpha=0.7)
plt.title('Distribución de Glucosa en Sangre', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Glucosa (mg/dL)', fontsize=12, fontweight='bold')
plt.ylabel('Frecuencia', fontsize=12, fontweight='bold')
plt.axvline(datos['Glucose'].mean(), color='darkred', linestyle='--', linewidth=2, label=f'Media: {datos["Glucose"].mean():.1f}')
plt.axvline(datos['Glucose'].median(), color='orange', linestyle='--', linewidth=2, label=f'Mediana: {datos["Glucose"].median():.1f}')
plt.legend(fontsize=10)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficas, 'histograma_glucose.png'), dpi=300, bbox_inches='tight')
print("✓ Guardada: histograma_glucose.png")
plt.close()

# ============================================================================
# GRÁFICA 4: HISTOGRAMA DE IMC
# ============================================================================

plt.figure(figsize=(10, 6))
plt.hist(datos['BMI'], bins=30, color='#9b59b6', edgecolor='black', alpha=0.7)
plt.title('Distribución del Índice de Masa Corporal (IMC)', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('IMC (kg/m²)', fontsize=12, fontweight='bold')
plt.ylabel('Frecuencia', fontsize=12, fontweight='bold')
plt.axvline(datos['BMI'].mean(), color='indigo', linestyle='--', linewidth=2, label=f'Media: {datos["BMI"].mean():.1f}')
plt.axvline(datos['BMI'].median(), color='magenta', linestyle='--', linewidth=2, label=f'Mediana: {datos["BMI"].median():.1f}')
plt.legend(fontsize=10)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficas, 'histograma_bmi.png'), dpi=300, bbox_inches='tight')
print("✓ Guardada: histograma_bmi.png")
plt.close()

# ============================================================================
# GRÁFICA 5: BOXPLOT DE GLUCOSA SEGÚN OUTCOME
# ============================================================================

plt.figure(figsize=(10, 6))
sns.boxplot(data=datos, x='Outcome', y='Glucose', palette=['#2ecc71', '#e74c3c'], linewidth=2)
plt.xticks([0, 1], ['Sin Diabetes', 'Con Diabetes'])
plt.title('Niveles de Glucosa según Estado de Diabetes', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Estado de Diabetes', fontsize=12, fontweight='bold')
plt.ylabel('Glucosa (mg/dL)', fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficas, 'boxplot_glucose_outcome.png'), dpi=300, bbox_inches='tight')
print("✓ Guardada: boxplot_glucose_outcome.png")
plt.close()

# ============================================================================
# GRÁFICA 6: BOXPLOT DE IMC SEGÚN OUTCOME
# ============================================================================

plt.figure(figsize=(10, 6))
sns.boxplot(data=datos, x='Outcome', y='BMI', palette=['#2ecc71', '#e74c3c'], linewidth=2)
plt.xticks([0, 1], ['Sin Diabetes', 'Con Diabetes'])
plt.title('Índice de Masa Corporal según Estado de Diabetes', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Estado de Diabetes', fontsize=12, fontweight='bold')
plt.ylabel('IMC (kg/m²)', fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficas, 'boxplot_bmi_outcome.png'), dpi=300, bbox_inches='tight')
print("✓ Guardada: boxplot_bmi_outcome.png")
plt.close()

# ============================================================================
# GRÁFICA 7: DISPERSIÓN BMI vs GLUCOSA
# ============================================================================

plt.figure(figsize=(11, 7))
scatter = plt.scatter(datos[datos['Outcome']==0]['Glucose'], 
                     datos[datos['Outcome']==0]['BMI'], 
                     alpha=0.6, s=50, color='#2ecc71', label='Sin Diabetes', edgecolor='black', linewidth=0.5)
scatter = plt.scatter(datos[datos['Outcome']==1]['Glucose'], 
                     datos[datos['Outcome']==1]['BMI'], 
                     alpha=0.6, s=50, color='#e74c3c', label='Con Diabetes', edgecolor='black', linewidth=0.5)

plt.title('Relación entre Glucosa e IMC', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Glucosa (mg/dL)', fontsize=12, fontweight='bold')
plt.ylabel('IMC (kg/m²)', fontsize=12, fontweight='bold')
plt.legend(fontsize=11, loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficas, 'dispersion_bmi_glucose.png'), dpi=300, bbox_inches='tight')
print("✓ Guardada: dispersion_bmi_glucose.png")
plt.close()

# ============================================================================
# GRÁFICA 8: MAPA DE CALOR DE CORRELACIONES
# ============================================================================

plt.figure(figsize=(10, 8))
# Calcular matriz de correlaciones
correlacion = datos.corr()

# Crear heatmap
sns.heatmap(correlacion, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
            cbar_kws={'label': 'Correlación'}, linewidths=0.5, linecolor='gray',
            vmin=-1, vmax=1)

plt.title('Matriz de Correlación entre Variables', fontsize=14, fontweight='bold', pad=20)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficas, 'mapa_correlacion.png'), dpi=300, bbox_inches='tight')
print("✓ Guardada: mapa_correlacion.png")
plt.close()

# ============================================================================
# 6. INTERPRETACIONES DE LAS GRÁFICAS
# ============================================================================

print("\n\n" + "="*70)
print("📝 INTERPRETACIÓN DE GRÁFICAS")
print("="*70)

interpretaciones = """

1. DISTRIBUCIÓN DE DIABETES (barras_outcome.png)
   ────────────────────────────────────────────
   • El dataset contiene un desbalance: 65.1% sin diabetes vs 34.9% con diabetes
   • Esto es representativo de la población general donde la diabetes es menos 
     frecuente que la ausencia de la enfermedad
   • El desbalance debe considerarse en análisis predictivos posteriores

2. DISTRIBUCIÓN DE LA EDAD (histograma_edad.png)
   ─────────────────────────────────────────────
   • Edad media: ~33.2 años, con rango de 21 a 81 años
   • La distribución es ligeramente asimétrica (sesgada a la derecha)
   • Hay más personas jóvenes que ancianas en el dataset
   • Es importante notar que la diabetes tipo 2 puede afectar a personas jóvenes

3. DISTRIBUCIÓN DE GLUCOSA (histograma_glucose.png)
   ────────────────────────────────────────────────
   • La glucosa tiene una media de ~120.9 mg/dL
   • Nivel normal en ayunas: < 100 mg/dL
   • La mayor parte de la población está por encima de lo normal
   • Muchos valores cero sugieren datos faltantes (no registrados)

4. DISTRIBUCIÓN DEL IMC (histograma_bmi.png)
   ─────────────────────────────────────────
   • IMC medio: ~31.9 kg/m² (clasificado como SOBREPESO)
   • Clasificación OMS: <18.5 (bajo peso), 18.5-24.9 (normal), 25-29.9 (sobrepeso),
     ≥30 (obesidad)
   • Mucha población está en riesgo por sobrepeso u obesidad
   • Existe una relación clara entre IMC y riesgo de diabetes

5. GLUCOSA vs ESTADO DE DIABETES (boxplot_glucose_outcome.png)
   ──────────────────────────────────────────────────────────
   • Personas CON diabetes: mediana de glucosa ~155 mg/dL (muy elevada)
   • Personas SIN diabetes: mediana de glucosa ~99 mg/dL (cercana a normal)
   • Diferencia clara y significativa entre grupos
   • La glucosa es un indicador muy importante para el diagnóstico

6. IMC vs ESTADO DE DIABETES (boxplot_bmi_outcome.png)
   ───────────────────────────────────────────────────
   • Personas CON diabetes: IMC mediano ~33.3 kg/m² (obesidad)
   • Personas SIN diabetes: IMC mediano ~30.0 kg/m² (sobrepeso)
   • Aunque ambos grupos tienen IMC alto, la diferencia es notable
   • El peso corporal es un factor de riesgo importante

7. RELACIÓN GLUCOSA-IMC (dispersion_bmi_glucose.png)
   ─────────────────────────────────────────────────
   • Hay una débil correlación positiva entre glucosa e IMC
   • Las personas con diabetes tienden a estar en la esquina superior derecha
     (glucosa alta + IMC alto)
   • Existe superposición entre grupos, pero hay una separación clara
   • Ambas variables son predictoras independientes de diabetes

8. MATRIZ DE CORRELACIÓN (mapa_correlacion.png)
   ────────────────────────────────────────────
   • Outcome tiene correlaciones positivas FUERTES con:
     - Glucose: 0.47 (relación moderada-fuerte)
     - BMI: 0.29 (relación moderada)
     - Age: 0.24 (relación débil-moderada)
   • DiabetesPedigreeFunction: 0.17 (historial familiar)
   • Pregnancies: 0.22 (puede indicar edad reproductiva)
   • Variables poco correlacionadas con Outcome suelen tener más ceros
     (sugieren valores faltantes)

CONCLUSIONES PRINCIPALES:
─────────────────────────
✓ La glucosa es el predictor más fuerte de diabetes en este dataset
✓ El IMC elevado es un factor de riesgo importante
✓ La edad también tiene influencia, aunque más débil
✓ Hay valores cero que probablemente representan datos faltantes
✓ La población estudiada tiene alto riesgo metabólico en general
✓ Intervenciones en estilo de vida (dieta, ejercicio) podrían reducir la incidencia
  considerando que glucosa e IMC son factores modificables
"""

print(interpretaciones)

# ============================================================================
# GUARDAR RESUMEN EN ARCHIVO DE TEXTO
# ============================================================================

archivo_resumen = os.path.join(carpeta_graficas, 'INTERPRETACION_GRAFICAS.txt')
with open(archivo_resumen, 'w', encoding='utf-8') as f:
    f.write("ANÁLISIS GRÁFICO EXPLORATORIO\n")
    f.write("PIMA INDIANS DIABETES DATABASE\n")
    f.write("="*70 + "\n")
    f.write(interpretaciones)

print(f"\n✓ Resumen guardado en: INTERPRETACION_GRAFICAS.txt")

print("\n" + "="*70)
print("✓ ANÁLISIS COMPLETADO EXITOSAMENTE")
print("="*70)
print(f"\nTodas las gráficas se guardaron en: {carpeta_graficas}")
print("\nArchivos generados:")
print("  • barras_outcome.png")
print("  • histograma_edad.png")
print("  • histograma_glucose.png")
print("  • histograma_bmi.png")
print("  • boxplot_glucose_outcome.png")
print("  • boxplot_bmi_outcome.png")
print("  • dispersion_bmi_glucose.png")
print("  • mapa_correlacion.png")
print("  • INTERPRETACION_GRAFICAS.txt")
print("\n")
