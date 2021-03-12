input_list = []

with open("advent_2020-4-1_input.txt") as input_list:
# with open("example.txt") as input_list:
	input_list = input_list.readlines()
	input_list = [x.rstrip("\n") for x in input_list]

control_table = [0, 0, 0, 0, 0, 0, 0]
loop = 1
passport_counter = 0

def keyword_search(keyword, position, table, line):
	if keyword in line:
		table[position] = 1

for line in input_list:
	if line == "":
		if control_table == [1, 1, 1, 1, 1, 1, 1]:
			passport_counter += 1
			control_table = [0, 0, 0, 0, 0, 0, 0]
		else :
			control_table = [0, 0, 0, 0, 0, 0, 0]
			continue
	else:
		keyword_search("ecl", 0, control_table, line)
		keyword_search("pid", 1, control_table, line)
		keyword_search("eyr", 2, control_table, line)
		keyword_search("hcl", 3, control_table, line)
		keyword_search("byr", 4, control_table, line)
		keyword_search("iyr", 5, control_table, line)
		keyword_search("hgt", 6, control_table, line)
print(passport_counter)
