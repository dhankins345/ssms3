from random import *
import settings

stockprices = settings.stock_price

# Autogen Total Market Value
x = 0
closeTotalOld = 0.00
closeTotal = 0.00
while x < len(settings.stock_price):
	origTotal = stockprices[x]
	closeTotalOld = closeTotalOld + origTotal
	x += 1
closeTotalOld = closeTotalOld * settings.totalvalue

# Set up variables
global stockDay
global dur
dur = 0
changeMark = "N/A"

# Create blank lists to use later
stock_price_old = []
stock_change = []
stock_change_old = []

x = 0
while x < len(settings.stock_symbols):
  stock_change.append("N/A")
  x += 1

# Below is the main guts of the program
def stockSim(duration):
	global closeTotalOld
	global closeTotal
	global totalvalue
	global stockDay
	global dur

	# Calculate Stocks
	if dur > 0:
		closeTotalOld = closeTotal
		x = 0
		for x in range(len(settings.stock_symbols)):
			stock_price_old.append(stockprices[x])
			stock_change_old.append(stock_change[x])
			maxchange = stockprices[x] * settings.volatility
			changeStock0 = random() * maxchange
			posNeg = random()
			if posNeg < 0.5:
				changeStock1 = changeStock0 * 2
				changeStock2 = changeStock0 - changeStock1
				stock_change[x] = '%.2f'%(changeStock2)
			else:
				changeStock2 = changeStock0
				stock_change[x] = "+" + '%.2f'%(changeStock2)
			stockprices[x] = stock_price_old[x] + changeStock2

	# Calculate Total
	finalTotal = 0.00

	x = 0
	for x in range(len(settings.stock_symbols)):
		runningTotal = stockprices[x]
		finalTotal = finalTotal + runningTotal

	closeTotal = finalTotal * settings.totalvalue

	# Calculate Market Difference
	changeMarkpre = closeTotal - closeTotalOld
	if dur == 0: changeMark = "N/A"
	else:
		if changeMarkpre < 0: changeMark = '%.2f'%(changeMarkpre)
		else: changeMark = "+" + '%.2f'%(changeMarkpre)

	# Generate day info
	log_file.write(str(dur+1) + "," + '%.2f'%(closeTotal) + "," + str(changeMark))
	log_file.write("\n")

	# Enumerate Stocks
	x = 0
	for x in range(len(settings.stock_symbols)):
		log_file.write('%.2f'%(stockprices[x]) + ",")
	
	log_file.write("\n")
	for x in range(len(settings.stock_symbols)):
		log_file.write(str(stock_change[x]) + ",")

	if dur+2 > duration:
		quit()
	else:
		dur += 1
		stock_price_old.clear()
		stock_change_old.clear()
		log_file.write("\n")
		stockSim(duration)
  
# Prepare log file and run main program
with open(settings.outputfile, "w") as log_file:
	stockSim(settings.days)