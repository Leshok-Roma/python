import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


file_path = "lab_4_part_5.xlsx"
df = pd.read_excel(file_path, header=1)

df["Дата"] = pd.to_datetime(df["Дата"], errors="coerce")
df = df.dropna(subset=["Дата", "товар", "точка"])
df["месяц"] = df["Дата"].dt.to_period("M")

for col in ["Количество", "Продажи", "Себестоимость"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

print("Первые строки датасета:")
print(df.head(), "\n")
print("Размерность датасета:", df.shape)
print("Количество товаров:", df["товар"].nunique())
print("Количество торговых точек:", df["точка"].nunique())
print("Период:", df["месяц"].min(), "—", df["месяц"].max())

product_month = df.groupby(["товар", "месяц"], as_index=False).agg({
    "Количество": "sum",
    "Продажи": "sum",
    "Себестоимость": "sum"
})

product_month["средняя_цена"] = product_month["Продажи"] / product_month["Количество"].replace(0, np.nan)
product_month["маржа"] = product_month["Продажи"] - product_month["Себестоимость"]

tmp = df.groupby(["товар", "месяц", "точка"], as_index=False)["Продажи"].sum()
avg_per_point = tmp.groupby(["товар", "месяц"], as_index=False)["Продажи"].mean()
avg_per_point.rename(columns={"Продажи": "ср_продажи_на_точку"}, inplace=True)

product_month = product_month.merge(avg_per_point, on=["товар", "месяц"], how="left")
product_month = product_month.sort_values(["товар", "месяц"])
product_month["рост_продаж_%"] = product_month.groupby("товар")["Продажи"].pct_change() * 100
product_month["рост_количества_%"] = product_month.groupby("товар")["Количество"].pct_change() * 100

print("\nАнализ продаж по товарам (первые строки):")
print(product_month.head())
point_month = df.groupby(["точка", "месяц"], as_index=False).agg({
    "Количество": "sum",
    "Продажи": "sum",
    "Себестоимость": "sum"
})
point_month["средняя_цена"] = point_month["Продажи"] / point_month["Количество"].replace(0, np.nan)
point_month["маржа"] = point_month["Продажи"] - point_month["Себестоимость"]
point_month = point_month.sort_values(["точка", "месяц"])
point_month["рост_продаж_%"] = point_month.groupby("точка")["Продажи"].pct_change() * 100
point_month["рост_количества_%"] = point_month.groupby("точка")["Количество"].pct_change() * 100
print("\nАнализ продаж по торговым точкам (первые строки):")
print(point_month.head())
turnover_month = df.groupby("месяц").agg({
    "Количество": "sum",
    "Продажи": "sum",
    "Себестоимость": "sum"
}).sort_index()
turnover_month["средняя_цена"] = turnover_month["Продажи"] / turnover_month["Количество"].replace(0, np.nan)
turnover_month["маржа"] = turnover_month["Продажи"] - turnover_month["Себестоимость"]
turnover_month["рост_продаж_%"] = turnover_month["Продажи"].pct_change() * 100
turnover_month["рост_количества_%"] = turnover_month["Количество"].pct_change() * 100
print("\nДинамика общего товарооборота:")
print(turnover_month.head())

total_revenue = df["Продажи"].sum()
total_cost = df["Себестоимость"].sum()
total_margin = total_revenue - total_cost
total_qty = df["Количество"].sum()
avg_price = total_revenue / total_qty if total_qty != 0 else np.nan

print("\n" + "=" * 70)
print("ОТЧЕТ: АНАЛИЗ ПРОДАЖ")
print("/" * 70)
print(f"Период: {df['месяц'].min()} — {df['месяц'].max()}")
print(f"Товаров: {df['товар'].nunique()} | Точек: {df['точка'].nunique()} | Записей: {len(df)}")
print("/" * 70)
print(f"ИТОГО количество: {total_qty:,.0f} шт.".replace(",", " "))
print(f"ИТОГО выручка: {total_revenue:,.2f} руб.".replace(",", " ").replace(".", ","))
print(f"ИТОГО себестоимость: {total_cost:,.2f} руб.".replace(",", " ").replace(".", ","))
print(f"ИТОГО маржа: {total_margin:,.2f} руб.".replace(",", " ").replace(".", ","))
print(f"СРЕДНЯЯ цена: {avg_price:,.2f} руб.".replace(",", " ").replace(".", ","))
print("/" * 70)

best_month = turnover_month["Продажи"].idxmax()
worst_month = turnover_month["Продажи"].idxmin()
print(f"Лучший месяц по выручке: {best_month} ({turnover_month.loc[best_month,'Продажи']:,.2f} руб.)".replace(",", " ").replace(".", ","))
print(f"Худший месяц по выручке: {worst_month} ({turnover_month.loc[worst_month,'Продажи']:,.2f} руб.)".replace(",", " ").replace(".", ","))
print("/" * 70)

top_products = (df.groupby("товар")["Продажи"].sum().sort_values(ascending=False).head(5).index.tolist())
top_points = (df.groupby("точка")["Продажи"].sum().sort_values(ascending=False).head(5).index.tolist())

print("\nТОП-5 товаров по выручке:", top_products)
print("ТОП-5 точек по выручке:", top_points)

x_all = turnover_month.index.to_timestamp()

plt.figure(figsize=(10, 5))
plt.plot(x_all, turnover_month["Продажи"], marker="o")
plt.title("Динамика общего товарооборота (выручка)")
plt.xlabel("Месяц")
plt.ylabel("Продажи, руб.")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(x_all, turnover_month["маржа"], marker="o")
plt.title("Динамика общей маржи")
plt.xlabel("Месяц")
plt.ylabel("Маржа, руб.")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(x_all, turnover_month["рост_продаж_%"], marker="o")
plt.title("Темп роста общего товарооборота, %")
plt.xlabel("Месяц")
plt.ylabel("Рост, %")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(x_all, turnover_month["Количество"], marker="o")
plt.title("Динамика общего количества продаж")
plt.xlabel("Месяц")
plt.ylabel("Количество, шт.")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


for product in top_products:
    data_p = product_month[product_month["товар"] == product].sort_values("месяц")
    x = data_p["месяц"].dt.to_timestamp()

    plt.figure(figsize=(10, 4))
    plt.plot(x, data_p["Продажи"], marker="o")
    plt.title(f"Товар: {product} — выручка по месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Продажи, руб.")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(x, data_p["Количество"], marker="o")
    plt.title(f"Товар: {product} — количество по месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Количество, шт.")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(x, data_p["средняя_цена"], marker="o")
    plt.title(f"Товар: {product} — средняя цена по месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Цена, руб.")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(x, data_p["ср_продажи_на_точку"], marker="o")
    plt.title(f"Товар: {product} — средние продажи на точку")
    plt.xlabel("Месяц")
    plt.ylabel("Выручка на точку, руб.")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


for point in top_points:
    data_t = point_month[point_month["точка"] == point].sort_values("месяц")
    x = data_t["месяц"].dt.to_timestamp()

    plt.figure(figsize=(10, 4))
    plt.plot(x, data_t["Продажи"], marker="o")
    plt.title(f"Точка: {point} — выручка по месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Продажи, руб.")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(x, data_t["Количество"], marker="o")
    plt.title(f"Точка: {point} — количество по месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Количество, шт.")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(x, data_t["рост_продаж_%"], marker="o")
    plt.title(f"Точка: {point} — рост/спад выручки, %")
    plt.xlabel("Месяц")
    plt.ylabel("Рост, %")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


forecast_horizon = 3
all_forecasts = []

for product, group in product_month.groupby("товар"):
    group = group.sort_values("месяц")
    y = group["Продажи"].values
    if len(y) < 2:
        continue  
    x = np.arange(len(y))
    res = linregress(x, y)
    x_future = np.arange(len(y), len(y) + forecast_horizon)
    y_future = res.intercept + res.slope * x_future
    y_future = np.clip(y_future, 0, None)  
    future_months = pd.period_range(
        start=group["месяц"].max() + 1,
        periods=forecast_horizon,
        freq="M"
    )

    forecast_df = pd.DataFrame({
        "товар": product,
        "месяц": future_months,
        "прогноз_продаж": y_future
    })
    all_forecasts.append(forecast_df)

forecast_result = pd.concat(all_forecasts, ignore_index=True)

print("\nПрогноз продаж по товарам:")
print(forecast_result.head())
example_product = top_products[0] if len(top_products) > 0 else product_month["товар"].iloc[0]
fact = product_month[product_month["товар"] == example_product].sort_values("месяц")
forecast = forecast_result[forecast_result["товар"] == example_product].sort_values("месяц")
x_fact = fact["месяц"].dt.to_timestamp()
x_fore = forecast["месяц"].dt.to_timestamp()
plt.figure(figsize=(10, 5))
plt.plot(x_fact, fact["Продажи"], marker="o", label="Факт")

if not forecast.empty:
    x_joined = pd.concat([x_fact.iloc[-1:], x_fore])
    y_joined = pd.concat([fact["Продажи"].iloc[-1:], forecast["прогноз_продаж"]])
    plt.plot(x_joined, y_joined, marker="x", linestyle="--", label="Прогноз")

plt.title(f"Факт и прогноз продаж товара: {example_product}")
plt.xlabel("Месяц")
plt.ylabel("Продажи, руб.")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nанализ, графики, прогноз построены." , "HAPPY END" , sep = '\n')
