from formula_engine.engine import compute

import daft

def main(formulas: str, datapoints_df: daft.DataFrame):
    '''
    Example input parameters for calling main function

    data = {
        "A": [1, 2, 3, 4, 5],
        "B": [10, 20, 30, 40, 50],
    }
    datapoints_df = daft.from_pydict(data)

    # Sample indicators string
    formulas = """
    C: SUM({A}, {B})
    D: PROD({C}, 2.0)
    E: DIV({D}, {A})
    """
    
    :param formulas: Formulas of the indicators to be computed
    :type formulas: str
    :param datapoints_df: Data of the external datapoints to be used in the computations
    :type datapoints_df: daft.DataFrame
    '''
    compute(formulas, datapoints_df)

if __name__ == "__main__":
    # Change this code to test with different data and formulas

    external_data = {
        "A": [1, 2, 3, 4, 5],
        "B": [10, 20, 30, 40, 50],
    }
    datapoints_df = daft.from_pydict(external_data)

    formulas = """
    C: SUM({A}, {B})
    D: PROD({C}, 2.0)
    E: DIV({D}, {A})
    """

    main(formulas, datapoints_df)