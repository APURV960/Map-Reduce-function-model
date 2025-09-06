# mapper.py
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(",")
    if len(parts) != 4:
        continue
    
    locality, timestamp, temperature, humidity = parts
    date = timestamp.split()[0]
    try:
        temp = float(temperature)
        print(f"{locality},{date}\t{temp}")
    except:
        continue
