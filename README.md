### Start datalake

```bash
cd infrastructure/datalake/
docker compose up -d
```

### Single node computation engine




### Cluster-based computation engine

```bash
minikube start
kubectl -n kuberay port-forward service/raycluster-kuberay-head-svc 8265:8265 > /dev/null &
```

activate virtual env:
ray job submit --address http://localhost:8265 --working-dir /home/mac/job/bigdata/formula_engine/tests --runtime-env-json '{"pip": ["daft"]}' -- python daft_minio_ray.py 

Ray dashboard
127.0.0.1:8265

