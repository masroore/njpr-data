import glob
import os
from smuggler import pre_processor as proc
import json

for fin in glob.glob("./reshape_in/*.json"):
    with open(fin, "r") as fp:
        json_data = json.loads(fp.read())

    json_data = proc.canonicalize_json_data(json_data, True)
    reshaped_data = proc.reshape_json_data(json_data, True)

    fout = os.path.join(os.path.abspath('./reshape_out/'), os.path.basename(fin))
    with open(fout, 'w') as fp:
        fp.write(json.dumps(reshaped_data, indent=2))
