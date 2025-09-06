# reducer.py
import sys

current_key = None
temp_sum = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")
    value = float(value)
    
    if current_key == key:
        temp_sum += value
        count += 1
    else:
        if current_key:
            avg = temp_sum / count
            print(f"{current_key}\t{avg:.2f}")
        current_key = key
        temp_sum = value
        count = 1

if current_key:
    avg = temp_sum / count
    print(f"{current_key}\t{avg:.2f}")
