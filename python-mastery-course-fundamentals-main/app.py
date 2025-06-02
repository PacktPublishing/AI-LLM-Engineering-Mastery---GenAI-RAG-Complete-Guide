from datetime import datetime
from pathlib import Path
import csv
import matplotlib.pyplot as plt

# plt.style.use("seaborn")


path = Path("weather.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

highs, dates = [], []
for row in reader:
    high = int(row[9])
    current_date = datetime.strptime(row[1], "%Y-%m-%d")
    highs.append(high)
    dates.append(current_date)

fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")

ax.set_title("Temps")
ax.set_xlabel("", fontsize=15)
fig.autofmt_xdate()
ax.set_ylabel("Temperature", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
