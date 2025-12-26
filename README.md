### Start datalake

```bash
cd infrastructure/datalake/
docker compose up -d
```

### Single node computations

Key technologies used in the project:

* Python 3.12
* **uv** as package and project manager
* **daft** as computation engine

For creating a single-node computation environment, run:

```bash
uv sync
```

For running some examples:

```bash
uv run tests/iceberg/ddl.py
uv run tests/iceberg/etl.py
```

### Cluster-based computations
TBD