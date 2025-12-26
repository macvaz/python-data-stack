Docker-based moder datalake solution including:

| Service                  | Role                                                                                                                                         |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **MinIO**                | Object storage for Iceberg table data and metadata (Parquet/ORC files). Acts as an S3-compatible backend.                                    |
| **Iceberg REST Catalog** | Exposes Iceberg tables via REST API. Resolves metadata, active snapshots, and Parquet file paths. Integrates Ranger plugin for ACLs/masking. |
| **Ranger Admin**         | Web-based management UI for creating and managing security policies (table/column-level access, masking).                                    |
| **Ranger DB (MySQL)**    | Stores Ranger policies, users, and service definitions.                                                                                      |
