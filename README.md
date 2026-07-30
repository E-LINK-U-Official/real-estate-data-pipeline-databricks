[🇺🇸 Switch to English Version](./README.en.md)

# Pipeline de Datos Inmobiliarios con PySpark y Databricks (Sin Servidor)

## 📝 Descripción del Proyecto
Este proyecto resuelve un problema común en el sector inmobiliario: la ingesta y limpieza de catálogos de propiedades destructurados, con formatos inconsistentes y mezcla de divisas (Dólares USD y Pesos DOP). 

A través de este desarrollo, se migró un flujo de trabajo manual y local hacia una infraestructura moderna en la nube utilizando **PySpark** dentro de **Databricks**, permitiendo el procesamiento escalable de datos y garantizando la gobernanza mediante almacenamiento en **Delta Lake**.

---

## 🛠️ Arquitectura y Decisiones Técnicas

*   **Motor de Cómputo (PySpark):** Se transformó la lógica local de manipulación de datos a un entorno de computación distribuida mediante Spark DataFrames, asegurando que la lógica de negocio funcione eficientemente tanto para archivos pequeños como para volúmenes de Big Data.
*   **Gobernanza y Calidad (Delta Lake):** Los datos procesados se persisten bajo el estándar Delta. Durante la fase de carga, se implementó una limpieza quirúrgica de nombres de columnas (reemplazo de espacios por caracteres permitidos) para cumplir con las estrictas reglas de esquema de Delta Lake y evitar corrupción de datos en producción.
*   **Orquestación Eficiente (Serverless Jobs):** El pipeline está configurado como una tarea automatizada (Job) bajo una arquitectura **Serverless**. Esto garantiza un control de costos óptimo para la organización, ya que la nube aprovisiona recursos de cómputo por los segundos exactos que dura la ejecución y se destruye inmediatamente al finalizar.
*   **Linaje de Datos:** Integrado con Unity Catalog para el rastreo automatizado del flujo del dato (Upstream/Downstream), permitiendo auditorías de seguridad rápidas.

---

## 📊 Lógica de Negocio Aplicada
1.  **Ingesta de Datos:** Conexión y lectura del catálogo inmobiliario crudo desde el catálogo de Databricks.
2.  **Limpieza de Esquema:** Reescritura de metadatos reemplazando espacios críticos (`Renta Original` -> `Renta_Original`) para compatibilidad industrial.
3.  **Conversión de Divisas Inteligente:** Aplicación de condicionales distribuidos nativos (`F.when`) para multiplicar por la tasa de cambio vigente (59.50) únicamente a las propiedades listadas originalmente en USD, unificando todo el catálogo a Pesos Dominicanos (DOP).
4.  **Carga Optimizada:** Sobreescritura controlada (`.mode("overwrite")`) en tablasDelta administradas de Workspace.

