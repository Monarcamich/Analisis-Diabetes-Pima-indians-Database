# ANÁLISIS ESTADÍSTICO: DIABETES MELLITUS TIPO 2
## Fundamentos de Probabilidad y Estadística

---

## 1. CONCEPTOS ESTADÍSTICOS CLAVE

### Media (Promedio)
**Fórmula**: x̄ = (Σx) / n

La media representa el valor promedio de una variable. En nuestro análisis:
- Edad media: ~33.2 años
- Glucosa media: ~120.9 mg/dL
- IMC medio: ~31.9 kg/m²

**Interpretación**: Un IMC promedio de 31.9 indica que la población está en riesgo metabólico.

---

### Mediana
**Definición**: El valor que divide el conjunto de datos ordenados en dos partes iguales.

Es más resistente a valores extremos (outliers) que la media.

---

### Desviación Estándar (σ)
**Fórmula**: σ = √[Σ(x - x̄)² / n]

Mide qué tan dispersos están los datos alrededor de la media.

- Valores pequeños: datos concentrados cerca de la media
- Valores grandes: datos muy dispersos

---

### Distribuciones de Probabilidad

#### Distribución Normal (Gaussiana)
Muchas variables biológicas siguen una distribución normal.

**Características**:
- Forma de campana simétrica
- Media = Mediana = Moda
- El 68% de datos está dentro de ±1σ
- El 95% de datos está dentro de ±2σ
- El 99.7% de datos está dentro de ±3σ

**En el dataset**: La glucosa aproxima a una distribución normal, pero con sesgo derecho.

---

## 2. VARIABLES DEL DATASET

### Variables Numéricas Continuas
Pueden tomar cualquier valor dentro de un rango.

- **Glucose**: 0-200 mg/dL
- **BloodPressure**: 0-122 mmHg
- **SkinThickness**: 0-99 mm
- **Insulin**: 0-846 mu U/ml
- **BMI**: 0-67.1 kg/m²
- **Age**: 21-81 años
- **DiabetesPedigreeFunction**: 0.078-2.420

### Variable de Respuesta (Dependiente)
- **Outcome**: Variable binaria (0 o 1)
  - 0 = Sin diabetes (n=500, 65.1%)
  - 1 = Con diabetes (n=268, 34.9%)

---

## 3. MEDIDAS DE ASOCIACIÓN

### Correlación de Pearson (r)
**Fórmula**: r = Cov(X,Y) / (σₓ × σᵧ)

Rango: -1 a +1

- **r > 0**: Correlación positiva (cuando X ↑, Y ↑)
- **r < 0**: Correlación negativa (cuando X ↑, Y ↓)
- **|r| = 1**: Correlación perfecta
- **|r| = 0**: Sin correlación

**Interpretación de magnitud**:
- 0.0 - 0.3: Débil
- 0.3 - 0.7: Moderada
- 0.7 - 1.0: Fuerte

**En el análisis**:
- Glucose - Outcome: r ≈ 0.47 (correlación moderada-fuerte)
- BMI - Outcome: r ≈ 0.29 (correlación débil-moderada)
- Age - Outcome: r ≈ 0.24 (correlación débil)

---

## 4. ANÁLISIS DE DIFERENCIAS ENTRE GRUPOS

### Boxplot (Diagrama de Cajas)
Representa cinco valores descriptivos:

```
        │─────Q3─────│  Bigote (1.5×IQR)
        │      │      │
    ────┼──────┼──────┼────
        │      │      │
Mínimo  Q1   Mediana Q3   Máximo
        └─ Valores atípicos (outliers)
```

Donde:
- **Q1**: Primer cuartil (25%)
- **Mediana**: Segundo cuartil (50%)
- **Q3**: Tercer cuartil (75%)
- **IQR**: Rango intercuartil = Q3 - Q1

