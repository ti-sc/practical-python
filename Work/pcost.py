# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    total = 0
    with open(filename,'rt') as portfolio:
        next(portfolio)
        rows = csv.reader(portfolio)
        for row in rows:
            try:
                n = int(row[1])
                m = float(row[2])
                total = total + n * m
            except ValueError:
                print('Data is corrupted',row)
        
    return(total)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost: ',cost)