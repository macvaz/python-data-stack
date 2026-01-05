from formula_engine.grammar.transformers.daft_transformer import DaftTransformer
from formula_engine.grammar.grammar import parser

import daft


def main(indicators: str, datapoints: daft.DataFrame):
    # Parse formulas
    tree = parser.parse(indicators)
    print(tree.pretty())

    # Initialize and transform
    transformer = DaftTransformer()
    transformer.transform(tree)

    # We need data for the referenced datapoints used in formulas
    df = datapoints

    # Register the calculated expressions into the DataFrame
    for name, expr in transformer.expressions.items():
        df = df.with_column(name, expr)

    df.show()

