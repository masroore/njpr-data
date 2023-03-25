import os
from glob import glob

import snakecase

options = [
    "--force-optional",
    "--input-file-type json",
    "--use-standard-collections",
    "--snake-case",
]

for f in glob(os.path.abspath("./json/") + "/*.json"):
    outfile = os.path.abspath(
        "./generated/"
        + snakecase.convert(os.path.splitext(os.path.basename(f))[0])
        + ".py"
    )
    print(f'datamodel-codegen.exe {" ".join(options)} --input {f} --output {outfile}')

'''
outfile = os.path.abspath("./generated/schema.py")
print(
    f"datamodel-codegen.exe {' '.join(options)} --input {os.path.abspath('./json/main.json')} --output {outfile}"
)
'''