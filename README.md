# Infix to Prefix Converter and Evaluator

This project contains functions to **convert infix expressions to prefix notation** and **evaluate prefix expressions**.

## Functions

### isOperator( c )
- **Purpose**: This helper function checks if the given character `c` is an operator (such as `+`, `-`, `*`, `/`, or `^`).
- **Parameters**: A single character `c`.
- **Returns**: `True` if the character is an operator; `False` otherwise.

### getPriority( c )
- **Purpose**: This function defines the precedence of operators. Operators with higher precedence are given a higher numeric value.
- **Parameters**: A single character `c` (an operator).
- **Returns**: An integer representing the precedence of the operator (`1` for `+` and `-`, `2` for `*` and `/`, `3` for `^`).

### infixToPrefix(expression)
- **Purpose**: Converts an infix expression to a prefix expression.
- **Parameters**: A string `expression` in infix notation (e.g., `a + b * c`).
- **Returns**: A string representing the equivalent prefix expression.
- **How it works**: 
  - The expression is first formatted by adding spaces around operators.
  - It is then split by spaces to handle multiple digit input.
  - It is then filtered from spaces using list comprehension.
  - The result is a space-separated string representing the expression in prefix notation.

### evaluation(prefix)
- **Purpose**: Evaluates a prefix expression and returns the result.
- **Parameters**: A string `prefix` representing a prefix expression (e.g., `+ 3 * 2 5`).
- **Returns**: The result of the evaluated prefix expression as an integer.
- **How it works**: 
  - The prefix expression is split into tokens (individual operands and operators) using split(' ').
  - The function processes the tokens in reverse order ([::-1]).
  - If the token is not an operator (using the helper function isOperator( c )), it is treated as an operand (number). This number is then converted to an integer and pushed onto the stack s.
  -  When an operator is encountered, the two most recent operands are popped from the stack (o1 and o2).
  - The operator is then applied to these operands, and the result is pushed back onto the stack.

## Examples

#### Converting Infix to Prefix:

For the infix expression `5+12-3+(3*4)`, the conversion to prefix will yield:
    + - + 5 12 3 * 3 4
#### Evaluating Prefix Expression:

For the prefix expression `+ - + 5 12 3 * 3 4`, the evaluation will return:
    26
    
