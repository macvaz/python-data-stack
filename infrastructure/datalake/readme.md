Python-based dockerized datalake solution including:

| Service | Description | URL |
| :--- | :--- | :--- |
| **Iceberg catalog** | Lakekeeper | [http://localhost:8181](http://localhost:8181) |
| **Identity** | Zitadel | [http://host.docker.internal:8080/](http://host.docker.internal:8080/ui/console/) |
| **S3 Storage** | MinIO | [http://localhost:9001](http://localhost:9001) |
            |

## Running platform

docker compose up



Login to Zitadel:

Visit http://host.docker.internal:8080/ui/console?login_hint=zitadel-admin@zitadel.host.docker.internal and enter Password1! to log in.

Create OIDC applications

## Similar initiatives

- https://www.dataminded.com/resources/locking-down-your-data-fine-grained-data-access-on-eu-clouds
- https://www.dataminded.com/resources/portable-by-design-rethinking-data-platforms-in-the-age-of-digital-sovereignty


