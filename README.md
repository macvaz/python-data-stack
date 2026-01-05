# Open-source modern lakehouse

## 1. Platform 

In 2026, a modern lakehouse acts as a unified interoperability layer where data engineering (DE), data science (DS) and AI teams operate against a single, consistent source of truth. By leveraging open source tools and open standards (like Apache Iceberg), **enterprises can unify siloed dedicated platforms** for DE and AI by **seamlessly sharing integrated metadata, security and container-based computing platform**.

### 1.1 Requirements

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

### 1.2 Technologies

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

#### 1.2.1 Similar platform stacks tested on EU cloud providers

- https://www.dataminded.com/resources/locking-down-your-data-fine-grained-data-access-on-eu-clouds
- https://www.dataminded.com/resources/portable-by-design-rethinking-data-platforms-in-the-age-of-digital-sovereignty
- https://upcloud.com/resources/tutorials/deploying-an-open-source-data-platform-on-upcloud/

### 1.3 Deployment

To start the datalake, execute the following:

```bash
cd infrastructure/datalake/
docker compose up
```

#### 1.3.1 Manual configuration tasks

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

## 2. Software (Data processes / ETLs)

### 2.1 Requirements

For demostrate the convenience of combining general-purpose python libraries inside data processing pipelines, the following use case is proposed:

In modern financial engineering, risk specialists are allowed to write their own formulas using a special formula language and formula-driven computation engine. This use case empowers risk analysts to write their own logic without waiting for a software release cycle.

By leveraging a Python/Rust stack, high-performance execution times when processing over millions of datapoints are possible, challenging the need of traditional massive Hadoop clusters that are normally used only by big data specialists. The technology stack should be compatible with running in a conventional local machine like a personal/employee laptop.

Risk specialists require a formula language to define risk indicator formulas like these: 

```
CONST_1: 1.20
CONST_2: 0.75
SUM_1: SUM({T(OWN_FUNDS)R(1)C(4)}, {T(LIABILITIES)R(2)C(10)})
PROD_1: PROD({SUM_1}, {CONST_1})
DIV_1: DIV({PROD_1}, {CONST_2})
```

As seen in the example, one indicator can reference other indicators, creating a Directed Acycle Graph (DAG). The computation engine will use the topological order of the DAG to control the execution order of the indicators (formulas with no dependencies will execute first, followed by those that reference them). No additional ordering metadata will be pased to the engine.

The only input to the engine is a flat file with 1 indicator definition by line, the expected systax of each line is the following: 

```
<INDICATOR_NAME> : <FORMULA>
```

The results will be produced in a tabular format (1 column per indicator). An example of the expected output for the above example is the following:

| CONST_1 | CONST_2 | SUM_1 | PROD_1 | DIV_1 |
| :--- | :--- | :--- | :--- | :--- |
| float_value | float_value | float_value  | float_value  | float_value  |


### 2.2 Software architecture

To avoid the memory overhead of the JVM and the latency of Spark, the system uses a Daft-backed execution engine.

* **Frontend**: No front-end will be developed. Formulas will be defined in a file
* **Compiler Layer**: A Python service that parses input file into an Abstract Syntax Tree (AST). It will use the topological order of the formula's graph to control the execution
* **Computation Core**: The AST is mapped directly to Daft expressions, which are executed in parallel across CPU cores using Rust's memory-safe concurrency.

| Feature | Legacy (Hadoop/Spark) | Modern (Polars/Rust) |
| :--- | :--- | :--- |
| **Startup Time** | Minutes (Cluster provisioning) | Milliseconds (Native binary) |
| **Memory Usage** | High (JVM Overhead) | Low (Direct memory mapping) |
| **Data Format** | Row-based / Distributed | Columnar / SIMD Optimized |
| **Complexity** | High (Requires Data Eng) | Low (Analysts write Pythonic logic) |


### 2.3 Technology stack
To comply with the  above requirements and architecture, the following technology stack is used:

| Library                  | Description                                                                                                                                         |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **python**               | Using python 3.12 as unique programming language used by all libraries                                                      |
| **uv**                   | Package and project manager written in Rust.                                                           |
| **daft**                 | General-purpose computation engine written in Rust.                                                    |
| **lark**                 | Grammar parsing tool.                                                                                  |
| **rustworkx**            | High-performance graph library written in Rust.                                                        |


### 2.4 Development experience in local machines (single-node mode)

For creating a single-node computation environment, run:

```bash
uv sync
```

For running some examples:

```bash
uv run src/main.py
```

### 2.5 Developoment experience in clusters (distributed mode)

Based on kuberentes container orchestrator and a ray distributed engine.

TBC

```bash
minikube start
kubectl -n kuberay port-forward service/raycluster-kuberay-head-svc 8265:8265 > /dev/null &
```

activate virtual env:
ray job submit --address http://localhost:8265 --working-dir /home/mac/job/bigdata/formula_engine/tests --runtime-env-json '{"pip": ["daft"]}' -- python daft_minio_ray.py 

Ray dashboard
127.0.0.1:8265


