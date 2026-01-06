from formula_engine.grammar.transformers.daft_transformer import DaftTransformer
from formula_engine.grammar.grammar import parser

import daft


def main(indicators: str, datapoints_df: daft.DataFrame):
    tree = parser.parse(indicators)
    print(tree.pretty())

    transformer = DaftTransformer()
    assignments = transformer.transform(tree)

    import pprint
    pprint.pprint(assignments)

    datapoints_df.show()

    # Add the formulas columns to the input dataframe with the datapoints
    for col_name, expr in assignments:
        datapoints_df = datapoints_df.with_column(col_name, expr)

    datapoints_df.show()
