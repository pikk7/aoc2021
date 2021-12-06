
# 4 nap, 1 part


def input_read(file_name):
    f = open(file_name, 'r')
    global pulled_number
    pulled_number = f.readline().split(',')
    f.readline()
    content = f.readlines()

    lines = [line.strip() for line in content]
    # print(pulled_number)
    matrix = []
    for line in lines:
        matrix.append(line.split())

    f.close()
    return matrix


def firts_task(list_of_matrixies):
    choosen_matrix = []
    not_found = True
    last_num = 0
    for numb in pulled_number:
        i = 0
        while(i < len(list_of_matrixies) and not_found):
            list_of_matrixies[i] = mark_element(numb, list_of_matrixies[i])
            if(is_over(list_of_matrixies[i])):
                choosen_matrix = list_of_matrixies[i]
                not_found = False
                last_num = int(numb)
            i = i+1
    return (sum_num(choosen_matrix)*last_num)


def matrix5x5(matrix):
    del matrix[6-1::6]
    composite_list = [matrix[x:x+5] for x in range(0, len(matrix), 5)]

    return(composite_list)


def mark_element(element, matrix):
    i = 0
    while(i < len(matrix)):
        j = 0
        while(j < len(matrix[i])):
            if(element == matrix[i][j]):
                matrix[i][j] = "B"+matrix[i][j]

            j = j+1
        i = i+1
    return matrix


def is_over(matrix):
    return is_over_row(matrix) or is_over_col(matrix)


def is_over_row(matrix):
    return row0(matrix) or row1(matrix) or row2(matrix) or row3(matrix) or row4(matrix)


def row0(matrix):
    return (matrix[0][0].startswith('B') and matrix[0][1].startswith('B') and matrix[0][2].startswith('B') and matrix[0][3].startswith('B') and matrix[0][4].startswith('B'))


def row1(matrix):
    return (matrix[1][0].startswith('B') and matrix[1][1].startswith('B') and matrix[1][2].startswith('B') and matrix[1][3].startswith('B') and matrix[1][4].startswith('B'))


def row2(matrix):
    return (matrix[2][0].startswith('B') and matrix[2][1].startswith('B') and matrix[2][2].startswith('B') and matrix[2][3].startswith('B') and matrix[2][4].startswith('B'))


def row3(matrix):
    return (matrix[3][0].startswith('B') and matrix[3][1].startswith('B') and matrix[3][2].startswith('B') and matrix[3][3].startswith('B') and matrix[3][4].startswith('B'))


def row4(matrix):
    return (matrix[4][0].startswith('B') and matrix[4][1].startswith('B') and matrix[4][2].startswith('B') and matrix[4][3].startswith('B') and matrix[4][4].startswith('B'))


def is_over_col(matrix):
    return (matrix[0][0].startswith('B') and matrix[1][0].startswith('B') and matrix[2][0].startswith('B') and matrix[3][0].startswith('B') and matrix[4][0].startswith('B')) or (matrix[0][1].startswith('B') and matrix[1][1].startswith('B') and matrix[2][1].startswith('B') and matrix[3][1].startswith('B') and matrix[4][1].startswith('B')) or (matrix[0][2].startswith('B') and matrix[1][2].startswith('B') and matrix[2][2].startswith('B') and matrix[3][2].startswith('B') and matrix[4][2].startswith('B')) or (matrix[0][3].startswith('B') and matrix[1][3].startswith('B') and matrix[2][3].startswith('B') and matrix[3][3].startswith('B') and matrix[4][3].startswith('B')) or (matrix[0][4].startswith('B') and matrix[1][4].startswith('B') and matrix[2][4].startswith('B') and matrix[3][4].startswith('B') and matrix[4][4].startswith('B'))


def sum_num(matrix):
    i = 0
    sum = 0
    while(i < len(matrix)):
        j = 0
        while(j < len(matrix[i])):
            current = matrix[i][j]
            if(not current.startswith("B")):
                sum = sum+int(current)
            j = j+1
        i = i+1
    return sum


def second_task(list_of_matrixies):
    choosen_matrix = []
    not_found = True
    not_last = True
    index = 0
    j = 0
    while(j < len(pulled_number) and not_found):
        numb = pulled_number[j]
        i = 0
        while(i < len(list_of_matrixies) and not_found):
            list_of_matrixies[i] = mark_element(numb, list_of_matrixies[i])
            if(is_over(list_of_matrixies[i]) and not_last):
                del list_of_matrixies[i]
                list_of_matrixies = list(list_of_matrixies)

            if(len(list_of_matrixies) == 1):
                not_last = False
                k = 0
                while(k < len(list_of_matrixies) and not_found):
                    list_of_matrixies[k] = mark_element(
                        numb, list_of_matrixies[k])
                    if(is_over(list_of_matrixies[k])):
                        choosen_matrix = list_of_matrixies[k]
                        not_found = False
                        last_num = int(numb)
                    k = k+1

            i = i+1
        j = j+1
    print(choosen_matrix)
    return (sum_num(choosen_matrix)*last_num)


if __name__ == '__main__':
    input_data = input_read("input.txt")
    # print(firts_task(matrix5x5(input_data)))
    print(second_task(matrix5x5(input_data)))
