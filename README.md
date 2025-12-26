### Docker-based open-source modern datalake

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