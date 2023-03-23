import re
from typing import Pattern, Any
from functools import lru_cache

_UNDER_SCORE_1: Pattern[str] = re.compile(r'([^_])([A-Z][a-z]+)')
_UNDER_SCORE_2: Pattern[str] = re.compile('([a-z0-9])([A-Z])')
_disallowed_chars = ['-', '(', ')']


def _to_snake(txt: str) -> str:
    subbed = _UNDER_SCORE_1.sub(r'\1_\2', txt)
    return _UNDER_SCORE_2.sub(r'\1_\2', subbed).lower()


@lru_cache()
def convert_text(txt: str) -> str:
    # sanitize characters like ()-
    for c in _disallowed_chars:
        txt = txt.replace(c, '_')
    txt = txt.rstrip('_')
    return _to_snake(txt)


def dict_to_snake(data: dict[Any, Any]) -> dict[Any, Any]:
    converted: dict[Any, Any] = {}
    for k, v in sorted(data.items()):
        if isinstance(k, str):
            key = convert_text(k)
        else:
            key = k

        if isinstance(v, dict):
            converted[key] = dict_to_snake(v)
        elif isinstance(v, list):
            converted[key] = [dict_to_snake(x) if isinstance(x, dict) else x for x in v]
        elif isinstance(v, tuple):
            converted[key] = tuple(dict_to_snake(x) if isinstance(x, dict) else x for x in v)
        else:
            converted[key] = data[k]

    return converted
