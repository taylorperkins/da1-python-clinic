"""FUNCTIONS LVL. 1

Definition::

    * A function is a block of code which only runs when it is called.
    * You can pass data, known as parameters, into a function.
    * A function can return data as a result.

You "define" a function using the `def` keyword.

Functions must have a name (preferably snake_case).
The name is followed by parenthesis, then a colon.
All functions return a value, denoted by the `return` keyword. Default is `None`::

    def <function_name>():
        ... do the cool things! ...
        return

"""


def my_first_function():
    print("I do nothing!")


def my_second_function():
    print("I do nothing!")
    return


def my_third_function():
    print("I do nothing!")
    pass


if __name__ == '__main__':
    first_return_value = my_first_function()
    second_return_value = my_second_function()
    third_return_value = my_third_function()

    if first_return_value is None:
        print("First: None returned!")

    if second_return_value is None:
        print("Seccond: None returned!")

    if third_return_value is None:
        print("Third: None returned!")
