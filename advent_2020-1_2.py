input_list = []
good_year_list = []

# je prends les éléments d'un fichier txt que je mets dans une liste
# j'enlève les sauts de lignes et je transforme les éléments en integer
with open("advent_2020-input-1_1.txt") as input_list:
    input_list = input_list.readlines()
    input_list = [x.rstrip("\n") for x in input_list]
    input_list = [int(x) for x in input_list]

last_value = -3
# je créé deux boucles imbriquées pour parcourir ma liste
for element in input_list:
    if element == input_list[last_value]:
        year = element+input_list[-1]+input_list[-2]
        if year == 2020:
            good_year_list.append(element*input_list[-1])
    else : 
        start_point = input_list.index(element)
        final_point = len(input_list)
        for element1 in input_list[start_point:final_point]:
            start_point1 = start_point+1
            for element2 in input_list[start_point1:final_point]:
                if element == element1:
                    continue
                else :
                    year = element+element1+element2
                    if year == 2020:
                        good_year_list.append(element*element1*element2)
print("solution seems to be", good_year_list)
solution = 0
for element in good_year_list:
    solution += element
print(solution)
             
