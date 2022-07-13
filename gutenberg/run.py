import csv
import requests
import random
import time

import sys

csv.field_size_limit(sys.maxsize)


def create_data_pair(a, b, delimeter=','):
    original = open(a)
    t9 = open(b)

    original = csv.reader(original, delimiter=delimeter)
    t9 = csv.reader(t9, delimiter=delimeter)

    original = list(original)
    t9 = list(t9)

    zipped = []

    t9_dict = {}

    for (o,t) in zip(original, t9):
        entry = [o[0],t[0],o[1]]
        if t[0] in t9_dict:
            t9_dict[t[0]].append(entry)
        else:
            t9_dict[t[0]] = [entry]

        zipped.append(entry)

    return t9_dict, zipped

t9_dict, _ = create_data_pair('result.txt', 'result_t9.txt')
_, reference = create_data_pair('original_files/t9backup_en.txt', 'original_files/t9backup_en_t9.txt', ' ')


#for key in t9_dict:
#    t9_dict[key].sort(key=lambda f: f[2])

def priority(l, word):
    p = len(l)
    for w in l:
        if word == w[0]:
            return p
        else:
            p = p - 1
    return 0

for word in reference:
    if word[1] in t9_dict:
        word[2] = priority(t9_dict[word[1]], word[0]) * 1


output = open('t9backup_en_ranked.txt', 'w')
for word in reference:
    print(f'{word[0]} {word[2]} 1', file=output)

#reference = open('t9backup_en.txt')
#longest = max(len(item) for item in t9_dict.values())
#print(longest)
