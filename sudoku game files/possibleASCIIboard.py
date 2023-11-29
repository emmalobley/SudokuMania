asciiBoard = "\=======+=======+=======/\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "+-------+-------+-------+\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "+-------+-------+-------+\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "/=======+=======+=======\ "

# random sudoku list to practice
board = [[0, 0, 0, 0, 2, 3, 8, 0, 0],
 [5, 9, 0, 7, 6, 4, 0, 0, 1],
 [7, 3, 2, 1, 0, 0, 0, 0, 0],
 [2, 0, 6, 0, 1, 8, 0, 7, 9],
 [3, 1, 5, 9, 7, 0, 0, 0, 8],
 [9, 8, 0, 0, 0, 0, 3, 0, 2],
 [0, 0, 0, 0, 0, 5, 7, 8, 0],
 [8, 0, 0, 0, 0, 1, 9, 0, 5],
 [0, 0, 9, 0, 3, 7, 1, 0, 0]]



# turn sudoku into single list
single_list = [num for slist in board for num in slist]

######################################
#
# zeros or dots?
#
# first option (dots)
#

result = []
index = 0
for char in asciiBoard:
    if char == '.':
        # Check if the number is 0
        if single_list[index] == 0:
            result.append('.')
        else:
            result.append(str(single_list[index]))
        index += 1
    else:
        result.append(char)

#
# second option (zeros)
#

# result = []
# index = 0
# for char in s:
#     if char == '.':
#         result.append(str(single_list[index]))
#         index += 1
#     else:
#         result.append(char)



# join and print
result_string = ''.join(result)
print(result_string)
