#======2======
def taxi_cost (distance, wait_time=0)-> int|None:
	if distance>0 and wait_time>=0:
		cost1=80+6*(distance/150)+3*wait_time
		cost1_fin=round(cost1)
		return cost1_fin
	
	elif distance==0 and wait_time>=0:
		cost2=80*2+3*wait_time
		cost2_fin=round(cost2)
		return cost2_fin
	
	elif distance<0 or wait_time<0:
		return None
		
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None
# >>> taxi_cost(0, 0)
# 160
# >>> print(taxi_cost(3605,-4))
# None