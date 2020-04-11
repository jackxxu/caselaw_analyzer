import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import lzma, json
import csv
from bs4 import BeautifulSoup

with open('data/cases.csv', mode='w') as csvfile: 
    fieldnames = ['id', 'url', 'name', 'name_abbreviation', 'decision_date', 'docket_number', 
                  'first_page', 'last_page', 'frontend_url',
                  'citations', 'citation_0_type', 'citation_0', 'citation_1_type', 'citation_1', 'citation_2_type', 'citation_2',
                  'volume_barcode', 'volume_number',
                  'reporter_name', "reporter_id",
                  'court_id', 'court_name',
                  'jurisdiction_id', 'jurisdiction_name',
                  'body']

    output = csv.DictWriter(csvfile, fieldnames=fieldnames)
    output.writeheader()

    for state in ['North Carolina', 'Arkansas', 'Illinois', 'New Mexico']:
        with lzma.open(f'{state}-20200302-xml/data/data.jsonl.xz', mode='r') as in_file:
            for line in in_file:
                case = json.loads(str(line, 'utf8'))

                for i, citation in enumerate(case['citations']): 
                    if i > 3: 
                        print(f"more than {len(case['citations'])} citations")
                        break
                    case[f'citation_{i}_type'] = citation['type']
                    case[f'citation_{i}'] = citation['cite']
                case['citations'] = len(case['citations'])
                del case['citations']

                case['volume_barcode'] = case['volume']['barcode']
                case['volume_number'] = case['volume']['volume_number']
                del case['volume']

                case['reporter_name'] = case['reporter']['full_name']
                case['reporter_id'] = case['reporter']['id']
                del case['reporter']

                case['court_id'] = case['court']['id']
                case['court_name'] = case['court']['name']
                del case['court']

                case['jurisdiction_id'] = case['jurisdiction']['id']
                case['jurisdiction_name'] = case['jurisdiction']['name_long']
                del case['jurisdiction']

                del case['preview']

                # soup = BeautifulSoup(case['casebody']['data'], 'html.parser')
                # case['body'] = soup.text
                case['body'] = case['casebody']['data']
                del case['casebody']

                output.writerow(case)