**Interpretación en diabetes**:
- La mediana de glucosa es MUCHO MÁS ALTA en diabéticos
- Hay mayor variabilidad en el grupo con diabetes
- Esto indica que la glucosa es un factor discriminante

---

### Prueba t de Student
Compara las medias de dos grupos independientes.

**Hipótesis**:
- H₀: No hay diferencia significativa entre grupos
- H₁: Hay diferencia significativa

**En el análisis de diabetes**:
- La diferencia de glucosa entre grupos es ESTADÍSTICAMENTE SIGNIFICATIVA (p < 0.001)
- La diferencia de IMC entre grupos también es significativa

---

## 5. ANÁLISIS BIVARIADO

### Gráficas de Dispersión (Scatterplot)
Muestran la relación entre dos variables continuas.

**En BMI vs Glucose**:
- Relación positiva débil (r ≈ 0.22)
- Pero cuando se colorean por Outcome, se ve una separación clara
- Las personas con diabetes tienden a estar en valores altos de ambas variables

---

### Matriz de Correlaciones
Resume todas las correlaciones entre pares de variables.

**Interpretación**:
- Valores cercanos a +1 (rojo oscuro): Correlaciones positivas fuertes
- Valores cercanos a -1 (azul oscuro): Correlaciones negativas fuertes
- Valores cercanos a 0 (blanco): Sin correlación

---

## 6. CEROS COMO VALORES FALTANTES

### El Problema
Variables como Glucose y BMI no pueden ser cero en la realidad humana.

- **Glucosa normal**: 70-100 mg/dL en ayunas
- **BMI mínimo viable**: ~12 (persona muy delgada)
- **Presión arterial**: Nunca es 0 en un vivo

### Proporción de Ceros Detectados
```
Glucose:       5 ceros (0.65%)
BloodPressure: 35 ceros (4.56%)
SkinThickness: 227 ceros (29.5%)
Insulin:       374 ceros (48.7%)
BMI:           11 ceros (1.43%)
```

### Impacto Estadístico
- Los ceros sesgan la distribución hacia la izquierda
- Reducen la media observada
- Aumentan la proporción de "valores bajos"

### Manejo Recomendado
Para análisis más precisos:
```python
# Filtrar datos válidos (eliminar ceros)
datos_limpios = datos[
    (datos['Glucose'] > 0) &
    (datos['BloodPressure'] > 0) &
    (datos['BMI'] > 0) &
    (datos['SkinThickness'] > 0) &
    (datos['Insulin'] > 0)
]
```

---

## 7. FACTORES DE RIESGO DE DIABETES MELLITUS TIPO 2

### Orden de Importancia (según correlación con Outcome)

1. **Glucose** (r = 0.47)
   - Principal biomarcador
   - Elevación indica hiperglucemia
   - Reversible con intervención temprana

2. **BMI** (r = 0.29)
   - Sobrepeso y obesidad son factores de riesgo
   - Modificable con dieta y ejercicio

3. **Age** (r = 0.24)
   - Mayor riesgo con la edad
   - No modificable directamente

4. **DiabetesPedigreeFunction** (r = 0.17)
   - Predisposición genética
   - No modificable

5. **Pregnancies** (r = 0.22)
   - Puede indicar edad reproductiva y cambios metabólicos
   - Relacionado indirectamente con edad

---

## 8. MODELOS ESTADÍSTICOS APLICABLES

### Regresión Logística
Predice la probabilidad de presencia/ausencia de diabetes.

**Modelo**: log(P/(1-P)) = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ

Donde:
- P = Probabilidad de diabetes
- X₁, X₂, ..., Xₙ = Variables predictoras
- β = Coeficientes de regresión

---

### Análisis Discriminante
Encuentra la mejor separación lineal entre grupos.

Ideal cuando:
- Datos aproximan distribución normal
- Varianzas son homogéneas entre grupos

---

### Árboles de Decisión
Clasifica usando reglas simples e interpretables.

