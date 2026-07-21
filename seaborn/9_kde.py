import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
stock_market = {
    "Date": [
        "2026-01-01", "2026-01-09", "2026-01-21", "2026-01-30",
        "2026-02-09", "2026-02-17", "2026-02-26",
        "2026-03-09", "2026-03-17", "2026-03-25",
        "2026-04-08", "2026-04-17", "2026-04-27",
        "2026-05-06", "2026-05-15", "2026-05-25",
        "2026-06-03", "2026-06-11", "2026-06-12"
    ],
    "Close_Price": [
        1575.6, 1475.3, 1404.6, 1395.4,
        1461.6, 1423.0, 1406.8,
        1424.0, 1397.6, 1413.1,
        1347.8, 1365.0, 1365.8,
        1437.9, 1336.4, 1367.0,
        1313.2, 1263.0, 1293.0
    ]
}
stock_market["Date"] = pd.to_datetime(stock_market["Date"])
#create kde chart
sns.kdeplot(x='Date',fill=True,data=stock_market)
plt.title("Reliance industry stock market data")
plt.xlabel('Date')
plt.ylabel('price')
plt.show()

