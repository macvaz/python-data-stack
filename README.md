### Docker-based open-source modern datalake

The following technologies are used:

| Service                  | Role                                                                                                                                         |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **MinIO**                | Object storage for Iceberg table data and metadata (Parquet/ORC files). Acts as an S3-compatible backend.                                    |
| **Iceberg REST Catalog** | Exposes Iceberg tables via REST API. Resolves metadata, active snapshots, and Parquet file paths. Integrates Ranger plugin for ACLs/masking. |
| **Ranger Admin**         | Web-based management UI for creating and managing security policies (table/column-level access, masking).                                    |
| **Ranger DB**    | Stores Ranger policies, users, and service definitions.   


To start the datalake, execute the following:

```bash
cd infrastructure/datalake/
docker compose up -d
```

### Single node data pipelines

Key technologies used in the project:

* **python 3.12** as single programming language
* **uv** as package and project manager
* **daft** as general-purpose computation engine
* **lark** as grammar parsing tool
* **rustworkx** as graph library

For creating a single-node computation environment, run:

```bash
uv sync
```

For running some examples:

```bash
uv run tests/iceberg/ddl.py
uv run tests/iceberg/etl.py
```

### Cluster-based data pipelines

Based on kuberentes cluster and a ray cluster.

TBD