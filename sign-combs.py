"""

Jake Beason
Customizations ID generator

Program made for a friend applying a 
"combinations with replacement" problem
to customizing signs / lights on signs.

"""

# "combinations with replacment"
from itertools import combinations_with_replacement
import csv
import copy

# Options:
# - Up to 16 strobe lights (0 - 16)
# - For each light, up to 10 choices of color
COLORS = list(["blue", "green", "red", "white", "yellow", "sblue", "sgreen", "sred", "swhite", "syellow"])

print("   LIST OF ALL POSSIBLE COMBINATIONS   ")
print("---------------------------------------")


# no customizations is one potential combination,
# so let's initialize to one
total_count = 1

# loops from 1 to 16
# looping through the number of lights the customer wants
for num_lights in range(1, 17):


	# print combinations for current number of lights
	# TO DO: UNCOMMENT BELOW BLOCK FOR TESTING
	print("")
	print("COMBINATIONS FOR " + str(num_lights) + " LIGHTS")
	print("---------------------------------------")

	temp_count = 0
	for comb in combinations_with_replacement(COLORS, num_lights):
		temp_count += 1
		total_count += 1

		# print a single combination to 
		# a single row with items separated by a comma
		temp = copy.copy(comb)

		# print only for even sized combs
		if (len(temp) % 2) == 0:
			# write current comb to output file
			with open("16combs-10colors-even.csv", "a+") as of:
				wr = csv.writer(of)
				wr.writerow(temp)


	# print summary for current number of lights
	# TO DO: UNCOMMENT BELOW BLOCK FOR TESTING
	print("")
	print("=>" + str(temp_count) + " COMBS FOR " + str(num_lights) + " LIGHTS")


# print overall summary
# TO DO: UNCOMMENT BELOW BLOCK FOR TESTING
"""
print("")
print("---------------------------------------")
print("==> TOTAL COMBINATIONS: " + str(total_count))
"""