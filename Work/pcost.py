# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    total = 0
    with open(filename,'rt') as portfolio:
        next(portfolio)
        for line in portfolio:
            row = line.split(',')
            try:
                n = int(row[1])
                m = float(row[2])
                total = total + n * m
            except ValueError:
                print('Data is corrupted',line)
        
    return(total)

cost = portfolio_cost('Work/Data/portfolio.csv')
print('Total cost: ',cost)