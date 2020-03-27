
def rate(h=0, m=0):
	
	h2m = h*60
	
	total_min2sec = m*60 + (h2m*60)
	
	sec2millisec = total_min2sec*1000
	
	rate_of_change = sec2millisec/100
	
	return rate_of_change
	
p = rate(h=2, m=45)/1000
print(p)