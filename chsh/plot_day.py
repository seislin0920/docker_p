import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


# read
station = "GUSH"
datafile = "14030111_day.txt"
df = pd.read_csv(datafile, sep="\s+", header=None, parse_dates=[[0, 1, 2]])
# 設置日期作為索引
df.set_index("0_1_2", inplace=True)


# 繪圖
fig, ax = plt.subplots(figsize=(25, 10))
ax.plot(
    df.index,
    df[3],
    "#016FB9",
    linewidth=3,
)


# 設置標題、軸標籤和圖例
ax.set_title(station, fontsize=24)
ax.set_xlabel("Time (year)", fontsize=16)
ax.set_ylabel("groundwater level (m)", fontsize=16)

ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.xaxis.set_major_locator(mdates.YearLocator())

plt.xticks(fontsize=(10))
plt.ylim([220, 225])

plt.savefig(f"{station}_day.png")

plt.grid(True)
plt.savefig(f"{station}_day_grid.png")
