from dataclasses import dataclass
from typing import List

import daft


@dataclass
class IndicatorInfo:
    expr: daft.Expression
    references: List[str]


type Assignment = tuple[str, IndicatorInfo]
