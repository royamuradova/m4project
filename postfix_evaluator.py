from stack import Stack
import operator

class PostfixEvaluator:
    OPS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,   # division should produce floats when used
    }

    @staticmethod
    def _is_number(token: str) -> bool:
        try:
            float(token)
            return True
        except:
            return False

    @staticmethod
    def evaluate(expr: str):
        """Evaluate a space-separated postfix expression (numbers only)."""
        s = Stack()
        for tok in expr.split():
            if tok in PostfixEvaluator.OPS:
                b = s.pop()  # right operand
                a = s.pop()  # left operand
                s.push(PostfixEvaluator.OPS[tok](a, b))
            elif PostfixEvaluator._is_number(tok):
                s.push(float(tok))      # push as float; display logic handled in main
            else:
                raise ValueError(f"Unsupported token in postfix: {tok}")
        result = s.pop()
        if not s.is_empty():
            raise ValueError("Malformed postfix expression.")
        return result
