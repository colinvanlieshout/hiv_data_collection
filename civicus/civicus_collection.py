import pycountry
import datetime
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

site = requests.get("https://monitor.civicus.org/")
# Saving the data
data = site.content
# Creating the soup
soup = BeautifulSoup(data, "html.parser")
pattern = re.compile(r"var COUNTRIES_DATA = .")
script_values = soup.find("script", text=pattern)  # was 6 in last edition
script_values_str = str(script_values)

#stores it as a txt file, this makes it possible to split lines when opening again
text_file = open("script_values.txt", "w")
n = text_file.write(script_values_str)
text_file.close()

script_text = open("script_values.txt", "r")
script_list = []
for line in script_text:
    line = line.replace("\n", "")
    script_list.append(line)

values = script_list[4:]

def get_value(text):
    return text.partition('\'')[2].rpartition('\'')[0]

df = pd.DataFrame(columns=['CountryCode', 'measure_value'])

for i, v in enumerate(values):
    if ': {' in v:
        code = get_value(v)
        if len(code) > 3:  # exclude Kosovo
            continue
        code = code if code != 'SVT' else 'VCT'  # Deze code staat verkeerd in lijst
        fill = get_value(values[i + 2])
        df.loc[len(df)] = [code, fill]

year = '2020'
df['Country'] = df.apply(lambda r: pycountry.countries.get(alpha_3=r['CountryCode']).name, axis=1)
df['Year'] = year
df['Indicator_category'] = 'Country'
df['Indicator'] = 'Civicus score'
df['unit_of_measure'] = 'Number'
df['Source'] = 'Civicus monitor'
df.to_csv('civicus_monitor_augustus_' + year + '.csv')