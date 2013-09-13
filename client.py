## OLD

import ystockquote
import technicals
import algorithm
import account
from numpy import *
from pylab import *

myaccount = account.account()

figure2 = figure()
lowerbox = figure2.add_subplot(111)
figure1 = figure()



upperbox = figure1.add_subplot(111)









startdate='20120101'
enddate='20121222'
# Get Quotes
GOOG = ystockquote.get_historical_prices('MSI', '20100101', '20120101')

# Create empty lists, quick and dirty
GOOGDate = []
GOOGOpen = []
GOOGHigh = []
GOOGLow = []
GOOGClose = []
GOOGVolume = []
GOOGAdj = [] #Adjusted Close


# Populate lists from downloaded data
def Populatelists():
	for i in range(1, len(GOOG)): #756
		GOOGDate.append(GOOG[i][0])
		GOOGOpen.append(GOOG[i][1])
		GOOGHigh.append(GOOG[i][2])
		GOOGLow.append(GOOG[i][3])
		GOOGClose.append(GOOG[i][4])
		GOOGVolume.append(GOOG[i][5])
		GOOGAdj.append(GOOG[i][6])
Populatelists()	

GOOGSMA=[]
GOOG200SMA=[]

def doSMA():
	for day in range(1, len(GOOGAdj)+1):
		GOOGSMA.append(technicals.simple_moving_average(GOOGAdj, day, 10)) #20

		GOOG200SMA.append(technicals.simple_moving_average(GOOGAdj, day, 200)) #20

GOOGEMA=[]
GOOG10EMA=[]
def doEMA():
	EMA=[]
	for day in range(1, len(GOOGAdj)+1):
		GOOGEMA.append(technicals.exponential_moving_average(GOOGAdj, day, 30, GOOGEMA))
		GOOG10EMA.append(technicals.exponential_moving_average(GOOGAdj, day, 10, GOOG10EMA))

def buyorders():
	buy = algorithm.buy(GOOGAdj, GOOGSMA) #GOOGSMA

	profit = 0
	marginalprofit=0
	bought =0
	boughtdate=0
	sold = 0

	for eachorder in buy:
		if eachorder[1]==1:
			bought = GOOGAdj[eachorder[0]]
			boughtdate = eachorder[0]
		if eachorder[1]==-1 and bought > 0:
			sold = GOOGAdj[eachorder[0]]
		if bought != 0 and sold != 0:
			marginalprofit=float(sold)-float(bought)
			profit +=marginalprofit
			if marginalprofit > 0:
				upperbox.axvspan(boughtdate, eachorder[0], color='green', alpha=0.5)
				upperbox.broken_barh([(boughtdate, eachorder[0]-boughtdate)], (float(bought), float(sold)-float(bought)), facecolors='green', alpha=0.5)
			if marginalprofit < 0:
				upperbox.axvspan(boughtdate, eachorder[0], color='red', alpha=0.5)
				upperbox.broken_barh([(boughtdate, eachorder[0]-boughtdate)], (float(bought), float(sold)-float(bought)), facecolors='red', alpha=0.5)

			bought = 0
			sold = 0
	print profit

def buyorders2():
	buy = algorithm.buyoncross(GOOGAdj, GOOGSMA, GOOGEMA, GOOG200SMA)
	
	profit = 0
	marginalprofit=0
	bought =0
	boughtdate=0
	sold = 0
	
	for eachorder in buy:
		boughtdate = eachorder[0]
		solddate = eachorder[1]
		bought = GOOGAdj[eachorder[0]]
		sold = GOOGAdj[eachorder[1]]

		shortorbuy = eachorder[2] #Returns 1 for buy, -1 for short

		marginalprofit=(float(sold)-float(bought))*shortorbuy
		print marginalprofit,
		profit +=marginalprofit
		
		#account
		quantity = int(myaccount.current / float(bought))
		prof = quantity * (float(sold)-float(bought))*shortorbuy
		myaccount.current += prof
		
		print prof, quantity, myaccount.current
		#end account
		
		if marginalprofit > 0:
			if eachorder[2] == 1:
				upperbox.axvspan(boughtdate, solddate, color='green', alpha=0.5)			
				upperbox.broken_barh([(boughtdate, solddate-boughtdate)], (float(sold), float(bought)-float(sold)), facecolors='green', alpha=0.5)
			elif eachorder[2] == -1:
				upperbox.axvspan(boughtdate, solddate, color='blue', alpha=0.5)
				upperbox.broken_barh([(boughtdate,solddate-boughtdate)], (float(sold), float(bought)-float(sold)), facecolors='blue', alpha=0.5)
			
		if marginalprofit < 0:
			if eachorder[2] == 1:
				upperbox.axvspan(boughtdate, solddate, color='red', alpha=0.5)
				upperbox.broken_barh([(boughtdate, solddate-boughtdate)], (float(sold), float(bought)-float(sold)), facecolors='red', alpha=0.5)
			if eachorder[2] == -1:
				upperbox.axvspan(boughtdate, solddate, color='orange', alpha=0.5)
				upperbox.broken_barh([(boughtdate, solddate-boughtdate)], (float(sold), float(bought)-float(sold)), facecolors='orange', alpha=0.5)

	
	myaccount.percentinc()


lowerbox.plot(GOOGVolume)

title("Google Adjusted Close from " + startdate + " to " + enddate)
ylabel(r"Google Closing Price ($USD)", fontsize = 12)
xlabel(r"Date", fontsize = 12)
grid(True)

class MyButton:
	ind = 0
	def SMA(self, event):
		doSMA()


		upperbox.plot(GOOGSMA)
		upperbox.plot(GOOG200SMA)
		

		
		draw()
		
	def EMA(self, event):
		doEMA()
		upperbox.plot(GOOGEMA)
		draw()
		
	def Colors(self, event):
		buyorders2()
		draw()

	def Populate(self, event):
		upperbox.plot(GOOGAdj)

		PopulateButton.disconnect(callback)
		draw()

	
callback = MyButton()
#				      x       y     hei   width
PopulateButton = Button(axes([0.0, 0, 0.2, 0.05]), 'Populate Graph')
PopulateButton.on_clicked(callback.Populate)

SMAButton = Button(axes([0.2, 0, 0.2, 0.05]), 'Show SMA')
SMAButton.on_clicked(callback.SMA)

EMAButton = Button(axes([0.4, 0, 0.2, 0.05]), 'Show EMA')
EMAButton.on_clicked(callback.EMA)


ColorsButton = Button(axes([0.8, 0, 0.2, 0.05]), 'Show Colors')
ColorsButton.on_clicked(callback.Colors)




show()