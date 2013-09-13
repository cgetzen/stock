def sma(price, length):
    # price is list of prices for each day (ex. [10, 10.20, 10.30 ... ]
    # length is length of sma (ex. 20 day sma)
    sma = []
    for day in range(0, len(price)):
	sum=0
	if day >= length-1: # day starts at zero and length starts at 1
	    for l in range(0,length):
		sum += price[day-l]
	    sma.append(sum/length)
	else:
	    sma.append(None)
    
    return sma

def ema(price, length):
    # EMAtoday = a * (p1 + (1-a)*p2 + (1-a)2 * p3 ... )
    #(current day's closing price x Exponent) + (previous day's EMA x (1-Exponent)) 
    
    ema = []
    alpha = 2./(length+1)
    for day in range(0, len(price)):
	if day == length-1:
	    sum = 0
	    for l in range(0,length):
		sum += price[day-l]
	    ema.append(sum/length)
	elif day >= length:
	    ema.append((price[day]-ema[-1])*alpha + ema[-1])
	else:
	     ema.append(None)
    return ema
    
    '''
    for day in range(0, len(price)):
	if day>=length-1:
	    EMAtoday=0
	    for l in range(0, length):
		EMAtoday += alpha*((1-alpha)**l)*price[day-l]
	    ema.append(EMAtoday)
	else:
	    ema.append(None)
    print ema
    '''

def simple_moving_average(STOCKAdj, startday, length):
	# STOCKAdj	list with all closing values
	# days		number of days (20, 50, 100)
	# startday	the beginning day (right now, numerical)
	
	if startday < length:
		return None
	# stockprices	fetches only the closing values we need, in reverse order
	stockprices = STOCKAdj[startday:(startday-length):-1]
	
	
	stockprices = STOCKAdj[(startday-length):startday]
	stockprices.reverse()

	SMA = sum(float(eachprice) for eachprice in stockprices)/len(stockprices)

	return SMA
	



# input  1,2,3, [], 


def exponential_moving_average(STOCKAdj, startday, length, oldEMA):
	
#EMA: {Close - EMA(previous day)} x multiplier + EMA(previous day). 

	# Multiplier is calculated like this: (2 / (Time periods + 1) ) 
	# EMA,
	# stockprices
	if startday < length:
		return None#float(STOCKAdj[startday]) #float(stockprices[1])
	# stockprices	fetches only the closing values we need, in reverse order
	elif startday == length:
		return simple_moving_average(STOCKAdj, startday, length)
	else:
		stockprices = STOCKAdj[(startday-length):startday]
		stockprices.reverse()
	
		for x in range(0, len(stockprices)):
			stockprices[x]=float(stockprices[x])
		alpha = 2./(length+1)
		
	#	 stockprices, startday
		# float(STOCKAdj[startday]) - oldEMA[len(oldEMA)-1]
		
		## off by one error
	#	EMA = (float(STOCKAdj[startday])-oldEMA[len(oldEMA)-1])*alpha + oldEMA[len(oldEMA)-1]
		EMA = (float(stockprices[0])-oldEMA[len(oldEMA)-1])*alpha + oldEMA[len(oldEMA)-1]
		# Weight input EMA by day, farther back is multiplied by alpha^history
		#EMA PREVIOUS DAY (SUM)

	
		return EMA
	


"""
moving average convergence divergence
KDJ indicator
relative strength index
Williams %R
bias ratio
bollinger bands
fast stochastic oscillator
slow stochastic oscillator
commodity channel index
volume moving average
"""