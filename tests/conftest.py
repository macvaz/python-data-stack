import pytest
import daft

@pytest.fixture
def only_constants():
    return """
    CONST_1: 1.20
    CONST_2: 0.75
    """

@pytest.fixture
def ordered_math_functions():
    return """
    CONST_1: 1.20
    CONST_2: 0.75
    SUM_1: SUM({T(OWN_FUNDS)R(1)C(4)}, {T(LIABILITIES)R(2)C(10)})
    PROD_1: PROD({SUM_1}, {CONST_1})
    DIV_1: DIV({PROD_1}, {CONST_2})
    """

@pytest.fixture
def external_datapoints():
    data = {
        "OWN_FUNDS_R1_C4": [100.0, 200.0],
        "LIABILITIES_R2_C10": [50.0, 80.0]
    }
    return daft.from_pydict(data)