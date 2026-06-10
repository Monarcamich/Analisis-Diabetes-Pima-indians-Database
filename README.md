# ANÁLISIS DE DIABETES - GUÍA DE INSTALACIÓN Y EJECUCIÓN

## 📥 PASO 1: Descargar el Dataset

### Opción A: Desde Kaggle (Recomendado)

1. Visita: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
2. Haz clic en el botón **"Download"** (esquina superior derecha)
3. El archivo `diabetes.csv` se descargará a tu carpeta de Descargas
4. **Mueve o copia** el archivo a esta carpeta del proyecto:
   ```
   ~/Library/CloudStorage/OneDrive-Personal/Documentos/UPY/UPY_3rd_RAAG/Probabilidity_&_Statistics/Project_U1/
   ```

### Opción B: Desde el navegador web

Si prefieres no usar Kaggle, puedes descargar el dataset desde:
- UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/148/diabetes

---

## 🔧 PASO 2: Instalar Dependencias

Abre la terminal en la carpeta del proyecto y ejecuta:

```bash
pip install pandas numpy matplotlib seaborn
```

Si usas conda:
```bash
conda install pandas numpy matplotlib seaborn
```

---

## ▶️ PASO 3: Ejecutar el Análisis

En la terminal, desde la carpeta del proyecto, ejecuta:

```bash
python analisis_diabetes.py
```

### ¿Qué sucede?

1. El script buscará automáticamente `diabetes.csv` en:
   - La carpeta actual
   - Tu carpeta de Descargas
   - La carpeta raíz del usuario
   - La ruta de Kaggle (si estás en Kaggle)

2. Si encuentra el archivo:
   - Mostrará información del dataset en la consola
   - Generará 8 gráficas PNG
   - Creará un archivo con interpretaciones

3. Si no encuentra el archivo:
   - Mostrará un mensaje de error con instrucciones

---

## 📊 ARCHIVOS GENERADOS

El script creará automáticamente estos archivos:

### Gráficas (PNG):
- ✓ `barras_outcome.png` - Distribución de diabetes
- ✓ `histograma_edad.png` - Distribución de edades
- ✓ `histograma_glucose.png` - Distribución de glucosa
- ✓ `histograma_bmi.png` - Distribución del IMC
- ✓ `boxplot_glucose_outcome.png` - Glucosa por estado
- ✓ `boxplot_bmi_outcome.png` - IMC por estado
- ✓ `dispersion_bmi_glucose.png` - Relación glucosa-IMC
- ✓ `mapa_correlacion.png` - Correlaciones

### Documento:
- ✓ `INTERPRETACION_GRAFICAS.txt` - Análisis detallado

---

## 📈 ESTRUCTURA DEL DATASET

El archivo `diabetes.csv` contiene:

| Columna | Descripción |
|---------|------------|
| **Pregnancies** | Número de embarazos |
| **Glucose** | Glucosa en sangre (mg/dL) |
| **BloodPressure** | Presión arterial (mmHg) |
| **SkinThickness** | Espesor de pliegue triceps (mm) |
| **Insulin** | Insulina en sangre (mu U/ml) |
| **BMI** | Índice de masa corporal (kg/m²) |
| **DiabetesPedigreeFunction** | Función de pedigrí de diabetes (0-1) |
| **Age** | Edad en años |
| **Outcome** | Presencia de diabetes (0=No, 1=Sí) |

---

## ⚠️ NOTAS IMPORTANTES

1. **Valores Cero**: Algunos ceros en Glucose, BloodPressure, SkinThickness, Insulin y BMI 
   representan **valores faltantes**, no son fisiológicamente posibles.

2. **Calidad de datos**: Este es un dataset real con algunas limitaciones. Se recomienda 
   filtrar los ceros si se realizan análisis predictivos.

3. **Resolución de gráficas**: Se guardan con 300 DPI, ideales para reportes e impresión.

4. **Comentarios en español**: Todo el código está comentado en español para facilitar 
   el aprendizaje.

---

## 🎓 USO PARA EL PROYECTO ESCOLAR

Este análisis proporciona:

✓ Visualización clara de patrones en diabetes tipo 2
✓ Identificación de factores de riesgo principales
✓ Interpretaciones estadísticas para el reporte
✓ Gráficas de calidad profesional para la presentación

Puedes usar las gráficas directamente en tu proyecto de Probabilidad y Estadística 
sobre Diabetes Mellitus Tipo 2.

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Error: "ModuleNotFoundError: No module named 'pandas'"
**Solución**: Instala las dependencias:
```bash
pip install pandas numpy matplotlib seaborn
```

### Error: "FileNotFoundError" para diabetes.csv
**Solución**: Asegúrate de que el archivo está en la carpeta correcta o usa la ruta completa.

### Las gráficas no se ven en color
**Solución**: Asegúrate de tener matplotlib actualizado:
```bash
pip install --upgrade matplotlib
```

### Las gráficas se abren en una ventana
**Solución**: Es el comportamiento normal. Las gráficas también se guardan como PNG.

---

## 📧 REFERENCIAS

- Dataset original: Kaggle Pima Indians Diabetes Database
- Documentación pandas: https://pandas.pydata.org/docs/
- Documentación matplotlib: https://matplotlib.org/
- Documentación seaborn: https://seaborn.pydata.org/

---

**Última actualización**: 2026-06-09
**Versión**: 1.0
**Estado**: ✓ Listo para usar
