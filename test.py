import ticker
import algorithm
import draw
import money

def standard_trade(ticker):
    ticker.get_historical_prices()
    ticker.populate_lists()
    
    ticker.doSMA(10)
    ticker.doSMA(200)
    ticker.doEMA(30)

    order = algorithm.buyoncross(ticker.adj, ticker.sma[10], ticker.ema[30], ticker.sma[200])

    


    drawing = draw.Draw()
    drawing.lines.append(ticker.sma[10])
    drawing.lines.append(ticker.sma[200])
    drawing.lines.append(ticker.ema[30])

    drawing.buyorders(order, ticker.adj)
    drawing.add_lines()
    drawing.show()

goog = ticker.Ticker()
goog.symbol = 'GOOG'
goog.start_date = '20100101'
goog.end_date = '20120101'

msi = ticker.Ticker()
msi.symbol = 'MSI'
msi.start_date = '20100101'
msi.end_date = '20120101'



#standard_trade(goog)
standard_trade(msi)

print money.how_much_made(goog.adj, algorithm.buyoncross(goog.adj, goog.sma[10], goog.ema[30], goog.sma[200]), 5000)