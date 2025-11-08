from stack import Stack

class InfixToPostfixConverter:
    PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}
    LEFT_ASSOC = {"+", "-", "*", "/"}

    @staticmethod
    def convert(infix: str) -> str:
        """Convert a space-separated infix expression to postfix."""
        out = []
        ops = Stack()

        for tok in infix.split():
            if tok.isalnum():  # variables (A,B,C) or digit-tokens
                out.append(tok)
            elif tok in InfixToPostfixConverter.PRECEDENCE:
                while (not ops.is_empty()
                       and ops.peek() in InfixToPostfixConverter.PRECEDENCE
                       and (InfixToPostfixConverter.PRECEDENCE[ops.peek()] >
                            InfixToPostfixConverter.PRECEDENCE[tok]
                            or (InfixToPostfixConverter.PRECEDENCE[ops.peek()] ==
                                InfixToPostfixConverter.PRECEDENCE[tok]
                                and tok in InfixToPostfixConverter.LEFT_ASSOC))):
                    out.append(ops.pop())
                ops.push(tok)
            elif tok == "(":
                ops.push(tok)
            elif tok == ")":
                while not ops.is_empty() and ops.peek() != "(":
                    out.append(ops.pop())
                if ops.is_empty():
                    raise ValueError("Mismatched parentheses")
                ops.pop()  # discard '('
            else:
                raise ValueError(f"Invalid token: {tok}")

        while not ops.is_empty():
            top = ops.pop()
            if top in ("(", ")"):
                raise ValueError("Mismatched parentheses")
            out.append(top)

        return " ".join(out)
