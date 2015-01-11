# with open ("states.txt", "r") as states_file:
# 	states = states_file.read().split("\n")
# print states


# with open("states.csv", "r") as states_file:
# 	states = states_file.read().split("\n")
# 	for index, state in enumerate(states):
# 		states[index] = state.split(",")
# print states

abr = []
sname = []
with open("states.csv", "r") as states_file:
	states = states_file.read().split("\n")
	for index, state in enumerate(states):
		abbreviation, statename = state.split(",")
 		abr.append(abbreviation)
 		sname.append(statename)
print abr
print sname


