def get_composite_indicator(norm_ind_vals):
	weights = [
		0.1,
		0.1,
		0.1,
		0.1,
		0.1,
		0.1,
		0.0667,
		0.0667,
		0.0667,
		0.2
	]
	total = 0
	for x in range(len(weights)):
		total = total + (weights[x] * norm_ind_vals[x])
	
	return total

def main():
	LA = [
		10.999249,
		2.1032,
		0.76534,
		52,
		10224,
		50,
		1.5092,
		1935,
		0.00001429207,
		0.6292
	]
	indic_val = get_composite_indicator(LA)
	print(indic_val)

main()