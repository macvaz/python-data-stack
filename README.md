# Open-source modern lakehouse

In 2026, a modern lakehouse acts as a unified interoperability layer where data engineering (DE), data science (DS) and AI teams operate against a single, consistent source of truth. By leveraging open source tools and open standards (like Apache Iceberg), **enterprises can unify siloed platforms** dedicated separately to DE and AI by **seamlessly sharing integrated metadata, security and container-based computing platform**.

## 1. Requirements

The following requirements are needed for a modern lakehouse:

| Requirement | Description |
| :--- | :--- |
| **Iceberg data catalog** | Apache Iceberg provides a high-performance metadata layer that enables **ACID transactions**, time travel, and seamless schema evolution on massive datasets. Its open architecture eliminates vendor lock-in by **allowing multiple engines to interoperate safely**. |
| **Fine-Grained Access Control (FGAC)** | Restricting access at the **row and column level** rather than just the bucket or folder level. |
| **S3-compatible storage with credential vending** | Providing short-lived, scoped credentials (session tokens) to compute engines (Spark, Trino, Flink) on top of S3-compatible storage  without exposing long-term IAM keys. |
| **Auditing** | A comprehensive trail of **who** accessed **what** data, when, and with which query engine. |
| **Python code for DE** | Python is the prevalent language for DS and AI. Additionally, based on its vast library ecosystem, provides a smooth path to DE for citizen developers. Consequenly, technical and non-technical users could build complex data pipelines with minimal friction.|
| **High performance** | Modern libraries are used in Python but written in rust, leveraging vectorized execution and Apache Arrow to provide lightning-fast, zero-copy data processing that scales from local machines to massive clusters. |
| **Unified container platform** | Unified data cluster allowing seamless resource sharing across data science, data engineering and AI training. |
| **Centralized identity** | Single source of truth for user and service identities, enabling the uniform enforcement of security policies across all data,  applications and infrastructure, radically simplifing compliance auditing through a unified trail of every access event. |

## 2. Technologies

The following technology stack leverages open-source standards and containerized orchestration to deliver a unified, high-performance environment that meets the above requirements:

| Service | Requirements | URL | Related services
| :--- | :--- | :--- | :--- |
| **Lakekeeper** | Iceberg catalog, Auditing | [http://localhost:8181](http://localhost:8181) | OpenFGA, MinIO, Zitadel
| **OpenFGA** | FGA | TBD | Lakekeeper
| **MinIO** | S3 storage with credential vending | [http://localhost:9001](http://localhost:9001) | Lakekeeper, Zitadel
| **Zitadel** | Centralized identity, Auditing | [http://host.docker.internal:8080/](http://host.docker.internal:8080/ui/console/) |
| **Daft** | Python code for DE | [http://localhost:8888](http://localhost:8888) | Jupyter notebooks
| **Kubernetes** | Unified container platform | TBD | 
| **Ray** | Python-based distributed computating framework | TBD | kuberay (ray cluster on top of kubernetes), daft

## 3. Deployment

To start the datalake, execute the following:

```bash
cd infrastructure/datalake/
docker compose up -d
```

### 3.1 Manual tasks

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

## 4. User experience in development machines (single-node)

Key technologies used in the project:

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

## 6. Similar initiatives and useful links

- https://www.dataminded.com/resources/locking-down-your-data-fine-grained-data-access-on-eu-clouds
- https://www.dataminded.com/resources/portable-by-design-rethinking-data-platforms-in-the-age-of-digital-sovereignty