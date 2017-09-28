import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

brands = ["Blend 45", "Cafe Puro", "Great Taste", "Jimm's", "Kopiko", "Maskape", "Nescafe", "RD Prince Coffee", "Samis",
          "Sams", "San Mig Coffee"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]

# iterate each row
# add all the value
# append to a list

total = []
with open('salesvalue_csv.csv', 'r') as salesval:
    salesval_reader = csv.DictReader(salesval)
    for row in salesval_reader:
        for brand in brands:
            sum = []
            if row["Month"] == "Jan":
                jan = row[brand]
                sum += jan
    total.append(sum)
print(total)

#graph 1 - bar graph
# total cf category

# for row in salesval:
#     pass
    # get sum of each row

    # display as each row (months)


# y , stacked column are the brands
# blend = []
# cpuro = []
# great = []
# jimms = []
# kopik = []
# maskp = []
# nescf = []


# blend = ax.bar(index, val[0], width, color="blue")
# cpuro = ax.bar(index, val[1], width, bottom=val[0], color="brown")
# great = ax.bar(index, val[2], width, bottom=val[0] + val[1], color="green")
# jimms = ax.bar(index, val[3], width, bottom=val[0] + val[1] + val[2], color="violet")
# kopik = ax.bar(index, val[4], width, bottom=val[0] + val[1] + val[2] + val[3], color="orange")
# maskp = ax.bar(index, val[5], width, bottom=val[0] + val[1] + val[2] + val[3] + val[4], color="red")


# x axis
# months = range(9)  # change data labels later to J, F, M, to Aug


# plt.plot(x,y, label='Sales Value')
# plt.xlabel('Value in Php')
# plt.ylabel('2017')
# plt.title("Coffee Sales in 2017")
# plt.legend()
# plt.show()

# import tick labels
# xaxis = np.loadtxt('salesvalue_csv.csv', dtype='str', delimiter=',', skiprows=1, usecols=(0,))
#
# #plot stacked bar graph
# width = 0.45
# index = np.arange(11) + 0.75
#
# fig, ax = plt.subplots(1, 1)
# blend = ax.bar(index, val[0], width, color="blue")
# cpuro = ax.bar(index, val[1], width, bottom=val[0], color="brown")
# great = ax.bar(index, val[2], width, bottom=val[0] + val[1], color="green")
# jimms = ax.bar(index, val[3], width, bottom=val[0] + val[1] + val[2], color="violet")
# kopik = ax.bar(index, val[4], width, bottom=val[0] + val[1] + val[2] + val[3], color="orange")
# maskp = ax.bar(index, val[5], width, bottom=val[0] + val[1] + val[2] + val[3] + val[4], color="red")
#
# ax.set_ylabel("sales value in PhP")
# ax.set_xlabel("Month")
# ax.set_xticks(index+width/2.)
# ax.set_xticklabels(xaxis, rotation=70)
#
#
# fig.legend((blend[0], cpuro[1], great[2], jimms[3], kopik[4], maskp[5]), ("Blend 45", 'Cafe Puro', "Great Taste",
#                                                                           "Jimm's", "Kopiko", "Maskape"))
# fig.tight_layout()
# print(fig.show())

# do this for each month from January to August 2017

# graph 1: stacked column
# column contain total monthly sales of Coffee from Jan-Aug 2017
# x-axis is months, y axis is value

# get coffee sales value per month


# graph 2: line graph
# add line graph for each brand (each line corresponds to one brand)
# overlay graph 2 on graph 1

# to create a command line interface that allows you to type in brand names and show graphs for the brands you want to
# compare. You have to show the legend for each graph


    # for each month, get total sales value per brand

    # for each month, get total sales = sum of sales for all brands

    # do this for each month from January to August 2017
