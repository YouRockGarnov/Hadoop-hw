#!/usr/bin/env python3.6

import sys
import io
import uuid
import random

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
output_stream = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

line_id_count = random.randint(1, 5)
id_line = []
row_count = 0

for line in input_stream:
    try:
        id = line.split('/')[1].strip()
    except ValueError as e:
        continue

    if line_id_count == 0:
        print(','.join(id_line), file=output_stream)
        line_id_count = random.randint(1, 5)
        id_line = []
        row_count += 1

        if row_count == 50:
            sys.exit(0)
    else:
        id_line.append(id)
        line_id_count -= 1

    
