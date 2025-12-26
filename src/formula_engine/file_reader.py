import daft


def read_parquet(file_path: str) -> daft.DataFrame:
    return daft.read_parquet(file_path)
