class account:
	amount0 = 5000.	
	current = amount0
	
	
	def percentinc(self):
		print (self.current/self.amount0 - 1) * 100, "% increase"