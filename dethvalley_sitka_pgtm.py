import csv
from datetime import datetime

import matplotlib.pyplot as plt

sitka_file = "data/sitka_weather_2018_simple.csv"
dethvalley_file = "data/death_valley_2018_full.csv"

with open(sitka_file) as sf, open(dethvalley_file) as df:
    s_reader = csv.reader(sf)
    s_header_row = next(s_reader)
    print(s_header_row)

    d_reader = csv.reader(df)
    d_header_row = next(d_reader)
    print(d_header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    #ファイルから日付と降水量を取得する
    dates, s_pgtms, d_pgtms = [], [], []
    for row in s_reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            s_pgtm = float(row[3])
        except ValueError:
            print(f"missing data for {current_date}")
        else:
            dates.append(current_date)
            s_pgtms.append(s_pgtm)

# print(highs)
# print(len(highs))
# print(dates)
# print(len(dates))

#最高気温のグラフを描画する
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, s_pgtms, c="red", alpha=0.5)
#plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

#グラフにフォーマットを指定する
title = "Daily Precipitation - 2018 \nSitka"
plt.title(title, fontsize=20)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
