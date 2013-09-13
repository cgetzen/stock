import pylab

class Draw:

    lines = []

    figure = pylab.figure()
    subfigure = figure.add_subplot(111)

    def buyorders(self, porder , price):
	
	marginalprofit = 0
	bought = 0
	bought_date = 0
	sold_date = 0
	sold = 0
	

	for order in porder:
	    
	    bought_date = order[0]
	    sold_date = order[1]
	    bought_price = price[bought_date]
	    sold_price = price[sold_date]

	    shortorbuy = order[2] # 1: buy, -1: short 

	    marginalprofit = (float(sold_price)-float(bought_price))*shortorbuy
	    
	    if marginalprofit > 0:
		if order[2] == 1:
		    self.subfigure.axvspan(bought_date, sold_date, color='green', alpha=0.5)
		    self.subfigure.broken_barh([(bought_date, sold_date-bought_date)], (float(sold_price), float(bought_price)-float(sold_price)), facecolors='green', alpha=0.5)
		elif order[2] == -1:
		    self.subfigure.axvspan(bought_date, sold_date, color='blue', alpha=0.5)
		    self.subfigure.broken_barh([(bought_date,sold_date-bought_date)], (float(sold_price), float(bought_price)-float(sold_price)), facecolors='blue', alpha=0.5)
	    if marginalprofit < 0:
		if order[2] == 1:
		    self.subfigure.axvspan(bought_date, sold_date, color='red', alpha=0.5)
		    self.subfigure.broken_barh([(bought_date, sold_date-bought_date)], (float(sold_price), float(bought_price)-float(sold_price)), facecolors='red', alpha=0.5)
		if order[2] == -1:
		    self.subfigure.axvspan(bought_date, sold_date, color='orange', alpha=0.5)
		    self.subfigure.broken_barh([(bought_date, sold_date-bought_date)], (float(sold_price), float(bought_price)-float(sold_price)), facecolors='orange', alpha=0.5)

    def add_lines(self):
	for graph in self.lines:
	    self.subfigure.plot(graph)

    def show(self):
	pylab.show()