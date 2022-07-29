def get_composite_indicator(norm_ind_vals):
	NUM_CATEGORIES = 7
	weights = [24.2, 16.2, 17.5, 13.6, 15.4, 3.0, 1.9]

	total = 0
	for i in range(0, NUM_CATEGORIES):
		total += norm_ind_vals[i] * weights[i]

	return total

def main():
	china = [5, 6, 7, 8, 9, 10, 11]
	us = [4, 6, 7, 8, 9, 10, 11]
	india = [3, 6, 7, 8, 9, 10, 11]

	countries = [get_composite_indicator(china), get_composite_indicator(us), get_composite_indicator(india)]

	maxi = -1
	for i in range(0, len(countries)):
		maxi = max(maxi, countries[i])

	for i in range(0, len(countries)):
		countries[i] = (countries[i] / maxi) * 100

	print(countries)

main()