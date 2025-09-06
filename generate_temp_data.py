import random
from datetime import datetime, timedelta

localities = ["AnnaNagar", "Velachery", "T.Nagar", "Adyar", "Guindy"]
start_date = datetime(2025, 9, 1, 0, 0)
minutes_per_day = 24 * 60
days = 1

with open("temperature_data.txt", "w") as f:
    f.write("locality,timestamp,temperature,humidity\n")
    for day in range(days):
        for minute in range(minutes_per_day):
            timestamp = start_date + timedelta(minutes=minute + day * minutes_per_day)
            for locality in localities:
                temp = round(random.uniform(25, 40), 1)
                humidity = random.randint(40, 80)
                f.write(f"{locality},{timestamp},{temp},{humidity}\n")
