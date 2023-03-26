import glob
import os
from smuggler import pre_processor as proc
import orjson as json

sort_ = True

for fin in glob.glob("./reshape_in/*.json"):
    with open(fin, "r") as fp:
        json_data = json.loads(fp.read())

    if isinstance(json_data, list):
        items = []
        for item in json_data:
            items.append(proc.canonicalize_json_data(item, sort_))
        json_data = items
    else:
        json_data = proc.canonicalize_json_data(json_data, sort_)

    reshaped_data = proc.reshape_json_data(json_data, sort_)

    fout = os.path.join(os.path.abspath("./reshape_out/"), os.path.basename(fin))
    with open(fout, "w") as fp:
        fp.write(json.dumps(reshaped_data, option=json.OPT_INDENT_2).decode("UTF8"))
