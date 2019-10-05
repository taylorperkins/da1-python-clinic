"""FUNCTIONS LVL. 4

Recursion

You can implement some crazy logic within functions!
What happens when a function references itself?

This is called recursion.
"""
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle
import turtle

t = turtle.Turtle()

t.speed(100)


def poly(sides, length):

    for i in range(sides):
        t.forward(length)
        t.left(180/sides)

    poly(sides, length-2)


def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n-1)


if __name__ == '__main__':
    poly(5, 50)
    # print(factorial_recursive(5))
