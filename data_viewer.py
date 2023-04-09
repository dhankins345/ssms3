import settings, csv

stockDay = 1

def textOutput(stockDay):
    # Generate Header
    print("")
    print("STOCK MARKET SIMULATOR")
    print("---------------------------------------------------------------------------------")
    print("Day: " + str(stockDay) + "   +++   " + "Total Market at Close: $" + str(closeTotal) + "   +++   " + "Change in Market: " + str(changeMark))
    print("---------------------------------------------------------------------------------")

    # Enumerate Stocks
    for x in range(len(stock_symbols)):
        if a == 0: print('{:10}'.format(settings.stock_symbols[x]) + '{:40}'.format(settings.stock_names[x]) + "$" + '{:>7.2f}'.format(stock_price[x]) + '{:>14}'.format(stock_change[x]))
        elif a >= 1: print('{:10}'.format(settings.stock_symbols[x]) + '{:40}'.format(settings.stock_names[x]) + "$" + '{:>7.2f}'.format(stock_price[x]) + '{:>+15.2f}'.format(stock_change[x]))

    print("---------------------------------------------------------------------------------")

    wait = input("PRESS < OR > TO SCROLL OR PRESS Q TO QUIT. > ");
    if wait == "<" and stockDay > 1:
        stockDay = stockDay-1
        textOutput(stockDay)
    if wait == ">" and stockDay < settings.days:
        stockDay = stockDay+1
        textOutput(stockDay)
    if wait == "Q" or wait == "q":
        quit()
    print("")
    textOutput()

with open(settings.datafile, 'r') as inputfile:
    textOutput(stockDay)