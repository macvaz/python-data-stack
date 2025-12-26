from daft import DataFrame
from typing import Protocol


class Process(Protocol):
    def execute(self, df: DataFrame) -> DataFrame: ...
