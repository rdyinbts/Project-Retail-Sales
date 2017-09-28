# import csv file
import csv

# read csv file
with open('salesvalue_csv.csv', 'r') as salesval:
    csv_reader = csv.reader(salesval)

    for row in csv_reader:
        print(row)

# parse? file

# for each month, get total sales value per brand

# for each month, get total sales = sum of sales for all brands

# do this for each month from January to August 2017

# graph 1: stacked column
# column contain total monthly sales of Coffee from Jan-Aug 2017
# x-axis is months, y axis is value

# graph 2: line graph
# add line graph for each brand (each line corresponds to one brand)
# overlay graph 2 on graph 1

#TODO create a command line interface that allows you to type in brand names and show graphs for the brands you want to
# compare. You have to show the legend for each graph