Ejemplo:
```
¿Glucose > 127?
├─ Sí → ¿IMC > 29.9?
│      ├─ Sí → DIABETES (85% probabilidad)
│      └─ No → PROBABLEMENTE NO DIABETES
└─ No → PROBABLEMENTE NO DIABETES
```

---

## 9. PRUEBAS DE HIPÓTESIS

### Prueba Chi-Cuadrado (χ²)
Compara distribuciones de variables categóricas.

**En diabetes**:
```
H₀: La presencia de diabetes es independiente de la edad
H₁: Existe dependencia
```

Resultado: La edad y la diabetes NO son independientes (p < 0.05)

---

### Prueba de Normalidad (Shapiro-Wilk)
Verifica si una variable sigue distribución normal.

```python
from scipy import stats
stat, p = stats.shapiro(datos['Glucose'])
if p > 0.05:
    print("Es normal")
else:
    print("No es normal")
```

---

## 10. INTERVALOS DE CONFIANZA

### Intervalo de Confianza al 95%
Rango probable donde cae el parámetro poblacional real.

**Fórmula**: x̄ ± 1.96 × (σ/√n)

**Interpretación**:
- Si repetimos el estudio 100 veces, en 95 ocasiones el parámetro caerá dentro del intervalo
- Es más informativo que un simple promedio

**Ejemplo en Glucosa**:
```
IC 95% = 120.9 ± 5.8 = [115.1 - 126.7] mg/dL
```

---

## 11. TAMAÑO DE EFECTO

### Cohen's d (para diferencias entre grupos)
**Fórmula**: d = (μ₁ - μ₂) / σ

Interpretación:
- d < 0.2: Efecto pequeño
- 0.2 ≤ d < 0.5: Efecto pequeño-medio
- 0.5 ≤ d < 0.8: Efecto medio-grande
- d ≥ 0.8: Efecto grande

En diabetes:
- La diferencia de glucosa entre grupos tiene efecto GRANDE
- La diferencia de IMC tiene efecto MEDIO

---

## 12. PROBABILIDADES IMPORTANTES

### Prevalencia de Diabetes en el Dataset
P(Diabetes) = 268/768 = 0.349 = 34.9%

### Glucosa Alta dado Diabetes
De las personas con diabetes, qué porcentaje tiene glucosa > 150?

```python
# P(Glucose > 150 | Outcome = 1)
diabeticos = datos[datos['Outcome'] == 1]
glucosa_alta_diabeticos = (diabeticos['Glucose'] > 150).sum()
probabilidad = glucosa_alta_diabeticos / len(diabeticos)
```

---

## 13. RECOMENDACIONES PARA EL PROYECTO

### Estructura de Reporte Sugerida

1. **Introducción**
   - ¿Qué es Diabetes Mellitus Tipo 2?
   - Importancia del problema
   - Objetivos del análisis

2. **Metodología**
   - Descripción del dataset
   - Variables estudiadas
   - Técnicas estadísticas aplicadas

3. **Resultados**
   - Estadística descriptiva
   - Visualizaciones (8 gráficas)
   - Análisis de correlaciones

4. **Interpretación**
   - Factores de riesgo identificados
   - Comparación entre grupos
   - Patrones observados

5. **Conclusiones**
   - Hallazgos principales
   - Implicaciones prácticas
   - Limitaciones del estudio
   - Recomendaciones futuras

---

## 14. REFERENCIAS ACADÉMICAS

- **Epidemiología**: Epidemiología básica. Beaglehole, Bonita, Kjellström.
- **Estadística**: Probabilidad y Estadística para Ingenieros. Walpole, Myers, Myers.
- **Metodología**: Research Methods in Statistics. Bryman & Bell.
- **Diabetes**: American Diabetes Association Standards of Care.

---

**Documento preparado para**: Proyecto U1 - Probabilidad y Estadística
**Tema**: Diabetes Mellitus Tipo 2
**Fecha**: 2026-06-09
**Nivel**: Educación Superior (Pregrado)
