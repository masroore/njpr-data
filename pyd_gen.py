import glob
import os
import re
import sys
from io import StringIO
from typing import Pattern

# from camel_converter import dict_to_snake
import orjson as json
from datamodel_code_generator.__main__ import main

from smuggler.pre_processor import canonicalize_json_data, reshape_json_data

_UNDER_SCORE_1: Pattern[str] = re.compile(r"([^_])([A-Z][a-z]+)")
_UNDER_SCORE_2: Pattern[str] = re.compile("([a-z0-9])([A-Z])")

sort_ = True

for f in glob.glob("./json/*.json"):
    print(os.path.basename(f))
    with open(f) as fp:
        input = fp.read().strip()

    loaded = json.loads(input)
    if isinstance(loaded, list):
        data = canonicalize_json_data(loaded[0], sort_)
    else:
        data = canonicalize_json_data(loaded, sort_)
    data = reshape_json_data(data, sort_)
    input = json.dumps(data, False).decode("utf8")

    output_file = (
        os.path.abspath("./tmp/")
        + "/"
        + os.path.splitext(os.path.basename(f))[0]
        + ".py"
    )
    # oldstdin = sys.stdin
    # sys.stdin = open(os.path.abspath('./json/main.json'))

    sys.stdin = StringIO(input)

    main(
        [
            "--force-optional",
            "--input-file-type",
            "json",
            "--use-standard-collections",
            "--snake-case",
            "--output",
            str(output_file),
        ]
    )
