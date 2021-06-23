# import ast


class BreakpointChecker:
    name = "flake8-breakpoint"
    version = "0.0.1"

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    def run(self):
        # line number, column offset, message, class
        yield (1, 0, 'B601 builtin function "breakpoint" found', type(self))

        # for node in ast.walk(self.tree):
        #     if isinstance(node, ast.Call) and ...:
        #         yield
