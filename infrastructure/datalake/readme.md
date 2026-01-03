Docker-based moder datalake solution including:

| Service                  | Role                                                                                                                                         |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **MinIO**                | Object storage for Iceberg table data and metadata (Parquet/ORC files). Acts as an S3-compatible backend.                                    |

Manual steps
1. enable migrate in lakekeeper
2. docker run --rm -v "$(pwd)/authelia/config:/keys" authelia/authelia:latest \
    authelia crypto pair rsa generate --directory /keys


3. docker run --rm authelia/authelia:latest     authelia crypto hash generate argon2 --password 'lakekeeper-ka93k339fkk&&222'

4. docker run --rm authelia/authelia:latest authelia crypto hash generate argon2 --password 'admin-pwd123'
5. docker run --rm authelia/authelia:latest authelia crypto hash generate argon2 --password 'ds_user1-pwd123'