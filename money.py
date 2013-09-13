def how_much_made(adj, porder, starting):
    profit = 0

    for order in porder:
	bought_date = order[0]
	sold_date = order[1]
	bought_price = adj[bought_date]
	sold_price = adj[sold_date]

	shortorbuy = order[2]

	quantity = starting/bought_price

	profit =  (sold_price - bought_price)*quantity*shortorbuy
	starting+=profit
    return starting