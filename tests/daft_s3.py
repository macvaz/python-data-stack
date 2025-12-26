import daft
from daft.io import IOConfig, S3Config

io_config = IOConfig(
    s3=S3Config(
        key_id="minioadmin",
        endpoint_url="http://localhost:9000",
        access_key="minioadmin",
    )
)

daft.set_planning_config(default_io_config=io_config)

df = daft.read_parquet("s3://bucket/*")

df.show()
