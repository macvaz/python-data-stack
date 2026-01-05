from lark import Lark

formula_grammar = r"""
    ?start: assignment+

    assignment: identifier ":" expression

    ?expression: function
               | reference
               | NUMBER        
               | identifier

    function:  FUNC_NAME "(" (expression ("," expression)*)? ")"
    
    reference: "{" (attribute | identifier)+ "}"
    attribute: "T(" TEXT ")"  -> table
             | "R(" INT ")"   -> row
             | "C(" INT ")"   -> column

    identifier: CNAME
    FUNC_NAME: "SUM" | "PROD" | "DIV" | "AVG"

    %import common.CNAME
    %import common.NUMBER 
    %import common.INT
    %import common.WS
    %import common.WORD -> TEXT
    %ignore WS
"""

parser = Lark(formula_grammar, parser='lalr')