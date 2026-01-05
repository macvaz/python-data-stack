import daft
from lark import Transformer

class DaftTransformer(Transformer):
    def __init__(self):
        # This will store the final executable expressions
        self.expressions = {}

    # --- Terminals ---
    
    def NUMBER(self, n):
        # Convert raw string number to a Daft literal
        return daft.lit(float(n))

    def INT(self, i):
        return int(i)

    def TEXT(self, t):
        return str(t)

    def FUNC_NAME(self, f):
        return str(f)

    # --- Rules ---

    def identifier(self, i):
        return str(i[0])

    def table(self, items):
        return f"T_{items[0]}"

    def row(self, items):
        return f"R_{items[0]}"

    def column(self, items):
        return f"C_{items[0]}"

    def reference(self, items):
        """
        Handles {T(OWN_FUNDS)R(1)C(4)} or {SUM1}
        """
        # Case 1: Simple reference like {SUM1} -> daft.col("SUM1")
        if len(items) == 1 and isinstance(items[0], str):
            return daft.col(items[0])
        
        # Case 2: Complex reference -> Join attributes into a column name
        # e.g., T_OWN_FUNDS_R_1_C_4
        ref_name = "_".join(str(i) for i in items)
        return daft.col(ref_name)

    def function(self, items):
        func_name = items[0]
        args = items[1:]
        
        if func_name == "SUM":
            # Start with the first arg, add the rest
            res = args[0]
            for arg in args[1:]:
                res = res + arg
            return res
            
        elif func_name == "PROD":
            res = args[0]
            for arg in args[1:]:
                res = res * arg
            return res
            
        elif func_name == "DIV":
            # Standard division: arg[0] / arg[1]
            return args[0] / args[1]
            
        return None

    def assignment(self, items):
        var_name = items[0]
        expression = items[1]
        
        # Store the expression for later use in the DataFrame
        self.expressions[var_name] = expression
        return (var_name, expression)