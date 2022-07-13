import csv
import requests
import random
import time
from os.path import isfile
random.seed(42)
with open('pg_catalog.csv') as csvfile:
    r = csv.reader(csvfile)
    r = filter(lambda a : a[4] == 'en' and a[1] == 'Text',r)
    r = list(r)
    random.shuffle(r)
    for row in r:
        if isfile(f'downloaded/b{row[0]}.txt'):
            print(f'Skipping: {row[0]}')
            continue
        try:
            #print(row[0])
            book = requests.get(f'https://www.gutenberg.org/files/{row[0]}/{row[0]}-0.txt', headers={'User-Agent': 'Mozilla'})
            if(book.status_code != 200): continue
            book = book.content.decode('utf-8').splitlines()
            print(row)
           # book = book.text.splitlines()

            with open(f"downloaded/b{row[0]}.txt", mode='w') as f:
                # Remove the headers and tails heuristically, we don't really care
                # about the start/beginning - only counting words!
                f.write('\n'.join(book[100:-500]))

        except:
            print(f"NOT VALID: {row[0]}")
            time.sleep(0.5)


