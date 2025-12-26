### Start datalake

```bash
cd infrastructure/datalake/
docker compose up -d
```

### Single node computation engine


```bash
uv run tests/iceberg/ddl.py
uv run tests/iceberg/etl.py
```
