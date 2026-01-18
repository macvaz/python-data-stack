from typing import List

import daft

from formula_engine.grammar.grammar import parser
from formula_engine.grammar.transformers.daft_transformer import DaftTransformer
from formula_engine.common.types import Assignment
from formula_engine.graph.dag import create_dag, iterate_by_generation


def compute(indicators: str, datapoints_df: daft.DataFrame):
    tree = parser.parse(indicators)
    print(tree.pretty())

    transformer = DaftTransformer()
    assignments: List[Assignment] = transformer.transform(tree)

    import pprint

    pprint.pprint(assignments)

    datapoints_df.show()

    # Create indicator's dag
    dag = create_dag(assignments)

    print("Nodes: ", dag.nodes())
    print("Edges: ", dag.edges())

    iterate_by_generation(dag)

    # Add the formulas columns to the input dataframe with the datapoints
    for indicator_name, indicator_info in assignments:
        datapoints_df = datapoints_df.with_column(indicator_name, indicator_info.expr)

    datapoints_df.show()
