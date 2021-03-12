input_list = []

with open("advent_2020-3-1_input.txt") as input_list:
# with open("test.txt") as input_list:
	# for line in input_list.readlines(): count += 1
	input_list = input_list.readlines()
	input_list = [x.rstrip("\n") for x in input_list]

line_result, char_result = (len(input_list), len(input_list[0]))

# line_result = -1
# for line in input_list:
	# line_result += 1

# char_result = -1
# for char in input_list[0]:
	# char_result += 1
print("nombre de lignes dans le tableau", line_result)
print("nombre de caractères par ligne", char_result)

iterator =[0 ,1 ,2 ,3 ,4]
value_down = [1, 1, 1, 1, 2]
value_right = [1, 3, 5, 7, 1]

check = True

result = []

def horizontal_check(v, current_h, max, down):
	v += down
	increment = current_h - max
	h = 0
	h += increment
	return v, h

def vertical_check(v, max):
	if v <= max-1:
		return True
	else :
		return False

def symbol_check(symbol):
	if symbol == "#":
		return 1
	else :
		return 0
for item in iterator:
	h_cursor = 0
	v_cursor = 0
	tree_result = 0
	print(item)
	print(value_right[item], value_down[item])
	while check == True:
		if v_cursor >= line_result-1:
			break
		else :
			h_cursor += value_right[item]
			if h_cursor > char_result-1:
				v_cursor, h_cursor = horizontal_check(v_cursor, h_cursor, char_result, value_down[item])
				tree_result += symbol_check(input_list[v_cursor][h_cursor])
			else :
				v_cursor += value_down[item]
				tree_result += symbol_check(input_list[v_cursor][h_cursor])
		check = vertical_check(v_cursor, line_result)
		print("dans la table",v_cursor, h_cursor, "symbole", input_list[v_cursor][h_cursor], "résultat", tree_result)
	result.append(tree_result)

final_result = result[0]*result[1]*result[2]*result[3]*result[4]

print("le résultat final est :", final_result)
