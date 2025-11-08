from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter

def test_postfix():
    print("----- Postfix Evaluator -----")
    tests = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -",
    ]
    for expr in tests:
        val = PostfixEvaluator.evaluate(expr)
        # Display rule to match expected lines:
        # If the expression contains '/', show as float (keep .0 / .5 etc);
        # otherwise, show as int if it's mathematically an integer.
        if "/" in expr:
            out = f"{val}"
        else:
            out = f"{int(val) if float(val).is_integer() else val}"
        print(f"[{expr}] = {out}")

def test_infix_to_postfix():
    print("\n----- Infix to Postfix Converter -----")
    tests = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A * B + C / D",
        "( A + B ) * ( C - D )",
        "A + B * C - D / E",
        "A * ( B + C ) / D",
        "( A + B * C ) / ( D - E )",
        "A +  ( B - C ) * D",
        "( A + B * ( C - D ) ) / E",
    ]
    for expr in tests:
        out = InfixToPostfixConverter.convert(expr)
        print(f"[{expr}] -> [{out}]")

if __name__ == "__main__":
    test_postfix()
    test_infix_to_postfix()
