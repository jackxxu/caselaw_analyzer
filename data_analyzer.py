import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import re
import lzma, json
import csv

with lzma.open("New Mexico-20200302-xml/data/data.jsonl.xz") as in_file:
    for line in in_file:
        case = json.loads(str(line, 'utf8'))
        cases.append(case)

# with open('data/cases.csv', mode='w') as csvfile: 
#     fieldnames = ['emp_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'emp_name': 'foo'})
#     writer.writerow({'emp_name': 'bar'})