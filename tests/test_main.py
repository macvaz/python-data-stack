from main import main
import daft

def test_constants(only_constants: str, external_datapoints: daft.DataFrame, ):
    main(only_constants, external_datapoints)

def test_several_functions(ordered_math_functions: str, external_datapoints: daft.DataFrame, ):
    main(ordered_math_functions, external_datapoints)
  