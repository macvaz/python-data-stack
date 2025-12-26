from pyiceberg.catalog import load_catalog
import daft

catalog = load_catalog(
    "catalog",
    **{
        "uri": "http://192.168.1.253:8181",
        "s3.endpoint": "http://192.168.1.253:9000",
        "py-io-impl": "pyiceberg.io.pyarrow.PyArrowFileIO",
        "s3.access-key-id": "minioadmin",
        "s3.secret-access-key": "minioadmin",
        "s3.region": "us-east-1",
    }
)

table = catalog.load_table("catalog_example.bids5")
df = daft.read_iceberg(table)
df.show()
