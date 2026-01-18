import operator
from typing import List

import daft
from lark import Transformer, v_args

from formula_engine.common.types import Assignment, IndicatorInfo


@v_args(inline=True)
class DaftTransformer(Transformer):
    def start(self, *assignments) -> List[Assignment]:
        return list(assignments)

    def assignment(self, name, indicator_info: IndicatorInfo) -> Assignment:
        return (str(name), indicator_info)

    def function(self, name, *infos: IndicatorInfo) -> IndicatorInfo:
        name = str(name)
        if name == "SUM":
            return _handle_binary_operator(operator.add, *infos)
        elif name == "PROD":
            return _handle_binary_operator(operator.mul, *infos)
        elif name == "DIV":
            return _handle_binary_operator(operator.truediv, *infos)
        return infos[0]

    def reference(self, *items) -> IndicatorInfo:
        ref = {}
        for i in items:
            if isinstance(i, dict):
                # It's a {T(A)R(1)C(1)} style reference
                ref.update(i)
            else:
                # It's a simple {SUM_1} style reference
                col_name = str(i)
                return IndicatorInfo(daft.col(col_name), [col_name])

        # It's a {T(A)R(1)C(1)} style reference
        col_name = f"{ref['table']}_R{ref['row']}_C{ref['column']}"
        return IndicatorInfo(daft.col(col_name), [col_name])

    def table(self, t) -> dict:
        return {"table": str(t).strip('"')}

    def row(self, r) -> dict:
        return {"row": int(r)}

    def column(self, c) -> dict:
        return {"column": int(c)}

    def identifier(self, id) -> str:
        return str(id)

    def NUMBER(self, n) -> IndicatorInfo:
        return IndicatorInfo(daft.lit(float(n)), [])


def _handle_binary_operator(op_function: operator, *infos: IndicatorInfo):
    result_expr = infos[0].expr
    result_ref = infos[0].references
    for next_info in infos[1:]:
        result_expr = op_function(result_expr, next_info.expr)
        result_ref.extend(next_info.references)
    return IndicatorInfo(result_expr, result_ref)
