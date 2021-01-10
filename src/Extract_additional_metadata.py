from glob import glob
from pprint import pprint

import csv

metadata = []

for header_file_path in glob("./data/physionet.org/files/tpehgdb/1.0.1/tpehgdb/*m.hea"):
    with open(header_file_path) as f:
        props = filter(lambda l: l.startswith("# "), f.readlines())
        props = map(lambda l: l.replace("#", "").strip().split(" "), props)
        props = {p[0]: p[1] for p in props}

        metadata.append(props)

with open('./results/tpehgdb_additional_metadata.csv', 'w', newline='') as csv_file:
    dict_writer = csv.DictWriter(csv_file, metadata[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(metadata)
