from main import main
import daft

def test_constants(only_constants: str, external_datapoints: daft.DataFrame, ):
    main(only_constants, external_datapoints)

def test_several_functions(some_math_functions: str, external_datapoints: daft.DataFrame, ):
    main(some_math_functions, external_datapoints)
  