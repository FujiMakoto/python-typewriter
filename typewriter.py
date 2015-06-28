import sys
from time import sleep

__author__     = "Makoto Fujimoto"
__copyright__  = 'Copyright 2015, Makoto Fujimoto'
__license__    = "MIT"
__version__    = "1.0"
__maintainer__ = "Makoto Fujimoto"


def typewrite(message, max_time=3, min_time=None, base=0.075, end='\n', **kwargs):
    """
    Print out a string using a typewriter like effect
    :param message: The message to print out
    :type  message: str

    :param max_time: The maximum amount of time printing a message should take
    :type  max_time: int, float or None

    :param min_time: The minimum amount of time printing a message should take
    :type  min_time: int, float or None

    :param base: The base pause time between each character
    :type  base: int or float

    :param end: The character to print after a message has been fully outputted
    :type  end: str

    :param kwargs: Arbitrary keyword arguments, see the online documentation
    """
    # Pause multipliers
    use_multipliers = kwargs.pop('use_multipliers', True)
    comma_multiplier = kwargs.pop('comma_multiplier', 2.0)
    stop_multiplier = kwargs.pop('stop_multiplier', 2.5)

    # Multipliers are applied for commas and full stops to add brief additional pauses
    characters = []
    for character in message:
        # Is this a comma?
        if character == ',':
            pause = (base * comma_multiplier) if use_multipliers else base
            characters.append((character, pause, 'comma'))
            continue

        # How about a full stop?
        if character in ('.', '!', '?'):
            pause = (base * stop_multiplier) if use_multipliers else base
            characters.append((character, pause, 'stop'))
            continue

        # Just a regular character then.
        characters.append((character, base, 'regular'))

    total_time = sum(c[1] for c in characters)

    # If our total time is too long or too short, adjust our base time per character accordingly
    if (max_time is not None) and (total_time > max_time):
        difference = 1 - ((total_time - max_time) / total_time)
        characters = [(c, p * difference, t) for (c, p, t) in characters]
    elif (min_time is not None) and (total_time < min_time):
        difference = 1 + ((min_time - total_time) / total_time)
        characters = [(c, p * difference, t) for (c, p, t) in characters]

    for character, pause, char_type in characters:
        print(character, end='')
        sys.stdout.flush()
        sleep(pause)

    if end:
        print(end)