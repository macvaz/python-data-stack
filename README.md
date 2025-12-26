### Start datalake

```bash
cd infrastructure/datalake/
docker compose up -d
```

### Single node computations

The source code is based on Python 3.12 and the project is managed by 'uv'.

for having a single-node environment, run:

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