import daft
from lark import Transformer, v_args

@v_args(inline=True)
class DaftTransformer(Transformer):
    def start(self, *assignments):
        return list(assignments)

    def assignment(self, name, expr):
        return (str(name), expr)

    def function(self, name, *args):
        name = str(name)
        if name == "SUM":
            res = args[0]
            for next_arg in args[1:]: res = res + next_arg
            return res
        elif name == "PROD":
            res = args[0]
            for next_arg in args[1:]: res = res * next_arg
            return res
        elif name == "DIV":
            return args[0] / args[1]
        return args[0]

    def reference(self, *items):
        # Determine if it's a coordinate-based reference or a variable-name reference
        ref = {}
        for i in items:
            if isinstance(i, dict): 
                ref.update(i)
            else: 
                return daft.col(str(i)) # It's a simple {SUM_1} style reference
        
        # It's a {T(A)R(1)C(1)} style reference
        col_name = f"{ref['table']}_R{ref['row']}_C{ref['column']}"
        return daft.col(col_name)

    def table(self, t): return {"table": str(t).strip('"')}
    def row(self, r): return {"row": int(r)}
    def column(self, c): return {"column": int(c)}
    def identifier(self, i): return str(i)
    def NUMBER(self, n): return daft.lit(float(n))