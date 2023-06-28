import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


# read
station = "CHSH"
datafile = "14060111_hr.txt"
data = pd.read_csv(
    datafile,
    sep="\s+",
    header=None,
    names=["Year", "Month", "Day"] + list(range(1, 25)),
)
# 將年、月、日欄位結合成日期欄位
data["Date"] = pd.to_datetime(data[["Year", "Month", "Day"]])

# 將日期欄位設定為索引
data.set_index("Date", inplace=True)

# 處理每列每行的水位資料
hourly_data = data.loc[:, 1:]  # 冒號 : 表示選取所有的列，而 '1': 則表示選取從欄位 '1' 到最後一個欄位的所有欄位。
# stack()將每列水位全變成行資料,reset_index()保留原本索引號
hourly_data = hourly_data.stack().reset_index()
hourly_data = hourly_data[hourly_data[0] != -999998]

# 繪圖
fig, ax = plt.subplots(figsize=(25, 10))
ax.plot(
    hourly_data.Date,
    hourly_data[0],
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
plt.ylim([240, 280])

plt.savefig(f"{station}_hr.png")

plt.grid(True)
plt.savefig(f"{station}_hr_grid.png")
