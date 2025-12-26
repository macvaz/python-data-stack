from pyiceberg.catalog import load_catalog

from pyiceberg.schema import Schema
from pyiceberg.types import (
    TimestampType,
    FloatType,
    DoubleType,
    StringType,
    NestedField,
)

from pyiceberg.partitioning import PartitionSpec, PartitionField
from pyiceberg.table.sorting import SortOrder, SortField

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

ns = catalog.list_namespaces()


if ('catalog_example', ) not in ns:
  catalog.create_namespace("catalog_example")

schema = Schema(
    NestedField(field_id=1, name="datetime", field_type=TimestampType(), required=True),
    NestedField(field_id=2, name="symbol", field_type=StringType(), required=True),
    NestedField(field_id=3, name="bid", field_type=FloatType(), required=False),
    NestedField(field_id=4, name="ask", field_type=DoubleType(), required=False),
)

partition_spec = PartitionSpec(
    PartitionField(
        source_id=1, field_id=1000, transform="day", name="datetime_day"
    )
)

# Sort on the symbol
sort_order = SortOrder(SortField(source_id=2, transform='identity'))

catalog.create_table(
    identifier="catalog_example.bids5",
    schema=schema,
    partition_spec=partition_spec,
    sort_order=sort_order,
)