countries = {
    "Колумбія": {"населення": 50372000, "площа": 1141748},
    "Чилі": {"населення": 19116209, "площа": 756102},
    "Еквадор": {"населення": 17643060, "площа": 283561},
    "Парагвай": {"населення": 7132538, "площа": 406752},
    "Бразилія": {"населення": 212559417, "площа": 8515767},
    "Венесуела": {"населення": 28435943, "площа": 916445}
}

print("Всі записи словника:")
for country, data in countries.items():
    print(f"{country}: населення - {data['населення']}, площа - {data['площа']} км²")

max_area_country = max(countries, key=lambda country: countries[country]['площа'])
print(f"\nКраїна з найбільшою площею: {max_area_country}, площа - {countries[max_area_country]['площа']} км²")

min_area_country = min(countries, key=lambda country: countries[country]['площа'])
min_area = countries[min_area_country]['площа']
print(f"Країна з найменшою площею: {min_area_country}, площа - {min_area} км²")