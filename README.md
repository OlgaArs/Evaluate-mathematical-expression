# Evaluate-mathematical-expression

Given a mathematical expression as a string you must return the result as a number.
Numbers

Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.
Operators

You need to support the following mathematical operators:

    Multiplication *
    Division / (as floating point division)
    Addition +
    Subtraction -

Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.
Parentheses

You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6
Whitespace

There may or may not be whitespace between numbers and operators.

An addition to this rule is that the minus sign (-) used for negating numbers and parentheses will never be separated by whitespace. I.e all of the following are valid expressions.

1-1    // 0
1 -1   // 0
1- 1   // 0
1 - 1  // 0
1- -1  // 2
1 - -1 // 2

6 + -(4)   // 2
6 + -( -4) // 10

And the following are invalid expressions

1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid

Solution

the solution was based on the Shunting-yard algorithm https://en.wikipedia.org/wiki/Shunting-yard_algorithm
The algorithm converts expressions in infix notation, which is familiar to us, into  Reverse Polish notationh.
Calculating an expression in  Reverse Polish notation (RPN) is attractive to us because it has a simple algorithm.

The entire algorithm for calculating the expression is divided into three parts:
 - parsing the source string into numbers and operators
 - using the marshalling yard algorithm to get an expression in the RPN
 - evaluating an expression in an RPN


At the output of steps 1 and 2, we get arrays of numbers and operators. It is tempting to implement the function as a generators pipeline. We will reduce memory consumption by using "lazy" data processing, where the expression is evaluated as numbers and operators arrive.
