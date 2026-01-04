import daft
from daft.io import IOConfig, S3Config

io_config = IOConfig(
    s3=S3Config(
        key_id="minio",
        access_key="minio-pwd123",
        endpoint_url="http://localhost:9000"
    )
)

daft.set_planning_config(default_io_config=io_config)

df = daft.read_parquet("s3://bde-warehouse/*")

df.show()
