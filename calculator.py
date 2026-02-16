import math
import operator

OPS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv),
    '%': (2, operator.mod),
    '^': (3, operator.pow)
}

def tokenize(expr):
    tokens = []
    num = ""

    for ch in expr:
        if ch.isdigit() or ch == '.':
            num += ch
        else:
            if num:
                tokens.append(float(num))
                num = ""
            if ch in OPS or ch in "()":
                tokens.append(ch)
            elif ch == ' ':
                continue
            else:
                raise ValueError(f"Invalid character: {ch}")

    if num:
        tokens.append(float(num))
    return tokens


def to_postfix(tokens):
    output = []
    stack = []

    for token in tokens:
        if isinstance(token, float):
            output.append(token)

        elif token in OPS:
            while (stack and stack[-1] in OPS and
                   OPS[token][0] <= OPS[stack[-1]][0]):
                output.append(stack.pop())
            stack.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()

    while stack:
        if stack[-1] in "()":
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())

    return output

def eval_postfix(postfix):
    stack = []

    for token in postfix:
        if isinstance(token, float):
            stack.append(token)
        else:
            if len(stack) < 2:
                raise ValueError("Invalid expression")

            b = stack.pop()
            a = stack.pop()

            if token == '/' and b == 0:
                raise ZeroDivisionError("Division by zero")

            result = OPS[token][1](a, b)
            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid expression")

    return stack[0]

def calculate(expr):
    tokens = tokenize(expr)
    postfix = to_postfix(tokens)
    return eval_postfix(postfix)

def main():
    print("===== Python Calculator =====")
    print("Type 'help' for instructions")

    while True:
        user = input("\n>> ").lower().strip()

        if user == "exit":
            print("Goodbye!")
            break

        elif user == "help":
            print("""
Operations:
+  Addition
-  Subtraction
*  Multiplication
/  Division
%  Modulo
^  Power

Supports parentheses: (2+3)*4
Commands: help, clear, exit
            """)

        elif user == "clear":
            print("\033c", end="")

        else:
            try:
                result = calculate(user)
                print("=", result)
            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    main()
