import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

file_path = "lab_4_part_5.xlsx"
df = pd.read_excel(file_path, header=1)
df["Дата"] = pd.to_datetime(df["Дата"])
df["месяц"] = df["Дата"].dt.to_period("M")
print("Первые строки исходного датафрейма:")
print(df.head())
print("\nРазмерность    :", df.shape)
print("\nСписок товаров:", df["товар"].nunique(), "шт.")
print("Список торговых точек:", df["точка"].nunique(), "шт.\n")
product_month = df.groupby(["товар", "месяц"], as_index=False).agg({
    "Количество": "sum",
    "Продажи": "sum",
    "Себестоимость": "sum"
})
product_month["средняя_цена"] = product_month["Продажи"] / product_month["Количество"]
product_month["маржа"] = product_month["Продажи"] - product_month["Себестоимость"]
tmp = df.groupby(["товар", "месяц", "точка"], as_index=False)["Продажи"].sum()
avg_per_point = tmp.groupby(["товар", "месяц"], as_index=False)["Продажи"].mean()
avg_per_point = avg_per_point.rename(columns={"Продажи": "ср_продажи_на_точку"})
product_month = product_month.merge(avg_per_point, on=["товар", "месяц"], how="left")
product_month = product_month.sort_values(["товар", "месяц"])
product_month["рост_продаж_%"] = product_month.groupby("товар")["Продажи"].pct_change() * 100
product_month["рост_количества_%"] = product_month.groupby("товар")["Количество"].pct_change() * 100
print("Агрегированные показатели по товарам и месяцам:")
print(product_month.head(), "\n")
point_month = df.groupby(["точка", "месяц"], as_index=False).agg({
    "Количество": "sum",
    "Продажи": "sum",
    "Себестоимость": "sum"
})
point_month["средняя_цена"] = point_month["Продажи"] / point_month["Количество"]
point_month["маржа"] = point_month["Продажи"] - point_month["Себестоимость"]
point_month = point_month.sort_values(["точка", "месяц"])
point_month["рост_продаж_%"] = point_month.groupby("точка")["Продажи"].pct_change() * 100
point_month["рост_количества_%"] = point_month.groupby("точка")["Количество"].pct_change() * 100
print("Агрегированные показатели по торговым точкам и месяцам:")
print(point_month.head(), "\n")
turnover_month = df.groupby("месяц").agg({
    "Количество": "sum",
    "Продажи": "sum",
    "Себестоимость": "sum"
})
turnover_month["средняя_цена"] = turnover_month["Продажи"] / turnover_month["Количество"]
turnover_month["маржа"] = turnover_month["Продажи"] - turnover_month["Себестоимость"]
turnover_month["рост_продаж_%"] = turnover_month["Продажи"].pct_change() * 100

print("Общий товарооборот по месяцам:")
print(turnover_month.head(), "\n")
plt.figure(figsize=(10, 5))
plt.plot(turnover_month.index.to_timestamp(), turnover_month["Продажи"], marker="o")
plt.title("Динамика общего товарооборота (выручка)")
plt.xlabel("Месяц")
plt.ylabel("Продажи, руб.")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 5))
plt.plot(turnover_month.index.to_timestamp(), turnover_month["маржа"], marker="o")
plt.title("Динамика общей маржи")
plt.xlabel("Месяц")
plt.ylabel("Маржа, руб.")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


top_products = (df.groupby("товар")["Продажи"]
                  .sum()
                  .sort_values(ascending=False)
                  .head(5)
                  .index)

print("ТОП-5 товаров по выручке:")
print(top_products, "\n")

for product in top_products:
    data_p = product_month[product_month["товар"] == product].sort_values("месяц")
    x = data_p["месяц"].dt.to_timestamp()

    plt.figure(figsize=(10, 5))
    plt.plot(x, data_p["Продажи"], marker="o")
    plt.title(f"Динамика продаж (выручка) по товару {product}")
    plt.xlabel("Месяц")
    plt.ylabel("Продажи, руб.")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(x, data_p["Количество"], marker="o")
    plt.title(f"Динамика количества продаж по товару {product}")
    plt.xlabel("Месяц")
    plt.ylabel("Количество, шт.")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

top_points = (df.groupby("точка")["Продажи"]
                .sum()
                .sort_values(ascending=False)
                .head(5)
                .index)

print("ТОП-5 точек по выручке:")
print(top_points, "\n")

for point in top_points:
    data_t = point_month[point_month["точка"] == point].sort_values("месяц")
    x = data_t["месяц"].dt.to_timestamp()

    plt.figure(figsize=(10, 5))
    plt.plot(x, data_t["Продажи"], marker="o")
    plt.title(f"Динамика продаж (выручка) по точке {point}")
    plt.xlabel("Месяц")
    plt.ylabel("Продажи, руб.")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

forecast_horizon = 3   
all_forecasts = []
for product, group in product_month.groupby("товар"):
    group_sorted = group.sort_values("месяц")

    y = group_sorted["Продажи"].values
    x = np.arange(len(y))
    res = linregress(x, y)
    x_future = np.arange(len(y), len(y) + forecast_horizon)
    y_future = res.intercept + res.slope * x_future
    last_period = group_sorted["месяц"].max()
    future_periods = pd.period_range(last_period + 1,
                                     periods=forecast_horizon,
                                     freq="M")

    fdf = pd.DataFrame({
        "товар": product,
        "месяц": future_periods,
        "прогноз_продаж": y_future
    })
    all_forecasts.append(fdf)

forecast_result = pd.concat(all_forecasts, ignore_index=True)

print("Прогноз продаж по каждому товару (первые строки):")
print(forecast_result.head(), "\n")

example_product = top_products[0] 
fact = product_month[product_month["товар"] == example_product].sort_values("месяц")
fact_x = fact["месяц"].dt.to_timestamp()

forecast_example = forecast_result[forecast_result["товар"] == example_product] \
                      .sort_values("месяц")
forecast_x = forecast_example["месяц"].dt.to_timestamp()

plt.figure(figsize=(10, 5))
plt.plot(fact_x, fact["Продажи"], marker="o", label="факт")
plt.plot(forecast_x, forecast_example["прогноз_продаж"], marker="x",
         linestyle="--", label="прогноз")
plt.title(f"Продажи и прогноз для товара {example_product}")
plt.xlabel("Месяц")
plt.ylabel("Продажи, руб.")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

