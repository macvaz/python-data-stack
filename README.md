## Open-source modern datalake

Python-based dockerized datalake solution including:

| Service | Description | URL |
| :--- | :--- | :--- |
| **Iceberg catalog** | Lakekeeper | [http://localhost:8181](http://localhost:8181) |
| **Identity** | Zitadel | [http://host.docker.internal:8080/](http://host.docker.internal:8080/ui/console/) |
| **S3 Storage** | MinIO | [http://localhost:9001](http://localhost:9001) |
| **Computation (single node)** | Daft + Notebooks | [http://localhost:8888](http://localhost:8888) |
| **Computation (distributed)** | Daft + Ray + Kubernetes | TBD |


To start the datalake, execute the following:

```bash
cd infrastructure/datalake/
docker compose up -d
```

## Manual provision tasks

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

## Single node data pipelines

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

## Cluster-based data pipelines

Based on kuberentes container orchestrator and a ray distributed engine.

TBD

## Similar initiatives

- https://www.dataminded.com/resources/locking-down-your-data-fine-grained-data-access-on-eu-clouds
- https://www.dataminded.com/resources/portable-by-design-rethinking-data-platforms-in-the-age-of-digital-sovereignty