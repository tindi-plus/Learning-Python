# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:07:24 2021.

Metric to English unit conversions

@author: Tindi.Sommers
"""
import re
import pandas as pd

# create a conversion table ie a dataFrame with the conversion constants
#       millimeters centimeters meters kilometers
# inches 25.4        2.54       0.0254     0.0000254
# yards  914.4       91.44      0.9144     0.0009144
# feet   304.8       30.48      0.3048     0.0003048
metric_length = {'millimeters': [25.4, 914.4, 304.8],
                 'centimeters': [2.54, 91.44, 30.48],
                 'meters': [0.0254, 0.9144, 0.3048],
                 'kilometers': [0.0000254, 0.0009144, 0.0003048]}
length_data = pd.DataFrame(metric_length, index=['inches', 'yards', 'feet'])
# create a conversion table ie a dataFrame with the conversion constants
#         grams       kilograms
# pounds  453.592     0.453592
metric_mass = {'grams': 453.592, 'kilograms': 0.453592}
mass_data = pd.DataFrame(metric_mass, index=['pounds'])

# create a conversion table ie a dataFrame with the conversion constants
#         milliliters  liters
# quarts    1136.52     1.13652
metric_volume = {'milliliters': 1136.52, 'liters': 1.13652}
volume_data = pd.DataFrame(metric_volume, index=['quarts'])

# data for checking validity of conversions
# length = ['millimeters', 'centimeters', 'meters',
#          'kilometers', 'inches', 'yards', 'feet']

# obtain the conversion units and values from user
question = input('Input your question. All units should be plural eg how many inches are in 1 meters?: ')
print()
result = re.search(r'\w{3} \w{4} (\w+) \w{3} \w\w ([0-9]+) ([a-z]+)', question)
# check that the format is correct
if not result:
    print('The format you entered is not correct. The format is: How many inches are in 2 meters?')
    raise SystemExit()

# extract the units for conversion
unitIn = result.group(1)
unitOut = result.group(3)
value = float(result.group(2))

data_list = [length_data, mass_data, volume_data]

valid_units = False  # variable for if the conversion is valid
for data in data_list:
    # verify that both units are compatible ie are found in the same dataframe
    # by checking if the units can be found in the dataframe's keys or index
    if unitIn in data.keys() and unitOut in data.index:
        converted_value = value * data.at[unitOut, unitIn]
        print(f'There are {converted_value:.3f} {unitIn} in {value} {unitOut}')
        valid_units = True
    elif unitIn in data.index and unitOut in data.keys():
        converted_value = value / data.at[unitIn, unitOut]
        print(f'There are {converted_value:.3f} {unitIn} in {value} {unitOut}')
        valid_units = True

if not valid_units:
    print(f'{unitIn} is not a valid conversion to {unitOut}.')




