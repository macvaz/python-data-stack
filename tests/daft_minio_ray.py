import daft
from daft.io import IOConfig, S3Config


def main():
    io_config = IOConfig(
        s3=S3Config(
            region_name="us-east-1",
            key_id="minioadmin",
            access_key="minioadmin",
            endpoint_url="http://192.168.49.1:9000",
        )
    )

    daft.set_planning_config(default_io_config=io_config)
    daft.set_runner_ray()

    df = daft.read_parquet("s3://bucket/*")

    df.show()

    result_df = daft.sql("""
        SELECT tpep_pickup_datetime, tpep_dropoff_datetime, (tpep_dropoff_datetime - tpep_pickup_datetime) AS trip_duration
        FROM df
        ORDER BY trip_duration DESC
        LIMIT 3
    """).collect()

    result_df.show()

if __name__ == "__main__":
    main()