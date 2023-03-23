import glob
from typing import Pattern, Any

from datamodel_code_generator.__main__ import main
import os
import sys
from io import StringIO
# from camel_converter import dict_to_snake
import orjson as json

import re

_UNDER_SCORE_1: Pattern[str] = re.compile(r'([^_])([A-Z][a-z]+)')
_UNDER_SCORE_2: Pattern[str] = re.compile('([a-z0-9])([A-Z])')

from functools import lru_cache


def camel_to_snake(string: str) -> str:
    subbed = _UNDER_SCORE_1.sub(r'\1_\2', string)
    return _UNDER_SCORE_2.sub(r'\1_\2', subbed).lower()


@lru_cache()
def convert(s: str) -> str:
    # sanitize characters like ()-
    if s.endswith(')'):
        s = s[:-1]
    s = s.replace('-', '_').replace('(', '_')
    return camel_to_snake(s)


def dict_to_snake(data: dict[Any, Any]) -> dict[Any, Any]:
    converted: dict[Any, Any] = {}
    for k, v in sorted(data.items()):
        if isinstance(k, str):
            key = convert(k)
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


for f in glob.glob('./scrapes/*.json'):
    print(os.path.basename(f))
    with open(f) as fp:
        input = fp.read().strip()

    input = json.dumps(dict_to_snake(json.loads(input)['primaryData'])).decode('utf8')

    output_file = os.path.abspath('./tmp/') + '/' + os.path.splitext(os.path.basename(f))[0] + '.py'
    # oldstdin = sys.stdin
    # sys.stdin = open(os.path.abspath('./json/main.json'))

    sys.stdin = StringIO(input)

    main(
        [
            "--force-optional",
            "--input-file-type",
            "json",
            "--use-standard-collections",
            '--output',
            str(output_file),
        ]
    )