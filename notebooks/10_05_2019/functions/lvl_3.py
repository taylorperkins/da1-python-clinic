"""FUNCTIONS LVL. 3

Practice round!!

Make the code run.
Don't touch ANYTHING below the line that looks like::

    "if __name__ == '__main__':"

"""


def greet_someone():
    # FIXME!!
    pass


def greet_all():
    # FIXME!!
    pass


if __name__ == '__main__':
    ########################################
    # CHALLENGE 1 --> Greeting one name..
    ########################################

    first_names = ['Selam', 'Mary', 'Taylor']

    for name in first_names:
        greeting = greet_someone(name)
        print(greeting)

        assert isinstance(greeting, str), '`greet_someone` must return a string!!'
        assert name in greeting, f'Oops! Looks like `greet_someone` didn\'t greet the appropriate person --> {name}'

    print('You have passed challenge 1.. Well done.')

    ########################################
    # CHALLENGE 2 --> Greeting full name
    ########################################

    last_names = ['Tekie', 'van Valkenburg', 'Perkins']

    greetings = greet_all(first_names, last_names)
    print(greetings)

    # There are 3 names.. Make sure this function returns a list of greetings!
    assert isinstance(greetings, list), f'`greet_all` must return a list of greetings! got {type(greetings)} instead'
    assert len(greetings) == len(last_names), f'`greet_all` must greet everyone only once.. ' \
        f'got {len(greetings)} greetings instead!'

    for ind, greeting in enumerate(greetings):
        first_name, last_name = first_names[ind], last_names[ind]

        assert f'{first_name} {last_name}' in greeting, f'Oops! Looks like this greeting ({greeting}) doesn\'t ' \
                                                        f'include their full name! --> "{first_name, last_name}"'

    print('You have passed challenge 2.. You are becoming one with the function.')

    ########################################
    # CHALLENGE 3 --> Greeting full name "n" times!
    ########################################
    greeting_count = [1, 2, 3]

    greetings = greet_all(first_names, last_names, greeting_count=greeting_count)
    print(greetings)

    assert len(greetings) == sum(greeting_count), f'I need {sum(greeting_count)} total greetings!'

    for ind, count in enumerate(greeting_count):
        full_name = f'{first_names[ind]} {last_names[ind]}'

        for i in range(ind):
            greeting = greetings.pop(0)

            assert full_name in greeting, f'Oops! Looks like this greeting ({greeting}) doesn\'t ' \
                f'include their full name! --> "{full_name}" | count {count} | index {i+1} of {count}'
