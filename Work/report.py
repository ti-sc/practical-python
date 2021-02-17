# report.py
#
# Exercise 2.4
import csv
import sys


def portfolio_cost(filename):
    portfolio = []
    
    with open(filename,'rt') as file:    
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            holding = {
                        headers[0] : row[0] ,
                        headers[1] : int(row[1]) ,
                        headers[2] : float(row[2]) 
                      } 
            portfolio.append(holding)
    return(portfolio)


def read_prices(filename):
    import csv
    prices = []
    with open('Data/prices.csv', 'rt') as file:
        rows = csv.reader(file)
        try:
            for row in rows:
                print(row)
                try:
                    holding = {
                            'name' : row[0] ,
                            'price': float(row[1])
                          }
                    prices.append(holding)
                except ValueError:
                    
                    print('ValueProblem')
        except IndexError:
             print('indexError')
    return(prices)
        
