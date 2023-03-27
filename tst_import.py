import os

import json

from smuggler import mapper, pre_processor
from smuggler.storage import Storage, StorageCompression

import smuggler.models as models
from database import create_db_and_tables


apns = ['0107_599_8.03', '0107_599_8.02', '0107_599_8.01', '0107_599_7', '0107_571_16', '0107_599_9']


def normalize_sections(sections: list[str]) -> list[str]:
    sections = sorted(sections)
    if not 'main' in sections:
        # return [] # ignore if main is not present
        return sections

    sections.insert(0, sections.pop(sections.index('main')))
    return sections


def smuggle_in(apn: str):
    print(apn + "  ###################################\n")
    storage = Storage(os.path.abspath('./storage'), compression=StorageCompression.LZMA)
    sections = storage.list_sections_for_apn(apn)
    sections = normalize_sections(sections)
    # print(sections)
    # return

    for section in sections:
        print(section + ' ^^^^^^^^^^^^^^^^^^^^^')
        json_data = json.loads(storage.load(apn, section))
        sort_ = False
        if isinstance(json_data, list):
            items = []
            for item in json_data:
                items.append(pre_processor.canonicalize_json_data(item, sort_))
            json_data = items
        else:
            json_data = pre_processor.canonicalize_json_data(json_data, sort_)

        reshaped_data = pre_processor.reshape_json_data(json_data, sort_)

        items = mapper.map(reshaped_data, section)
        for i in items:
            print(i.schema()['title'])
            # print(i.json())
            print(i)

        print("\n")


create_db_and_tables()
for apn in apns:
    smuggle_in(apn)
