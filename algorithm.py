import technicals
import sys

def buy(STOCKAdj, TECHNICAL):
	"""ADD 10-Day SMA and 30 Day EMA, if lines cross, it shifts"""
	
	# If price > (20 day moving average) + Buffer	buy
	# If price < (20 day moving average) - Buffer	sell
	# Returns list [start, stop, start, stop] of when to buy.
	
	# Buffer is 2 percent:
	buffer = .02 #GETTING ONLY 1 DECIMAL
	
	
	# Creates list for each day: buy(1) sell(-1) or neither(0)

	#MARGINAL RETURNS VS MARGINAL LOSS
	# GRAPH X-Buffer, Y-Profit
	buysell = [ ]
	stockholder = [float(eachprice) for eachprice in STOCKAdj]
	STOCKAdj = stockholder
	
	for day in range(0, len(STOCKAdj)-1):
		minusbuffer = .02 * STOCKAdj[day]
		plusbuffer = .005 * STOCKAdj[day]
		
		if TECHNICAL[day] != None:
			# Increasing trend
			if STOCKAdj[day] > (TECHNICAL[day]+plusbuffer):
				buysell.append(1)
			# Decreasing trend
			elif STOCKAdj[day] < (TECHNICAL[day]-minusbuffer):
				buysell.append(-1)
			else:
				buysell.append(0)
		else:
			buysell.append(0)
	# Turn 1111111-1-1-1-1111110000-1-1-1 into list
	
	purchaseorder=[ ]
	
	for day in range(1, len(STOCKAdj)-1): # 1, to avoid buysell[-1]
		if buysell[day] != buysell[day-1] and buysell[day] != 0:
			if len(purchaseorder) == 0:
				purchaseorder.append([day, buysell[day]])
			elif purchaseorder[len(purchaseorder)-1][1] != buysell[day]:
				purchaseorder.append([day, buysell[day]])
				
	# purchaseorder
	return purchaseorder
	


def buyoncross(STOCKAdj, TenDaySMA, ThirtyDayEMA, SMA200):
	"""
	Buy stock when the TenDaySMA is greater than the ThirtyDayEMA AND Over 200 MSA
	Sell stock when the TenDaySMA is less than the ThirtyDayEMA or the STOCKAdj UNDER 200SMA
	"""
	buysell=[]
	
	stockholder = [float(eachprice) for eachprice in STOCKAdj]
	STOCKAdj = stockholder
	
	for day in range(0, len(STOCKAdj)-1):
		
		# Make sure both exist
		if TenDaySMA[day] != None and ThirtyDayEMA[day] != None and SMA200[day]!=None:
			
			# Positive trend -- buy
			if (TenDaySMA[day] >ThirtyDayEMA[day] and TenDaySMA[day] > SMA200[day]):
				buysell.append(1)
			elif (TenDaySMA[day] <ThirtyDayEMA[day] and TenDaySMA[day] < SMA200[day]):
				buysell.append(-1)
			else:
				buysell.append(0)
		else:
			buysell.append(0)
	

	
	# RETURN [date, date, +-1]
	porder=[]
	
	for day in range(1, len(STOCKAdj)-1): # 1, to avoid buysell[-1]
		if buysell[day] ==1 and buysell[day]!=buysell[day-1]:
			x = day
			while buysell[x]==1:
				x+=1
				if x == len(buysell):
					break
			x-=1
			porder.append([day,x,1])
		
		if buysell[day] ==-1 and buysell[day]!=buysell[day-1]:
			x = day
			while buysell[x]==-1:
				x+=1
				if x == len(buysell):
					break
			x-=1
			porder.append([day,x,-1])
	
	#
	return porder
	
	
	
	
	
	
	
	
	