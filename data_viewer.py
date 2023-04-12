import settings, csv

stockDay = 1

def textOutput(stockDay):
    marketLine = (3 * stockDay) - 3
    marketStat = marketinfo[marketLine]
    marketList = marketprice[marketLine]
    marketChg = marketchange[marketLine]
    # Generate Header
    print("")
    print("SIMPLE STOCK MARKET SIMULATOR")
    print("---------------------------------------------------------------------------------")
    print(f"Day: {stockDay}   +++   Total Market at Close: ${marketStat[1]}   +++   Change in Market: {marketStat[2]}")
    print("---------------------------------------------------------------------------------")

    # Enumerate Stocks
    for x in range(len(stock_symbols)):
        if a == 0: print('{:10}'.format(settings.stock_symbols[x]) + '{:40}'.format(settings.stock_names[x]) + "$" + '{:>7.2f}'.format(stock_price[x]) + '{:>14}'.format(stock_change[x]))
        elif a >= 1: print('{:10}'.format(settings.stock_symbols[x]) + '{:40}'.format(settings.stock_names[x]) + "$" + '{:>7.2f}'.format(stock_price[x]) + '{:>+15.2f}'.format(stock_change[x]))

    print("---------------------------------------------------------------------------------")

    wait = input("PRESS < OR > TO SCROLL OR PRESS Q TO QUIT - ");
    if wait == "<" and stockDay > 1:
        stockDay = stockDay-1
        textOutput(stockDay)
    if wait == ">" and stockDay < settings.days:
        stockDay = stockDay+1
        textOutput(stockDay)
    if wait == "Q" or wait == "q":
        quit()

# create lists to store values from csv
marketinfo = []
marketprice = []
marketchange = []
dayRows = 1
dayCSV = 1

# load values from CSV
with open(settings.datafile, 'r') as inputfile:
    csv_reader = csv.reader(inputfile, delimiter=',')
    for row in csv_reader:
        if dayRows == 1:
            marketinfo.append(row)
        if dayRows == 2:
            marketprice.append(row)
        if dayRows == 3:
            marketchange.append(row)
            dayCSV += 1
            dayRows = 0
        dayRows += 1

textOutput(stockDay)