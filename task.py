import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_excel("s7_data_sample_rev4_50k.xlsx")

print(df.columns)
date_col = 'ISSUE_DATE'
print(f" Используем колонку даты: {date_col}")

df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
df["year"] = df[date_col].dt.year
df["month"] = df[date_col].dt.month
print(df.describe(include="all").transpose(), "\n")

airport_counts = df["ORIG_CITY_CODE"].value_counts()
plt.figure(figsize=(10, 5))
airport_counts.head(15).plot(kind="bar", color="skyblue")
plt.title("Топ-15 городов по количеству вылетов")
plt.ylabel("Количество")
plt.grid(axis='y', alpha=0.4)
plt.tight_layout()
plt.show()

monthly_sales = df.groupby("month")["REVENUE_AMOUNT"].sum()
plt.figure(figsize=(8, 4))
monthly_sales.plot(marker="o", color="blue")
plt.title("Сезонность продаж (сумма продаж по месяцам)")
plt.xlabel("Месяц")
plt.ylabel("Сумма продаж")
plt.grid(True)
plt.tight_layout()
plt.show()

monthly_avg = df.groupby("month")["REVENUE_AMOUNT"].mean()
plt.figure(figsize=(8, 4))
monthly_avg.plot(kind="bar", color="orange")
plt.title("Средний чек по месяцам")
plt.xlabel("Месяц")
plt.ylabel("Средний чек")
plt.grid(axis="y", alpha=0.4)
plt.tight_layout()
plt.show()

pax_counts = df["PAX_TYPE"].value_counts()
plt.figure(figsize=(6, 4))
pax_counts.plot(kind="bar", color="green")
plt.title("Распределение пассажиров по статусам")
plt.ylabel("Количество")
plt.grid(axis="y", alpha=0.4)
plt.tight_layout()
plt.show()

pay_counts = df["FOP_TYPE_CODE"].value_counts()
plt.figure(figsize=(6, 4))
pay_counts.plot(kind="bar", color="purple")
plt.title("Популярность способов оплаты")
plt.ylabel("Количество")
plt.grid(axis="y", alpha=0.4)
plt.tight_layout()
plt.show()


