from functools import partial
import re
import inflect

_re_snake1 = partial(re.compile(r'(.)((?<![^A-Za-z])[A-Z][a-z]+)').sub, r'\1_\2')
_re_snake2 = partial(re.compile(r'([a-z0-9])([A-Z])').sub, r'\1_\2')


def snake_case(input: str) -> str:
    return _re_snake2(_re_snake1(input)).casefold()


def table_name(input: str) -> str:
    input = snake_case(input)
    parts = input.rsplit('_', 1)
    last = parts.pop()
    last = inflect.engine().plural(last)
    parts.append(last)
    return '_'.join(parts)
