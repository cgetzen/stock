import ystockquote
import technicals
import string
class Ticker:
    


#################################	VARIABLES	#################################
    ## USER MUST INPUT symbol, startdate, AND enddate
    symbol = ''

    start_date = ''
    end_date = ''

    data = '' # Stores all info in one large list
    data_headers = ''
    '''
    ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    ['2012-01-20', '590.53', '591.00', '581.70', '585.99', '10576300', '585.99']
    ['2012-01-19', '640.99', '640.99', '631.46', '639.57', '6305300', '639.57']
    ['2012-01-18', '626.63', '634.00', '622.12', '632.91', '2761700', '632.91']
    ['2012-01-17', '631.98', '631.98', '625.68', '628.58', '1909300', '628.58']
    ['2012-01-13', '626.26', '626.95', '621.06', '624.99', '2307300', '624.99']
    '''
    
    date = 	[]
    open = 	[]
    high = 	[]
    low = 	[]
    close = 	[]
    volume = 	[]
    adj = 	[] # Adjusted close

    # averages should be a dictionary, where index is day number

    sma = {}	# Simple Moving Average
    ema = {}	# Exponential Moving Average

#################################	FUNCTIONS	#################################

    def get_historical_prices(self):
	data = ystockquote.get_historical_prices(self.symbol, self.start_date, self.end_date)
	data_headers = data[0]
	data.pop(0)
	
	self.data = data[::-1]
	self.data_headers = data_headers

    def populate_lists(self):
	for i in range(0, len(self.data)):
	    self.date.append(self.data[i][0])
	    self.open.append(float(self.data[i][1]))
	    self.high.append(float(self.data[i][2]))
	    self.low.append(float(self.data[i][3]))
	    self.close.append(float(self.data[i][4]))
	    self.volume.append(float(self.data[i][5]))
	    self.adj.append(float(self.data[i][6]))



    def doSMA(self, length):
	self.sma[length] = technicals.sma(self.adj, length)

    def doEMA(self, length):
	self.ema[length] = technicals.ema(self.adj, length)


    def print_data(self, *args):
	for x in args:
	    if x is 'raw_data':
		matrix = self.data
		matrix.insert(0, self.data_headers)
		max_lens = [max([len(str(r[i])) for r in matrix]) for i in range(len(matrix[0]))]
		print "\n".join(["".join([string.ljust(str(e), l + 2) for e, l in zip(r, max_lens)]) for r in matrix])

	    if x is 'sma':
		for key in self.sma.keys():
		    print ''.join([str(key), '-day Simple Moving Average'])
		    matrix = []
		    for day in range(0,len(self.date)):
			matrix.append([self.date[day], self.sma[key][day]])
		    
		    max_lens = [max([len(str(r[i])) for r in matrix]) for i in range(len(matrix[0]))]
		    print "\n".join(["".join([string.ljust(str(e), l + 2) for e, l in zip(r, max_lens)]) for r in matrix])
		    print ''

	    if x is 'ema':
		for key in self.ema.keys():
		    print ''.join([str(key), '-day Exponential Moving Average'])
		    matrix = []
		    for day in range(0,len(self.date)):
			matrix.append([self.date[day], self.ema[key][day]])
		    
		    max_lens = [max([len(str(r[i])) for r in matrix]) for i in range(len(matrix[0]))]
		    print "\n".join(["".join([string.ljust(str(e), l + 2) for e, l in zip(r, max_lens)]) for r in matrix])
		    print ''






















