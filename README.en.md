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
