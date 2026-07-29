# 💻 Código Fuente (PySpark)

```python
from pyspark.sql import functions as F

# 1. Leer la tabla original
df = spark.table("workspace.default.tabla_final_inmobiliaria")

# 2. LIMPIEZA DE COLUMNA: Reemplazar el espacio por un guión bajo para cumplir con Delta
df_limpio = df.withColumnRenamed("Renta Original", "Renta_Original")

USD_TO_DOP_RATE = 59.50

# 3. Aplicar la lógica usando el nuevo nombre de la columna (Renta_Original)
df_procesado = df_limpio.withColumn(
    "Renta_Calculada_DOP",
    F.when(F.col("Moneda") == "USD", F.col("Renta_Original") * USD_TO_DOP_RATE)
     .otherwise(F.col("Renta_Original"))
)

# 4. Persistir los datos transformados en una tabla Delta optimizada
display(df_procesado)
# Guardar la tabla sin errores de caracteres invalidos
df_procesado.write.mode("overwrite").format("delta").saveAsTable("workspace.default.rentas_limpias_realestate")
