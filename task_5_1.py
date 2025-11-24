import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import argparse
import re

def load_page(country, cache_folder="cache"):
    if not os.path.exists(cache_folder):
        os.makedirs(cache_folder)
    cache_file = os.path.join(cache_folder, f"{country}.html")
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()
    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
    except:
        print(f" Cann't load page : {country}")
        return None


    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(html)

    time.sleep(1)  
    return html

def parse_country_data(html):
    soup = BeautifulSoup(html, "html.parser")

    infobox = soup.find("table", class_="infobox")
    if infobox is None:
        return None, None, None
    capital = None
    area = None
    population = None
    rows = infobox.find_all(["tr"])
    for row in rows:
        header = row.find("th")
        value = row.find("td")

        if not header or not value:
            continue

        text = header.get_text(strip=True)
        if "Capital" in text:
            capital = value.get_text(" ", strip=True)        
        if "Area" in text:
            area_text = value.get_text(" ", strip=True)
            digits = re.findall(r"[\d,]+", area_text)
            if digits:
                area = digits[0].replace(",", "")        
        if "Population" in text:
            pop_text = value.get_text(" ", strip=True)
            digits = re.findall(r"[\d,]+", pop_text)
            if digits:
                population = digits[0].replace(",", "")

    return capital, area, population

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="countries.txt")
    parser.add_argument("--output", default="countries_data.csv")
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    with open(input_file, "r", encoding="utf-8") as f:
        countries = [line.strip() for line in f if line.strip()]

    data = []

    for country in countries:
        print(f" Country : {country}")

        html = load_page(country)
        if not html:
            continue

        capital, area, population = parse_country_data(html)    
        capital = capital or "N/A"
        area = area or "N/A"
        population = population or "N/A"

        data.append([country, capital, area, population])
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["country", "capital", "area", "population"])
        writer.writerows(data)

    print(f" Data saved in  {output_file}")


if __name__ == "__main__":
    main()
