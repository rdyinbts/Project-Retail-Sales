
#which brand sold the most? in value and volume
#which month did that brand get highest sales? in terms of value and volume



import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

# with open('salesvalue_csv.csv', 'r') as salesval:
#     salesval_reader = csv.DictReader(salesval)
#     for row in salesval_reader:
#         print(row)

val = [[7447, 5966, 8324, 6377, 6944, 6396, 9456, 6420], [576, 405, 365, 392, 357, 446, 559, 564]]
y = range(8)

# plot stacked bar graph
width = 0.45
index = np.arange(11) + 0.75

plt.plot

figure = plt.plot
fig, ax = plt.subplot(1, 1)
blend = ax.bar(index, val[0], width, color="blue")
cpuro = ax.bar(index, val[1], width, bottom=val[0], color="brown")