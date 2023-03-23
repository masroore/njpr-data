import glob
from typing import Pattern, Any

from datamodel_code_generator.__main__ import main
import os
import sys
from io import StringIO

# from camel_converter import dict_to_snake
import orjson as json
from smuggler.pre_processor import canonicalize_json_data
import re

_UNDER_SCORE_1: Pattern[str] = re.compile(r"([^_])([A-Z][a-z]+)")
_UNDER_SCORE_2: Pattern[str] = re.compile("([a-z0-9])([A-Z])")

for f in glob.glob("./scrapes/*.json"):
    print(os.path.basename(f))
    with open(f) as fp:
        input = fp.read().strip()

    input = json.dumps(canonicalize_json_data(json.loads(input)["primaryData"]), False).decode(
        "utf8"
    )

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
            "--output",
            str(output_file),
        ]
    )
