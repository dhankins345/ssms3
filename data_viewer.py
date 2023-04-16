import settings, csv

stockDay = 1

def textOutput(stockDay):
    marketLine = stockDay-1
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
    for x in range(len(settings.stock_symbols)):
        print('{:10}'.format(settings.stock_symbols[x]) + '{:40}'.format(settings.stock_names[x]) + "$ " + '{:>6}'.format(marketList[x]) + '{:>14}'.format(marketChg[x]))

    print("---------------------------------------------------------------------------------")

    wait = input("PRESS ENTER TO SCROLL OR PRESS Q TO QUIT - ")
    if wait == "Q" or wait == "q":
        quit()
    elif stockDay >= settings.days:
        stockDay = 1
        textOutput(stockDay)
    else:
        stockDay+=1
        textOutput(stockDay)

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