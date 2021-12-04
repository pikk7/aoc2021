
# 3 nap, 1 part
def input_read(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        return lines


def get_bigger(dict):
    if(dict["zero"] > dict["one"]):
        return "0"
    else:
        return "1"


def get_smaller(dict):
    if(dict["zero"] == dict["one"]):
        return "0"
    if(dict["zero"] > dict["one"]):
        return "1"
    else:
        return "0"


def get_zeros_ones(lines):
    i = 0
    one = 0
    zero = 0

    j = 0
    line_end = len(lines[i])
    data = []
    while(j < line_end):
        i = 0
        one = 0
        zero = 0
        while(i < len(lines)):
            if(lines[i][j] == "0"):
                zero = zero+1
            else:
                one = one+1
            i = i+1
        j = j+1
        data.append({"zero": zero, "one": one})

    return data


def firts_task(lines):
    data = get_zeros_ones(lines)
    gamma = []
    epsilon = []
    for dict in data:
        gamma.append(get_bigger(dict))
        epsilon.append(get_smaller(dict))
    gamma_int = int("".join(gamma), 2)
    epsilon_int = int("".join(epsilon), 2)
    return (gamma_int*epsilon_int)


# 3nap, 2 part
def get_O2(bit_occurenses, lines):
    starting_string = ''
    o2 = ''
    i = 0
    while(i < len(bit_occurenses)):
        nummber_in_row = get_bigger(bit_occurenses[i])
        starting_string = starting_string+nummber_in_row
        filtered_list = [
            item for item in lines if item.startswith(starting_string)]
        if(len(filtered_list) == 1):
            o2 = filtered_list[0]
            return(int(o2, 2))
        bit_occurenses = (get_zeros_ones(filtered_list))
        i = i+1


def get_CO2(bit_occurenses, lines):
    starting_string = ''
    co2 = ''
    i = 0
    while(i < len(bit_occurenses)):
        nummber_in_row = get_smaller(bit_occurenses[i])
        starting_string = starting_string+nummber_in_row
        filtered_list = [
            item for item in lines if item.startswith(starting_string)]
        if(len(filtered_list) == 1):
            co2 = filtered_list[0]
            return(int(co2, 2))
        bit_occurenses = (get_zeros_ones(filtered_list))
        i = i+1


def second_task(lines):
    bit_occurenses = (get_zeros_ones(lines))
    o2 = get_O2(bit_occurenses, lines)
    co2 = get_CO2(bit_occurenses, lines)

    return(o2*co2)


if __name__ == '__main__':
    input_data = input_read("input.txt")
    print(firts_task(input_data))
    print(second_task(input_data))
