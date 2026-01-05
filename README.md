# Open-source modern lakehouse

In 2026, a modern lakehouse acts as a unified interoperability layer where data engineering (DE), data science (DS) and AI teams operate against a single, consistent source of truth. By leveraging open source tools and open standards (like Apache Iceberg), **enterprises can unify siloed dedicated platforms** for DE and AI by **seamlessly sharing integrated metadata, security and container-based computing platform**.

## 1. Platform requirements

The following requirements are needed for a modern lakehouse:

| Requirement | Description |
| :--- | :--- |
| **Iceberg data catalog** | Apache Iceberg provides a high-performance metadata layer that enables **ACID transactions**, time travel, and seamless schema evolution on massive datasets. Its open architecture eliminates vendor lock-in by **allowing multiple engines to interoperate safely**. |
| **Fine-Grained Access Control (FGAC)** | Restricting access at the **row and column level** rather than just the bucket or folder level. |
| **S3-compatible storage with credential vending** | Providing short-lived, scoped credentials (session tokens) to compute engines (Spark, Trino, Flink) on top of S3-compatible storage  without exposing long-term IAM keys. |
| **Auditing** | A comprehensive trail of **who** accessed **what** data, when, and with which query engine. |
| **Coding in Python for DE** | Python is the prevalent language for DS and AI. Additionally, based on its vast library ecosystem, provides a **smooth path to DE for citizen developers**. Consequenly, technical and non-technical users could build complex data pipelines with minimal friction.|
| **High performance** | Modern libraries are used in Python but written in rust, leveraging vectorized execution and **Apache Arrow to provide lightning-fast, zero-copy data** processing that scales from **local machines to massive clusters**. |
| **Unified container platform** | Unified data cluster allowing seamless resource sharing across data science, data engineering and AI training. |
| **Centralized identity** | Single **source of truth for user and service identities**, enabling the uniform enforcement of security policies across all data,  applications and infrastructure, radically simplifing compliance auditing through a unified trail of every access event. |

## 2. Platform technologies

The following technology stack leverages open-source standards and containerized orchestration to deliver a unified, high-performance environment that meets the above requirements:

| Service repo | Requirements | Service URL | Related services
| :--- | :--- | :--- | :--- |
| [Lakekeeper](https://github.com/lakekeeper/lakekeeper) | Iceberg catalog, Auditing | [http://localhost:8181](http://localhost:8181) | OpenFGA, MinIO, Zitadel
| [OpenFGA](https://openfga.dev/) | FGAC | TBD | Lakekeeper
| [MinIO](https://github.com/minio/minio) | S3 storage with credential vending | [http://localhost:9001](http://localhost:9001) | Lakekeeper, Zitadel
| [Zitadel](https://github.com/zitadel/zitadel) | Centralized identity, Auditing | [http://host.docker.internal:8080/](http://host.docker.internal:8080/ui/console/) |
| [Daft](https://github.com/Eventual-Inc/Daft) | Coding in Python for DE | From IDE | Jupyter notebooks
| [Kubernetes](https://github.com/kubernetes/kubernetes) | Unified container platform | TBD | 
| [Ray](https://github.com/ray-project/ray) | Python-based distributed computating framework | TBD | kuberay (ray cluster on top of kubernetes), daft

### 2.1 Similar stacks tested on EU cloud providers

- https://www.dataminded.com/resources/locking-down-your-data-fine-grained-data-access-on-eu-clouds
- https://www.dataminded.com/resources/portable-by-design-rethinking-data-platforms-in-the-age-of-digital-sovereignty
- https://upcloud.com/resources/tutorials/deploying-an-open-source-data-platform-on-upcloud/

## 3. Platform deployment

To start the datalake, execute the following:

```bash
cd infrastructure/datalake/
docker compose up
```

### 3.1 Manual configuration tasks

1. Create bucket in Minio (bde-warehouse)
2. Create warehouse in lakekeeper (bde-warehouse)

```
MINIO CREDENTIALS
ENDPOINT: http://minio:9000/
PATH STYLE ACCESS: ENABLED
STS: ENABLED
FLAVOR: s3-compat
```

3. Open the notebook called [daft.ipynb](http://localhost:8888/lab/tree/Daft.ipynb) and execute

## 4. Data processing in local machines (single-node)

### 4.1 ETL requirements

For demostrate the convenience of combining general-purpose python libraries inside data processing pipelines, the following use case is proposed:

In modern financial engineering, risk specialists are allowed to write their own formulas using a special formula language and formula-driven computation engine. This use case empowers risk analysts to write their own logic without waiting for a software release cycle.

By leveraging a Python/Rust stack, high-performance execution times when processing over millions of datapoints are possible, challenging the need of traditional massive Hadoop clusters that are normally used only by big data specialists. The technology stack should be compatible with running in a conventional local machine like a personal/employee laptop.

Risk specialists require a "Formula Builder" interface where they can input logic like:

* Total_Exposure = Asset_Price * Quantity
* Risk_Weighted_Asset = Total_Exposure * Counterparty_Factor
* Final_Score = Risk_Weighted_Asset / Portfolio_Limit

The "computation engine" will use the topological order defined in the Directed Acycle Graph (DAG) that the formulas implicitly defines. The computation engine will use the DAG to control the execution order (formulas with no dependencies will execute first, followed by those that reference them). 

No additional ordering metadata will be pased to the engine, only a CSV file with the formulas. The CSV file will have the following columns:

* Indicator name
* Indicator formula

The results will be produced in a tabular format with the following structure:
* Indicator value (0)
* Indicator value (n)

Each column represented an indicator value, whill use the name of the "Indicator name" input in the csv file.

### 4.2 ETL architecture

To avoid the memory overhead of the JVM and the latency of Spark, the system uses a Daft-backed execution engine.

* **Frontend**: No front-end will be developed. Formulas will be defined in a file
* **Compiler Layer**: A Python service that parses user strings into an Abstract Syntax Tree (AST). It will use the topological order of the formula's graph to control the execution
* **Computation Core**: The AST is mapped directly to Daft expressions, which are executed in parallel across CPU cores using Rust's memory-safe concurrency.

| Feature | Legacy (Hadoop/Spark) | Modern (Polars/Rust) |
| :--- | :--- | :--- |
| **Startup Time** | Minutes (Cluster provisioning) | Milliseconds (Native binary) |
| **Memory Usage** | High (JVM Overhead) | Low (Direct memory mapping) |
| **Data Format** | Row-based / Distributed | Columnar / SIMD Optimized |
| **Complexity** | High (Requires Data Eng) | Low (Analysts write Pythonic logic) |


### 4.3 ETL technology stack
To comply with the  above requirements and architecture, the following technology stack is used:

| Library                  | Description                                                                                                                                         |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **python**               | Using python 3.12 as unique programming language used by all libraries                                                      |
| **uv**                   | Package and project manager written in Rust.                                                           |
| **daft**                 | General-purpose computation engine written in Rust.                                                    |
| **lark**                 | Grammar parsing tool.                                                                                  |
| **rustworkx**            | High-performance graph library written in Rust.                                                        |


For creating a single-node computation environment, run:

```bash
uv sync
```

For running some examples:

```bash
uv run tests/iceberg/ddl.py
uv run tests/iceberg/etl.py
```

## 5. User experience in clusters (distributed enviroment)

Based on kuberentes container orchestrator and a ray distributed engine.

TBD


