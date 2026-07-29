# Real Estate Data Pipeline with PySpark & Databricks (Serverless)

## 📝 Project Overview
This project addresses a common operational challenge in the real estate sector: ingesting, cleansing, and converting unstructured property catalogs containing inconsistent layout formats and mixed currencies (USD and DOP). 

To solve this, a manual spreadsheet workflow was re-engineered and migrated into a scalable cloud infrastructure using **PySpark** inside **Databricks**, ensuring robust data engineering practices and governance through **Delta Lake** storage.

---

## 🛠️ Architecture & Technical Decisions

*   **Compute Engine (PySpark):** Converted local data manipulation logic into a distributed computing framework via Spark DataFrames, ensuring the pipeline seamlessly handles both sample data and large-scale Big Data volumes.
*   **Data Governance & Quality (Delta Lake):** Transformed datasets are persisted using the Delta format. During the ingestion phase, a strict schema enforcement cleanup was implemented to replace whitespaces in critical columns (`Renta Original` -> `Renta_Original`), ensuring strict compliance with Delta Lake production standards and preventing data corruption.
*   **Orquestation & Cost Control (Serverless Jobs):** The automated data workflow runs as a scheduled task powered by Databricks **Serverless** architecture. This eliminates infrastructure overhead and guarantees optimum cost efficiency, as cloud compute resources are provisioned on-demand solely for the execution runtime and terminated instantly afterward.
*   **Data Lineage & Traceability:** Integrated with Unity Catalog to maintain automated upstream/downstream visual mapping for end-to-end data dependency audits.

---

## 📊 Implemented Business Logic
1.  **Data Ingestion:** Securely connected to internal Databricks catalog tables to fetch raw unstructured real estate records.
2.  **Schema Normalization:** Automated metadata renaming to ensure structural alignment with strict cloud storage protocols.
3.  **Smart Currency Conversion:** Deployed distributed conditional expressions (`F.when`) to automatically apply a live exchange rate (59.50) strictly to property rentals listed under USD, standardizing the entire final dataset to Dominican Pesos (DOP).
4.  **Optimized Load:** Controlled target upserts using programmatic overwrite modes (`.mode("overwrite")`) into target data layers.

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

