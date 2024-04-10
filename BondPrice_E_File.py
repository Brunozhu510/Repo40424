def getBondPrice_E(face,couponRate,m,yc):
	pv = [(1+item) ** - (index+1) for index, item in enumerate(yc)]
	bondPrice = (sum(pv) * couponRate + PV[-1]) * face
	return(int(round(bondPrice,0)))


